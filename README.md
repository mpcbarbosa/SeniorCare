# SeniorCare 💚

**Companheiro de Cuidado para Idosos** - Uma aplicação mobile PWA que proporciona autonomia, segurança e companhia a pessoas idosas.

## 🎯 Funcionalidades

### MVP (Fase 1)
- ✅ Interface ultra-simples para idosos
- ✅ Gestão de medicação com lembretes
- ✅ Contactos de família com chamada rápida
- ✅ Botão de emergência sempre visível
- ✅ Rotina diária
- ✅ Conversa/Companhia
- ✅ PWA (instalável no telemóvel)
- ✅ Funciona offline

### Próximas Fases
- 🔜 Integração com Claude AI para conversas inteligentes
- 🔜 Notificações push para lembretes
- 🔜 Alertas para familiares via WhatsApp/SMS
- 🔜 Painel do cuidador
- 🔜 Deteção de inatividade
- 🔜 Reconhecimento de voz

## 🚀 Deploy no Render

### Pré-requisitos
- Conta no [Render](https://render.com)
- Repositório GitHub

### Configuração

1. **Web Service**
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

2. **Base de Dados PostgreSQL**
   - Criar PostgreSQL no Render
   - Copiar Internal Database URL

3. **Variáveis de Ambiente** (no Render)
   ```
   DATABASE_URL=<Internal Database URL>
   SECRET_KEY=<gerar chave segura>
   ```

### Deploy
O Render faz deploy automático a cada push no branch `master`.

## 💻 Desenvolvimento Local

```bash
# Clonar repositório
git clone https://github.com/mpcbarbosa/SeniorCare.git
cd SeniorCare

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis
cp .env.example .env
# Editar .env com as suas configurações

# Inicializar base de dados
python -c "from app import init_db; init_db()"

# Executar
python app.py
```

Aceder em: http://localhost:5000

## 📱 Instalar no Telemóvel

1. Aceder à URL da aplicação no browser do telemóvel
2. Tocar em "Adicionar ao ecrã inicial" (iOS Safari) ou "Instalar app" (Android Chrome)
3. A app fica disponível como uma aplicação nativa

## 🏗 Estrutura do Projeto

```
SeniorCare/
├── app.py              # Aplicação Flask principal
├── requirements.txt    # Dependências Python
├── templates/
│   └── index.html      # Frontend PWA (React inline)
├── static/
│   ├── manifest.json   # Configuração PWA
│   ├── sw.js          # Service Worker
│   └── icons/         # Ícones da app
├── migrations/        # Migrações da BD
├── .env.example       # Exemplo de variáveis
└── README.md
```

## 🔌 API Endpoints

### Autenticação
- `POST /api/auth/register` - Registar utilizador
- `POST /api/auth/login` - Login

### Utilizador
- `GET /api/user/profile` - Obter perfil
- `POST /api/user/activity` - Heartbeat

### Medicação
- `GET /api/medications` - Listar medicamentos
- `GET /api/medications/today` - Medicação de hoje
- `POST /api/medications/<id>/take` - Marcar como tomado

### Contactos
- `GET /api/contacts` - Listar contactos
- `POST /api/contacts` - Adicionar contacto

### Alertas
- `POST /api/alerts/emergency` - Criar alerta de emergência

### Chat
- `GET /api/chat/messages` - Histórico
- `POST /api/chat/send` - Enviar mensagem

## 🎨 Design

A interface foi desenhada com foco em:
- **Botões muito grandes** (mínimo 140px)
- **Texto legível** (20-42px)
- **Alto contraste** de cores
- **Poucos elementos** por ecrã
- **Ícones intuitivos** (emojis)
- **Zero curva de aprendizagem**

## 📄 Licença

MIT License - Uso livre para fins não comerciais.

## 👥 Contacto

Desenvolvido por Miguel Barbosa
