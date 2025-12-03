"""
SeniorCare - AI Caregiver Companion
Backend Flask para a aplicação mobile de cuidado a idosos
"""

import os
import sys
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# Inicialização da app
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Configuração
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configurar DATABASE_URL
database_url = os.environ.get('DATABASE_URL', '')
if database_url:
    # Render usa postgres:// mas SQLAlchemy precisa de postgresql://
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    # Verificar qual driver PostgreSQL está disponível
    try:
        import psycopg2
        # psycopg2 disponível - usar driver padrão
        pass
    except ImportError:
        try:
            import psycopg
            # psycopg3 disponível - usar driver específico
            if 'postgresql://' in database_url and '+' not in database_url.split('://')[0]:
                database_url = database_url.replace('postgresql://', 'postgresql+psycopg://', 1)
        except ImportError:
            print("Aviso: Nenhum driver PostgreSQL encontrado. A usar SQLite.")
            database_url = ''
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Fallback para SQLite local
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seniorcare.db'

# Log da configuração (sem password)
db_uri_safe = app.config['SQLALCHEMY_DATABASE_URI']
if '@' in db_uri_safe:
    # Esconder password no log
    parts = db_uri_safe.split('@')
    db_uri_safe = parts[0].rsplit(':', 1)[0] + ':***@' + parts[1]
print(f"Database: {db_uri_safe}")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
}

# Inicialização das extensões
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ==================== MODELOS ====================

class User(db.Model):
    """Utilizador principal (idoso)"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True)
    pin = db.Column(db.String(256))  # PIN simples para acesso
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Preferências
    wake_time = db.Column(db.Time, default=datetime.strptime('07:00', '%H:%M').time())
    sleep_time = db.Column(db.Time, default=datetime.strptime('22:00', '%H:%M').time())
    language = db.Column(db.String(10), default='pt')
    
    # Relações
    medications = db.relationship('Medication', backref='user', lazy=True, cascade='all, delete-orphan')
    contacts = db.relationship('Contact', backref='user', lazy=True, cascade='all, delete-orphan')
    activities = db.relationship('Activity', backref='user', lazy=True, cascade='all, delete-orphan')
    alerts = db.relationship('Alert', backref='user', lazy=True, cascade='all, delete-orphan')
    mood_logs = db.relationship('MoodLog', backref='user', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'last_active': self.last_active.isoformat() if self.last_active else None,
            'wake_time': self.wake_time.strftime('%H:%M') if self.wake_time else None,
            'sleep_time': self.sleep_time.strftime('%H:%M') if self.sleep_time else None,
        }


class Caregiver(db.Model):
    """Cuidador/Familiar com acesso ao painel"""
    __tablename__ = 'caregivers'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(20), default='family')  # family, professional, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relação com utilizadores que cuida
    users = db.relationship('CaregiverUser', backref='caregiver', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'phone': self.phone,
            'role': self.role,
        }


class CaregiverUser(db.Model):
    """Relação entre cuidadores e utilizadores"""
    __tablename__ = 'caregiver_users'
    
    id = db.Column(db.Integer, primary_key=True)
    caregiver_id = db.Column(db.Integer, db.ForeignKey('caregivers.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    relationship = db.Column(db.String(50))  # filho, filha, neto, cuidador profissional
    is_primary = db.Column(db.Boolean, default=False)
    notify_alerts = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Medication(db.Model):
    """Medicamentos e horários"""
    __tablename__ = 'medications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50))
    instructions = db.Column(db.Text)
    icon = db.Column(db.String(10), default='💊')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Horários
    schedules = db.relationship('MedicationSchedule', backref='medication', lazy=True, cascade='all, delete-orphan')
    logs = db.relationship('MedicationLog', backref='medication', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dosage': self.dosage,
            'instructions': self.instructions,
            'icon': self.icon,
            'is_active': self.is_active,
            'schedules': [s.to_dict() for s in self.schedules],
        }


class MedicationSchedule(db.Model):
    """Horários de cada medicamento"""
    __tablename__ = 'medication_schedules'
    
    id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'), nullable=False)
    time = db.Column(db.Time, nullable=False)
    days_of_week = db.Column(db.String(20), default='0123456')  # 0=Dom, 1=Seg, etc.
    
    def to_dict(self):
        return {
            'id': self.id,
            'time': self.time.strftime('%H:%M'),
            'days_of_week': self.days_of_week,
        }


class MedicationLog(db.Model):
    """Registo de medicação tomada"""
    __tablename__ = 'medication_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'), nullable=False)
    schedule_id = db.Column(db.Integer, db.ForeignKey('medication_schedules.id'))
    scheduled_time = db.Column(db.DateTime, nullable=False)
    taken_at = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='pending')  # pending, taken, skipped, late
    notes = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'medication_id': self.medication_id,
            'scheduled_time': self.scheduled_time.isoformat(),
            'taken_at': self.taken_at.isoformat() if self.taken_at else None,
            'status': self.status,
        }


class Contact(db.Model):
    """Contactos de emergência e família"""
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    relationship = db.Column(db.String(50))
    avatar = db.Column(db.String(10), default='👤')
    is_emergency = db.Column(db.Boolean, default=False)
    priority = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'relationship': self.relationship,
            'avatar': self.avatar,
            'is_emergency': self.is_emergency,
        }


class Activity(db.Model):
    """Atividades da rotina diária"""
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    time = db.Column(db.Time)
    icon = db.Column(db.String(10), default='📋')
    category = db.Column(db.String(50))  # health, meal, exercise, social, other
    is_recurring = db.Column(db.Boolean, default=True)
    days_of_week = db.Column(db.String(20), default='0123456')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'time': self.time.strftime('%H:%M') if self.time else None,
            'icon': self.icon,
            'category': self.category,
        }


class Alert(db.Model):
    """Alertas e notificações"""
    __tablename__ = 'alerts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # emergency, medication_missed, inactivity, fall, mood
    severity = db.Column(db.String(20), default='medium')  # low, medium, high, critical
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)
    resolved_by = db.Column(db.Integer, db.ForeignKey('caregivers.id'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'severity': self.severity,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
            'resolved_at': self.resolved_at.isoformat() if self.resolved_at else None,
        }


class MoodLog(db.Model):
    """Registo de estado emocional"""
    __tablename__ = 'mood_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mood = db.Column(db.String(20))  # happy, neutral, sad, anxious, tired
    energy_level = db.Column(db.Integer)  # 1-5
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'mood': self.mood,
            'energy_level': self.energy_level,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
        }


class ChatMessage(db.Model):
    """Histórico de conversas com o assistente"""
    __tablename__ = 'chat_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # user, assistant
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ==================== AUTENTICAÇÃO ====================

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            return jsonify({'error': 'Token em falta'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            if data.get('type') == 'user':
                current_user = User.query.get(data['id'])
            else:
                current_user = Caregiver.query.get(data['id'])
            if not current_user:
                return jsonify({'error': 'Utilizador não encontrado'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


def generate_token(user_id, user_type='user', expires_hours=24*30):
    return jwt.encode({
        'id': user_id,
        'type': user_type,
        'exp': datetime.utcnow() + timedelta(hours=expires_hours)
    }, app.config['SECRET_KEY'], algorithm='HS256')


# ==================== ROTAS - FRONTEND ====================

@app.route('/')
def index():
    """Página principal - PWA Mobile"""
    return render_template('index.html')


@app.route('/manifest.json')
def manifest():
    """PWA Manifest"""
    return send_from_directory('static', 'manifest.json')


@app.route('/sw.js')
def service_worker():
    """Service Worker para PWA"""
    return send_from_directory('static', 'sw.js')


@app.route('/healthz')
def health_check():
    """Health check para o Render"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()})


# ==================== ROTAS - API ====================

@app.route('/api/auth/register', methods=['POST'])
def register_user():
    """Registar novo utilizador (idoso)"""
    data = request.get_json()
    
    if not data.get('name'):
        return jsonify({'error': 'Nome é obrigatório'}), 400
    
    user = User(
        name=data['name'],
        phone=data.get('phone'),
    )
    
    if data.get('pin'):
        user.pin = generate_password_hash(str(data['pin']))
    
    db.session.add(user)
    db.session.commit()
    
    token = generate_token(user.id, 'user')
    
    return jsonify({
        'user': user.to_dict(),
        'token': token
    }), 201


@app.route('/api/auth/login', methods=['POST'])
def login_user():
    """Login com PIN ou telefone"""
    data = request.get_json()
    
    user = None
    if data.get('phone'):
        user = User.query.filter_by(phone=data['phone']).first()
    elif data.get('user_id'):
        user = User.query.get(data['user_id'])
    
    if not user:
        return jsonify({'error': 'Utilizador não encontrado'}), 404
    
    # Verificar PIN se existir
    if user.pin and data.get('pin'):
        if not check_password_hash(user.pin, str(data['pin'])):
            return jsonify({'error': 'PIN incorreto'}), 401
    
    # Atualizar última atividade
    user.last_active = datetime.utcnow()
    db.session.commit()
    
    token = generate_token(user.id, 'user')
    
    return jsonify({
        'user': user.to_dict(),
        'token': token
    })


@app.route('/api/user/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    """Obter perfil do utilizador"""
    return jsonify(current_user.to_dict())


@app.route('/api/user/activity', methods=['POST'])
@token_required
def update_activity(current_user):
    """Atualizar última atividade (heartbeat)"""
    current_user.last_active = datetime.utcnow()
    db.session.commit()
    return jsonify({'status': 'ok'})


# ==================== MEDICAÇÃO ====================

@app.route('/api/medications', methods=['GET'])
@token_required
def get_medications(current_user):
    """Listar medicamentos do utilizador"""
    medications = Medication.query.filter_by(
        user_id=current_user.id,
        is_active=True
    ).all()
    return jsonify([m.to_dict() for m in medications])


@app.route('/api/medications', methods=['POST'])
@token_required
def add_medication(current_user):
    """Adicionar medicamento"""
    data = request.get_json()
    
    medication = Medication(
        user_id=current_user.id,
        name=data['name'],
        dosage=data.get('dosage'),
        instructions=data.get('instructions'),
        icon=data.get('icon', '💊'),
    )
    db.session.add(medication)
    db.session.flush()
    
    # Adicionar horários
    for schedule in data.get('schedules', []):
        time = datetime.strptime(schedule['time'], '%H:%M').time()
        med_schedule = MedicationSchedule(
            medication_id=medication.id,
            time=time,
            days_of_week=schedule.get('days_of_week', '0123456')
        )
        db.session.add(med_schedule)
    
    db.session.commit()
    return jsonify(medication.to_dict()), 201


@app.route('/api/medications/today', methods=['GET'])
@token_required
def get_today_medications(current_user):
    """Obter medicações de hoje com estado"""
    today = datetime.utcnow().date()
    day_of_week = str(today.weekday())
    
    medications = Medication.query.filter_by(
        user_id=current_user.id,
        is_active=True
    ).all()
    
    result = []
    for med in medications:
        for schedule in med.schedules:
            if day_of_week in schedule.days_of_week:
                # Verificar se já foi tomado
                scheduled_datetime = datetime.combine(today, schedule.time)
                log = MedicationLog.query.filter_by(
                    medication_id=med.id,
                    schedule_id=schedule.id,
                    scheduled_time=scheduled_datetime
                ).first()
                
                result.append({
                    'id': med.id,
                    'schedule_id': schedule.id,
                    'name': med.name,
                    'dosage': med.dosage,
                    'time': schedule.time.strftime('%H:%M'),
                    'icon': med.icon,
                    'taken': log.status == 'taken' if log else False,
                    'taken_at': log.taken_at.isoformat() if log and log.taken_at else None,
                })
    
    # Ordenar por hora
    result.sort(key=lambda x: x['time'])
    return jsonify(result)


@app.route('/api/medications/<int:med_id>/take', methods=['POST'])
@token_required
def take_medication(current_user, med_id):
    """Marcar medicamento como tomado"""
    data = request.get_json()
    schedule_id = data.get('schedule_id')
    
    medication = Medication.query.filter_by(
        id=med_id,
        user_id=current_user.id
    ).first_or_404()
    
    today = datetime.utcnow().date()
    schedule = MedicationSchedule.query.get(schedule_id)
    scheduled_datetime = datetime.combine(today, schedule.time) if schedule else datetime.utcnow()
    
    # Criar ou atualizar log
    log = MedicationLog.query.filter_by(
        medication_id=med_id,
        schedule_id=schedule_id,
        scheduled_time=scheduled_datetime
    ).first()
    
    if not log:
        log = MedicationLog(
            medication_id=med_id,
            schedule_id=schedule_id,
            scheduled_time=scheduled_datetime
        )
        db.session.add(log)
    
    log.taken_at = datetime.utcnow()
    log.status = 'taken'
    
    db.session.commit()
    return jsonify({'status': 'ok', 'log': log.to_dict()})


# ==================== CONTACTOS ====================

@app.route('/api/contacts', methods=['GET'])
@token_required
def get_contacts(current_user):
    """Listar contactos"""
    contacts = Contact.query.filter_by(user_id=current_user.id).order_by(Contact.priority.desc()).all()
    return jsonify([c.to_dict() for c in contacts])


@app.route('/api/contacts', methods=['POST'])
@token_required
def add_contact(current_user):
    """Adicionar contacto"""
    data = request.get_json()
    
    contact = Contact(
        user_id=current_user.id,
        name=data['name'],
        phone=data['phone'],
        relationship=data.get('relationship'),
        avatar=data.get('avatar', '👤'),
        is_emergency=data.get('is_emergency', False),
        priority=data.get('priority', 0),
    )
    db.session.add(contact)
    db.session.commit()
    
    return jsonify(contact.to_dict()), 201


# ==================== ATIVIDADES ====================

@app.route('/api/activities', methods=['GET'])
@token_required
def get_activities(current_user):
    """Listar atividades de hoje"""
    today = datetime.utcnow().date()
    day_of_week = str(today.weekday())
    
    activities = Activity.query.filter_by(user_id=current_user.id).all()
    
    result = []
    for activity in activities:
        if day_of_week in activity.days_of_week:
            result.append(activity.to_dict())
    
    # Ordenar por hora
    result.sort(key=lambda x: x['time'] or '23:59')
    return jsonify(result)


@app.route('/api/activities', methods=['POST'])
@token_required
def add_activity(current_user):
    """Adicionar atividade"""
    data = request.get_json()
    
    time = None
    if data.get('time'):
        time = datetime.strptime(data['time'], '%H:%M').time()
    
    activity = Activity(
        user_id=current_user.id,
        title=data['title'],
        description=data.get('description'),
        time=time,
        icon=data.get('icon', '📋'),
        category=data.get('category'),
        days_of_week=data.get('days_of_week', '0123456'),
    )
    db.session.add(activity)
    db.session.commit()
    
    return jsonify(activity.to_dict()), 201


# ==================== ALERTAS ====================

@app.route('/api/alerts/emergency', methods=['POST'])
@token_required
def create_emergency(current_user):
    """Criar alerta de emergência"""
    data = request.get_json()
    
    alert = Alert(
        user_id=current_user.id,
        type='emergency',
        severity='critical',
        message=data.get('message', 'Pedido de ajuda de emergência'),
    )
    db.session.add(alert)
    db.session.commit()
    
    # TODO: Enviar notificações para cuidadores (WhatsApp, SMS, Push)
    
    return jsonify(alert.to_dict()), 201


@app.route('/api/alerts', methods=['GET'])
@token_required
def get_alerts(current_user):
    """Listar alertas recentes"""
    alerts = Alert.query.filter_by(user_id=current_user.id).order_by(Alert.created_at.desc()).limit(50).all()
    return jsonify([a.to_dict() for a in alerts])


# ==================== HUMOR/BEM-ESTAR ====================

@app.route('/api/mood', methods=['POST'])
@token_required
def log_mood(current_user):
    """Registar estado emocional"""
    data = request.get_json()
    
    mood_log = MoodLog(
        user_id=current_user.id,
        mood=data.get('mood'),
        energy_level=data.get('energy_level'),
        notes=data.get('notes'),
    )
    db.session.add(mood_log)
    db.session.commit()
    
    return jsonify(mood_log.to_dict()), 201


@app.route('/api/mood/recent', methods=['GET'])
@token_required
def get_recent_mood(current_user):
    """Obter registos de humor recentes"""
    logs = MoodLog.query.filter_by(user_id=current_user.id).order_by(MoodLog.created_at.desc()).limit(30).all()
    return jsonify([l.to_dict() for l in logs])


# ==================== CHAT/COMPANHIA ====================

@app.route('/api/chat/messages', methods=['GET'])
@token_required
def get_chat_history(current_user):
    """Obter histórico de mensagens"""
    messages = ChatMessage.query.filter_by(user_id=current_user.id).order_by(ChatMessage.created_at.desc()).limit(50).all()
    return jsonify([{
        'id': m.id,
        'role': m.role,
        'content': m.content,
        'created_at': m.created_at.isoformat()
    } for m in reversed(messages)])


@app.route('/api/chat/send', methods=['POST'])
@token_required
def send_chat_message(current_user):
    """Enviar mensagem e obter resposta"""
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Guardar mensagem do utilizador
    user_msg = ChatMessage(
        user_id=current_user.id,
        role='user',
        content=user_message
    )
    db.session.add(user_msg)
    
    # TODO: Integrar com AI (Claude API) para respostas inteligentes
    # Por agora, respostas simples
    responses = [
        f"Olá {current_user.name}! Como posso ajudar?",
        "Que bom falar consigo! O dia está bonito lá fora.",
        "Estou aqui para o que precisar. Quer conversar um pouco?",
        "Já tomou a sua medicação hoje?",
        "Lembre-se de beber água regularmente!",
    ]
    
    import random
    ai_response = random.choice(responses)
    
    # Guardar resposta do assistente
    assistant_msg = ChatMessage(
        user_id=current_user.id,
        role='assistant',
        content=ai_response
    )
    db.session.add(assistant_msg)
    db.session.commit()
    
    return jsonify({
        'user_message': {
            'id': user_msg.id,
            'role': 'user',
            'content': user_message,
            'created_at': user_msg.created_at.isoformat()
        },
        'assistant_message': {
            'id': assistant_msg.id,
            'role': 'assistant',
            'content': ai_response,
            'created_at': assistant_msg.created_at.isoformat()
        }
    })


# ==================== DASHBOARD CUIDADOR ====================

@app.route('/api/caregiver/register', methods=['POST'])
def register_caregiver():
    """Registar cuidador/familiar"""
    data = request.get_json()
    
    if Caregiver.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email já registado'}), 400
    
    caregiver = Caregiver(
        email=data['email'],
        name=data['name'],
        phone=data.get('phone'),
        role=data.get('role', 'family'),
    )
    caregiver.set_password(data['password'])
    
    db.session.add(caregiver)
    db.session.commit()
    
    token = generate_token(caregiver.id, 'caregiver')
    
    return jsonify({
        'caregiver': caregiver.to_dict(),
        'token': token
    }), 201


@app.route('/api/caregiver/login', methods=['POST'])
def login_caregiver():
    """Login do cuidador"""
    data = request.get_json()
    
    caregiver = Caregiver.query.filter_by(email=data['email']).first()
    
    if not caregiver or not caregiver.check_password(data['password']):
        return jsonify({'error': 'Credenciais inválidas'}), 401
    
    token = generate_token(caregiver.id, 'caregiver')
    
    return jsonify({
        'caregiver': caregiver.to_dict(),
        'token': token
    })


@app.route('/api/caregiver/users/<int:user_id>/summary', methods=['GET'])
@token_required
def get_user_summary(current_caregiver, user_id):
    """Obter resumo do estado do utilizador (para cuidador)"""
    # Verificar se tem acesso
    access = CaregiverUser.query.filter_by(
        caregiver_id=current_caregiver.id,
        user_id=user_id
    ).first()
    
    if not access:
        return jsonify({'error': 'Sem acesso a este utilizador'}), 403
    
    user = User.query.get_or_404(user_id)
    
    # Estatísticas
    today = datetime.utcnow().date()
    
    # Medicação de hoje
    med_logs = MedicationLog.query.join(Medication).filter(
        Medication.user_id == user_id,
        db.func.date(MedicationLog.scheduled_time) == today
    ).all()
    
    meds_taken = len([l for l in med_logs if l.status == 'taken'])
    meds_total = len(med_logs)
    
    # Alertas não resolvidos
    pending_alerts = Alert.query.filter_by(
        user_id=user_id,
        resolved_at=None
    ).count()
    
    # Último humor registado
    last_mood = MoodLog.query.filter_by(user_id=user_id).order_by(MoodLog.created_at.desc()).first()
    
    return jsonify({
        'user': user.to_dict(),
        'last_active': user.last_active.isoformat() if user.last_active else None,
        'medications_today': {
            'taken': meds_taken,
            'total': meds_total,
        },
        'pending_alerts': pending_alerts,
        'last_mood': last_mood.to_dict() if last_mood else None,
    })


# ==================== INICIALIZAÇÃO ====================

def init_db():
    """Criar tabelas na base de dados"""
    with app.app_context():
        try:
            db.create_all()
            print("Base de dados inicializada!")
        except Exception as e:
            print(f"Aviso: Não foi possível inicializar BD: {e}")


# Inicializar BD automaticamente no primeiro request
@app.before_request
def ensure_db_initialized():
    """Garantir que as tabelas existem antes do primeiro request"""
    if not hasattr(app, '_db_initialized'):
        try:
            # Testar conexão
            db.session.execute(db.text('SELECT 1'))
            db.session.commit()
        except Exception:
            # Se falhar, tentar criar tabelas
            try:
                db.create_all()
            except Exception as e:
                print(f"Aviso BD: {e}")
        app._db_initialized = True


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
