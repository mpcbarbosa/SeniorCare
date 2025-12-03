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
        database_url = database_url.replace('postgres://', 'postgresql+psycopg://', 1)
    elif database_url.startswith('postgresql://'):
        database_url = database_url.replace('postgresql://', 'postgresql+psycopg://', 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    print(f"Database: PostgreSQL configurado")
else:
    # Fallback para SQLite local
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'seniorcare.db')
    print(f"Database: SQLite (local)")

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


class Appointment(db.Model):
    """Consultas médicas"""
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    doctor_name = db.Column(db.String(100))
    specialty = db.Column(db.String(100))
    location = db.Column(db.String(200))
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.Text)
    reminder_hours_before = db.Column(db.Integer, default=24)
    status = db.Column(db.String(20), default='scheduled')  # scheduled, completed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('appointments', lazy='dynamic'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'doctor_name': self.doctor_name,
            'specialty': self.specialty,
            'location': self.location,
            'appointment_date': self.appointment_date.isoformat() if self.appointment_date else None,
            'appointment_time': self.appointment_time.strftime('%H:%M') if self.appointment_time else None,
            'notes': self.notes,
            'reminder_hours_before': self.reminder_hours_before,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class HealthReading(db.Model):
    """Medições de saúde (tensão, glicemia, peso, etc.)"""
    __tablename__ = 'health_readings'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reading_type = db.Column(db.String(50), nullable=False)  # blood_pressure, glucose, weight, temperature, heart_rate, oxygen
    value_primary = db.Column(db.Float, nullable=False)  # Valor principal (sistólica, glicemia, peso, etc.)
    value_secondary = db.Column(db.Float)  # Valor secundário (diastólica para tensão)
    unit = db.Column(db.String(20))  # mmHg, mg/dL, kg, °C, bpm, %
    notes = db.Column(db.Text)
    measured_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('health_readings', lazy='dynamic'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'reading_type': self.reading_type,
            'value_primary': self.value_primary,
            'value_secondary': self.value_secondary,
            'unit': self.unit,
            'notes': self.notes,
            'measured_at': self.measured_at.isoformat() if self.measured_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class MedicationAlertConfig(db.Model):
    """Configuração de alertas de medicação"""
    __tablename__ = 'medication_alert_configs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'))  # Null = configuração global
    
    # Tempos de alerta (em minutos)
    first_alert_delay = db.Column(db.Integer, default=15)  # Primeiro alerta após X minutos
    second_alert_delay = db.Column(db.Integer, default=30)  # Segundo alerta
    escalation_delay = db.Column(db.Integer, default=60)  # Escalar para cuidadores após X minutos
    
    # Quem notificar
    notify_user_sound = db.Column(db.Boolean, default=True)
    notify_user_vibration = db.Column(db.Boolean, default=True)
    notify_caregivers = db.Column(db.Boolean, default=True)
    notify_via_sms = db.Column(db.Boolean, default=False)
    notify_via_whatsapp = db.Column(db.Boolean, default=True)
    notify_via_push = db.Column(db.Boolean, default=True)
    
    # Cuidadores específicos a notificar (lista de IDs separados por vírgula)
    caregiver_ids = db.Column(db.String(200))
    
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('alert_configs', lazy='dynamic'))
    medication = db.relationship('Medication', backref=db.backref('alert_config', uselist=False))
    
    def to_dict(self):
        return {
            'id': self.id,
            'medication_id': self.medication_id,
            'first_alert_delay': self.first_alert_delay,
            'second_alert_delay': self.second_alert_delay,
            'escalation_delay': self.escalation_delay,
            'notify_user_sound': self.notify_user_sound,
            'notify_user_vibration': self.notify_user_vibration,
            'notify_caregivers': self.notify_caregivers,
            'notify_via_sms': self.notify_via_sms,
            'notify_via_whatsapp': self.notify_via_whatsapp,
            'notify_via_push': self.notify_via_push,
            'caregiver_ids': self.caregiver_ids.split(',') if self.caregiver_ids else [],
            'is_active': self.is_active,
        }


class NotificationLog(db.Model):
    """Log de notificações enviadas"""
    __tablename__ = 'notification_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    notification_type = db.Column(db.String(50), nullable=False)  # medication_reminder, appointment_reminder, health_alert, emergency
    reference_type = db.Column(db.String(50))  # medication, appointment, health_reading
    reference_id = db.Column(db.Integer)
    message = db.Column(db.Text, nullable=False)
    channel = db.Column(db.String(20))  # push, sms, whatsapp, email
    sent_to = db.Column(db.String(200))  # user, caregiver_id, phone_number
    status = db.Column(db.String(20), default='pending')  # pending, sent, delivered, failed
    sent_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('notifications', lazy='dynamic'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'notification_type': self.notification_type,
            'message': self.message,
            'channel': self.channel,
            'status': self.status,
            'sent_at': self.sent_at.isoformat() if self.sent_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


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


# ==================== CONSULTAS ====================

@app.route('/api/appointments', methods=['GET'])
@token_required
def get_appointments(current_user):
    """Listar consultas"""
    status = request.args.get('status', 'scheduled')
    query = Appointment.query.filter_by(user_id=current_user.id)
    
    if status != 'all':
        query = query.filter_by(status=status)
    
    appointments = query.order_by(Appointment.appointment_date, Appointment.appointment_time).all()
    return jsonify([a.to_dict() for a in appointments])


@app.route('/api/appointments', methods=['POST'])
@token_required
def create_appointment(current_user):
    """Criar nova consulta"""
    data = request.get_json()
    
    appointment = Appointment(
        user_id=current_user.id,
        title=data['title'],
        doctor_name=data.get('doctor_name'),
        specialty=data.get('specialty'),
        location=data.get('location'),
        appointment_date=datetime.strptime(data['appointment_date'], '%Y-%m-%d').date(),
        appointment_time=datetime.strptime(data['appointment_time'], '%H:%M').time(),
        notes=data.get('notes'),
        reminder_hours_before=data.get('reminder_hours_before', 24),
    )
    db.session.add(appointment)
    db.session.commit()
    
    return jsonify(appointment.to_dict()), 201


@app.route('/api/appointments/<int:appointment_id>', methods=['PUT'])
@token_required
def update_appointment(current_user, appointment_id):
    """Atualizar consulta"""
    appointment = Appointment.query.filter_by(id=appointment_id, user_id=current_user.id).first_or_404()
    data = request.get_json()
    
    if 'title' in data:
        appointment.title = data['title']
    if 'doctor_name' in data:
        appointment.doctor_name = data['doctor_name']
    if 'specialty' in data:
        appointment.specialty = data['specialty']
    if 'location' in data:
        appointment.location = data['location']
    if 'appointment_date' in data:
        appointment.appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d').date()
    if 'appointment_time' in data:
        appointment.appointment_time = datetime.strptime(data['appointment_time'], '%H:%M').time()
    if 'notes' in data:
        appointment.notes = data['notes']
    if 'status' in data:
        appointment.status = data['status']
    if 'reminder_hours_before' in data:
        appointment.reminder_hours_before = data['reminder_hours_before']
    
    db.session.commit()
    return jsonify(appointment.to_dict())


@app.route('/api/appointments/<int:appointment_id>', methods=['DELETE'])
@token_required
def delete_appointment(current_user, appointment_id):
    """Eliminar consulta"""
    appointment = Appointment.query.filter_by(id=appointment_id, user_id=current_user.id).first_or_404()
    db.session.delete(appointment)
    db.session.commit()
    return jsonify({'message': 'Consulta eliminada'})


@app.route('/api/appointments/upcoming', methods=['GET'])
@token_required
def get_upcoming_appointments(current_user):
    """Obter próximas consultas"""
    today = datetime.utcnow().date()
    appointments = Appointment.query.filter(
        Appointment.user_id == current_user.id,
        Appointment.status == 'scheduled',
        Appointment.appointment_date >= today
    ).order_by(Appointment.appointment_date, Appointment.appointment_time).limit(5).all()
    return jsonify([a.to_dict() for a in appointments])


# ==================== MEDIÇÕES DE SAÚDE ====================

@app.route('/api/health/readings', methods=['GET'])
@token_required
def get_health_readings(current_user):
    """Listar medições de saúde"""
    reading_type = request.args.get('type')
    limit = request.args.get('limit', 50, type=int)
    
    query = HealthReading.query.filter_by(user_id=current_user.id)
    
    if reading_type:
        query = query.filter_by(reading_type=reading_type)
    
    readings = query.order_by(HealthReading.measured_at.desc()).limit(limit).all()
    return jsonify([r.to_dict() for r in readings])


@app.route('/api/health/readings', methods=['POST'])
@token_required
def create_health_reading(current_user):
    """Registar nova medição de saúde"""
    data = request.get_json()
    
    reading = HealthReading(
        user_id=current_user.id,
        reading_type=data['reading_type'],
        value_primary=data['value_primary'],
        value_secondary=data.get('value_secondary'),
        unit=data.get('unit'),
        notes=data.get('notes'),
        measured_at=datetime.strptime(data['measured_at'], '%Y-%m-%dT%H:%M') if data.get('measured_at') else datetime.utcnow(),
    )
    db.session.add(reading)
    db.session.commit()
    
    return jsonify(reading.to_dict()), 201


@app.route('/api/health/readings/<int:reading_id>', methods=['DELETE'])
@token_required
def delete_health_reading(current_user, reading_id):
    """Eliminar medição de saúde"""
    reading = HealthReading.query.filter_by(id=reading_id, user_id=current_user.id).first_or_404()
    db.session.delete(reading)
    db.session.commit()
    return jsonify({'message': 'Medição eliminada'})


@app.route('/api/health/readings/latest', methods=['GET'])
@token_required
def get_latest_readings(current_user):
    """Obter última medição de cada tipo"""
    types = ['blood_pressure', 'glucose', 'weight', 'temperature', 'heart_rate', 'oxygen']
    latest = {}
    
    for t in types:
        reading = HealthReading.query.filter_by(
            user_id=current_user.id,
            reading_type=t
        ).order_by(HealthReading.measured_at.desc()).first()
        
        if reading:
            latest[t] = reading.to_dict()
    
    return jsonify(latest)


@app.route('/api/health/readings/summary', methods=['GET'])
@token_required
def get_health_summary(current_user):
    """Obter resumo de saúde (médias, últimas medições)"""
    from sqlalchemy import func
    
    # Últimos 30 dias
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    summary = {}
    types = ['blood_pressure', 'glucose', 'weight', 'temperature', 'heart_rate', 'oxygen']
    
    for t in types:
        readings = HealthReading.query.filter(
            HealthReading.user_id == current_user.id,
            HealthReading.reading_type == t,
            HealthReading.measured_at >= thirty_days_ago
        ).all()
        
        if readings:
            values = [r.value_primary for r in readings]
            summary[t] = {
                'count': len(readings),
                'average': round(sum(values) / len(values), 1),
                'min': min(values),
                'max': max(values),
                'latest': readings[-1].to_dict() if readings else None,
            }
    
    return jsonify(summary)


# ==================== CONFIGURAÇÕES DE ALERTAS ====================

@app.route('/api/alerts/config', methods=['GET'])
@token_required
def get_alert_config(current_user):
    """Obter configuração de alertas"""
    # Configuração global (medication_id = null)
    config = MedicationAlertConfig.query.filter_by(
        user_id=current_user.id,
        medication_id=None
    ).first()
    
    if not config:
        # Criar configuração padrão
        config = MedicationAlertConfig(
            user_id=current_user.id,
            medication_id=None,
        )
        db.session.add(config)
        db.session.commit()
    
    return jsonify(config.to_dict())


@app.route('/api/alerts/config', methods=['PUT'])
@token_required
def update_alert_config(current_user):
    """Atualizar configuração de alertas"""
    data = request.get_json()
    medication_id = data.get('medication_id')
    
    config = MedicationAlertConfig.query.filter_by(
        user_id=current_user.id,
        medication_id=medication_id
    ).first()
    
    if not config:
        config = MedicationAlertConfig(
            user_id=current_user.id,
            medication_id=medication_id,
        )
        db.session.add(config)
    
    # Atualizar campos
    if 'first_alert_delay' in data:
        config.first_alert_delay = data['first_alert_delay']
    if 'second_alert_delay' in data:
        config.second_alert_delay = data['second_alert_delay']
    if 'escalation_delay' in data:
        config.escalation_delay = data['escalation_delay']
    if 'notify_user_sound' in data:
        config.notify_user_sound = data['notify_user_sound']
    if 'notify_user_vibration' in data:
        config.notify_user_vibration = data['notify_user_vibration']
    if 'notify_caregivers' in data:
        config.notify_caregivers = data['notify_caregivers']
    if 'notify_via_sms' in data:
        config.notify_via_sms = data['notify_via_sms']
    if 'notify_via_whatsapp' in data:
        config.notify_via_whatsapp = data['notify_via_whatsapp']
    if 'notify_via_push' in data:
        config.notify_via_push = data['notify_via_push']
    if 'caregiver_ids' in data:
        config.caregiver_ids = ','.join(str(x) for x in data['caregiver_ids']) if data['caregiver_ids'] else None
    if 'is_active' in data:
        config.is_active = data['is_active']
    
    db.session.commit()
    return jsonify(config.to_dict())


@app.route('/api/notifications/log', methods=['GET'])
@token_required
def get_notification_log(current_user):
    """Obter histórico de notificações"""
    limit = request.args.get('limit', 50, type=int)
    notifications = NotificationLog.query.filter_by(
        user_id=current_user.id
    ).order_by(NotificationLog.created_at.desc()).limit(limit).all()
    return jsonify([n.to_dict() for n in notifications])


# ==================== TIPOS DE MEDIÇÕES (para o frontend) ====================

@app.route('/api/health/types', methods=['GET'])
def get_health_reading_types():
    """Obter tipos de medições disponíveis"""
    types = [
        {
            'id': 'blood_pressure',
            'name': 'Tensão Arterial',
            'name_en': 'Blood Pressure',
            'icon': '❤️',
            'unit': 'mmHg',
            'has_secondary': True,
            'primary_label': 'Sistólica',
            'secondary_label': 'Diastólica',
            'normal_range': {'primary': [90, 120], 'secondary': [60, 80]},
        },
        {
            'id': 'glucose',
            'name': 'Glicemia',
            'name_en': 'Blood Glucose',
            'icon': '🩸',
            'unit': 'mg/dL',
            'has_secondary': False,
            'primary_label': 'Valor',
            'normal_range': {'primary': [70, 100]},
        },
        {
            'id': 'weight',
            'name': 'Peso',
            'name_en': 'Weight',
            'icon': '⚖️',
            'unit': 'kg',
            'has_secondary': False,
            'primary_label': 'Peso',
        },
        {
            'id': 'temperature',
            'name': 'Temperatura',
            'name_en': 'Temperature',
            'icon': '🌡️',
            'unit': '°C',
            'has_secondary': False,
            'primary_label': 'Temperatura',
            'normal_range': {'primary': [36, 37.5]},
        },
        {
            'id': 'heart_rate',
            'name': 'Frequência Cardíaca',
            'name_en': 'Heart Rate',
            'icon': '💓',
            'unit': 'bpm',
            'has_secondary': False,
            'primary_label': 'Batimentos',
            'normal_range': {'primary': [60, 100]},
        },
        {
            'id': 'oxygen',
            'name': 'Saturação de Oxigénio',
            'name_en': 'Oxygen Saturation',
            'icon': '💨',
            'unit': '%',
            'has_secondary': False,
            'primary_label': 'SpO2',
            'normal_range': {'primary': [95, 100]},
        },
    ]
    return jsonify(types)


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
