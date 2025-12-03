# SeniorCare - Documentação Técnica

## 📋 Informação do Projeto

| Item | Valor |
|------|-------|
| **Nome** | SeniorCare - AI Caregiver Companion |
| **Tipo** | Mobile-only PWA |
| **Repositório** | https://github.com/mpcbarbosa/SeniorCare |
| **URL Produção** | https://seniorcare-57e1.onrender.com |
| **Desenvolvedor** | Miguel Barbosa |

---

## 🖥️ Ambiente de Desenvolvimento

### Localização Local
```
C:\Users\mcast\Documents\AIProjects\AISeniorCare
```

### Comandos PowerShell Úteis

```powershell
# Navegar para o projeto
cd C:\Users\mcast\Documents\AIProjects\AISeniorCare

# Criar ambiente virtual (primeira vez)
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate

# Instalar dependências
pip install -r requirements.txt

# Executar localmente
python app.py

# Git - verificar estado
git status

# Git - commit e push
git add .
git commit -m "mensagem"
git push origin master
```

---

## ☁️ Ambiente Render

### Web Service

| Configuração | Valor |
|--------------|-------|
| **Nome** | SeniorCare |
| **Service ID** | srv-d4o65uk9c44c73dilv8g |
| **URL** | https://seniorcare-57e1.onrender.com |
| **Runtime** | Python 3 |
| **Instance** | Starter (0.5 CPU, 512 MB) |
| **Region** | Oregon (US West) |
| **Branch** | master |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Auto-Deploy** | On Commit |
| **Health Check** | /healthz |

### Base de Dados PostgreSQL

| Configuração | Valor |
|--------------|-------|
| **Nome** | SeniorCareDB |
| **Service ID** | dpg-d4o4cp0gjchc73cd6ql0-a |
| **Versão** | PostgreSQL 18 |
| **Instance** | Basic-256mb (0.1 CPU, 256 MB RAM, 15 GB Storage) |
| **Region** | Oregon (US West) |
| **Database** | seniorcaredb |
| **Username** | seniorcaredb_user |
| **Hostname (interno)** | dpg-d4o4cp0gjchc73cd6ql0-a |
| **Port** | 5432 |

### Variáveis de Ambiente (Render)

```
DATABASE_URL=postgresql://seniorcaredb_user:YYY9C4UDYkoWNTUY0iCWyjAs87WdEINA@dpg-d4o4cp0gjchc73cd6ql0-a/seniorcaredb
SECRET_KEY=<gerar-chave-segura>
```

**Nota:** A Internal Database URL usa o hostname interno `dpg-d4o4cp0gjchc73cd6ql0-a` que só funciona dentro da rede do Render.

---

## 🏗️ Stack Tecnológico

### Backend
- **Framework:** Flask 3.0
- **ORM:** SQLAlchemy + Flask-SQLAlchemy
- **Migrações:** Flask-Migrate
- **Autenticação:** JWT (PyJWT)
- **CORS:** Flask-CORS
- **Server:** Gunicorn
- **Database:** PostgreSQL

### Frontend
- **Tipo:** PWA (Progressive Web App)
- **Framework:** Vanilla JS com React inline (via CDN)
- **CSS:** Custom CSS com variáveis CSS
- **Fonts:** Google Fonts (Nunito)
- **Offline:** Service Worker

### Infraestrutura
- **Hosting:** Render.com
- **Database:** Render PostgreSQL
- **CI/CD:** Auto-deploy via GitHub

---

## 📁 Estrutura do Projeto

```
SeniorCare/
├── app.py                 # Aplicação Flask principal
│                          # - Modelos SQLAlchemy
│                          # - Rotas API
│                          # - Autenticação JWT
│
├── requirements.txt       # Dependências Python
│
├── templates/
│   └── index.html         # Frontend PWA completo
│                          # - HTML estrutura
│                          # - CSS inline
│                          # - JavaScript/React inline
│
├── static/
│   ├── manifest.json      # Configuração PWA
│   ├── sw.js             # Service Worker
│   └── icons/
│       └── icon.svg      # Ícone da aplicação
│
├── migrations/
│   └── versions/         # Migrações da BD
│
├── .env.example          # Template variáveis ambiente
├── .gitignore            # Ficheiros ignorados pelo Git
├── README.md             # Documentação geral
└── DOCUMENTATION.md      # Esta documentação técnica
```

---

## 🗃️ Modelos da Base de Dados

### User (Utilizador/Idoso)
```python
- id: Integer (PK)
- name: String(100)
- phone: String(20) UNIQUE
- pin: String(256) - hash do PIN
- created_at: DateTime
- last_active: DateTime
- wake_time: Time
- sleep_time: Time
- language: String(10)
```

### Caregiver (Cuidador/Familiar)
```python
- id: Integer (PK)
- email: String(120) UNIQUE
- password_hash: String(256)
- name: String(100)
- phone: String(20)
- role: String(20) - family/professional/admin
- created_at: DateTime
```

### Medication (Medicamento)
```python
- id: Integer (PK)
- user_id: Integer (FK → users)
- name: String(100)
- dosage: String(50)
- instructions: Text
- icon: String(10)
- is_active: Boolean
- created_at: DateTime
```

### MedicationSchedule (Horário)
```python
- id: Integer (PK)
- medication_id: Integer (FK → medications)
- time: Time
- days_of_week: String(20) - "0123456"
```

### MedicationLog (Registo)
```python
- id: Integer (PK)
- medication_id: Integer (FK)
- schedule_id: Integer (FK)
- scheduled_time: DateTime
- taken_at: DateTime
- status: String(20) - pending/taken/skipped/late
- notes: Text
```

### Contact (Contacto)
```python
- id: Integer (PK)
- user_id: Integer (FK)
- name: String(100)
- phone: String(20)
- relationship: String(50)
- avatar: String(10)
- is_emergency: Boolean
- priority: Integer
```

### Activity (Atividade)
```python
- id: Integer (PK)
- user_id: Integer (FK)
- title: String(100)
- description: Text
- time: Time
- icon: String(10)
- category: String(50)
- is_recurring: Boolean
- days_of_week: String(20)
```

### Alert (Alerta)
```python
- id: Integer (PK)
- user_id: Integer (FK)
- type: String(50) - emergency/medication_missed/inactivity/fall/mood
- severity: String(20) - low/medium/high/critical
- message: Text
- created_at: DateTime
- resolved_at: DateTime
- resolved_by: Integer (FK → caregivers)
```

### MoodLog (Humor)
```python
- id: Integer (PK)
- user_id: Integer (FK)
- mood: String(20) - happy/neutral/sad/anxious/tired
- energy_level: Integer (1-5)
- notes: Text
- created_at: DateTime
```

### ChatMessage (Mensagem)
```python
- id: Integer (PK)
- user_id: Integer (FK)
- role: String(20) - user/assistant
- content: Text
- created_at: DateTime
```

---

## 🔌 API Endpoints

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/auth/register` | Registar utilizador |
| POST | `/api/auth/login` | Login com PIN/telefone |

### Utilizador
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/user/profile` | Obter perfil |
| POST | `/api/user/activity` | Heartbeat (atualizar última atividade) |

### Medicação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/medications` | Listar todos os medicamentos |
| POST | `/api/medications` | Adicionar medicamento |
| GET | `/api/medications/today` | Medicação de hoje com estado |
| POST | `/api/medications/<id>/take` | Marcar como tomado |

### Contactos
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/contacts` | Listar contactos |
| POST | `/api/contacts` | Adicionar contacto |

### Atividades
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/activities` | Listar atividades de hoje |
| POST | `/api/activities` | Adicionar atividade |

### Alertas
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/alerts` | Listar alertas recentes |
| POST | `/api/alerts/emergency` | Criar alerta de emergência |

### Humor
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/mood/recent` | Registos recentes |
| POST | `/api/mood` | Registar estado emocional |

### Chat
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/chat/messages` | Histórico de mensagens |
| POST | `/api/chat/send` | Enviar mensagem |

### Sistema
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/healthz` | Health check para Render |
| GET | `/manifest.json` | PWA manifest |
| GET | `/sw.js` | Service Worker |

---

## 🎨 Design System

### Cores
```css
--primary: #2E7D32        /* Verde principal */
--primary-light: #4CAF50  /* Verde claro */
--primary-dark: #1B5E20   /* Verde escuro */
--emergency: #C62828      /* Vermelho emergência */
--emergency-light: #EF5350
--family: #1565C0         /* Azul família */
--family-light: #42A5F5
--medication: #F57C00     /* Laranja medicação */
--medication-light: #FFB74D
--companion: #7B1FA2      /* Roxo conversa */
--companion-light: #BA68C8
--background: #FAFAFA
--text-primary: #212121
--text-secondary: #616161
```

### Tipografia
- **Font:** Nunito (Google Fonts)
- **Tamanhos:** 16px-42px
- **Pesos:** 400, 600, 700, 800

### Componentes
- **Botões grandes:** min 140px altura
- **Border radius:** 16px-32px
- **Sombras:** 0 4px 20px rgba(0,0,0,0.12)

---

## 📱 PWA Features

### Manifest
- Nome: "SeniorCare - Companheiro de Cuidado"
- Display: standalone
- Orientação: portrait
- Theme color: #2E7D32

### Service Worker
- Cache de assets estáticos
- Network-first para API
- Suporte offline
- Background sync para ações offline
- Push notifications (preparado)

### Instalação
1. Abrir URL no browser mobile
2. "Adicionar ao ecrã inicial" (iOS) ou "Instalar" (Android)

---

## 🚀 Roadmap

### MVP (Fase 1) ✅
- [x] Interface mobile-first para idosos
- [x] Gestão de medicação
- [x] Contactos de família
- [x] Botão de emergência
- [x] Rotina diária
- [x] Chat básico
- [x] PWA com offline

### Fase 2 (Em Desenvolvimento)
- [ ] Integração Claude AI para chat inteligente
- [ ] Notificações push
- [ ] Alertas WhatsApp/SMS para família
- [ ] Painel do cuidador (web)

### Fase 3 (Planeado)
- [ ] Reconhecimento de voz
- [ ] Deteção de inatividade
- [ ] Integração sensores IoT
- [ ] Videochamadas

---

## 🔧 Troubleshooting

### Erro de conexão à BD
```
Verificar DATABASE_URL no Render Environment
Usar Internal URL (não External) para conexões internas
```

### Deploy falha
```
Verificar requirements.txt
Verificar logs no Render Dashboard
Confirmar que gunicorn está nas dependências
```

### PWA não instala
```
Verificar HTTPS (obrigatório)
Verificar manifest.json
Verificar service worker registado
```

---

*Última atualização: Dezembro 2024*
