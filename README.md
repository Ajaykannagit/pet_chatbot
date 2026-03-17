# 🐾 Smart Pet Care Chatbot

<div align="center">

![Pet Care Chatbot](https://img.shields.io/badge/Pet-Care%20Chatbot-blue?style=for-the-badge&logo=pets)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3+-red?style=for-the-badge&logo=flask)
![AI Powered](https://img.shields.io/badge/AI-Powered-orange?style=for-the-badge&logo=openai)

**An intelligent, AI-powered chatbot for pet care advice with voice input/output capabilities**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Deployment](#-deployment)

</div>

---

## ✨ Features

### 🤖 AI-Powered Intelligence
- **Multiple AI Providers**: Supports OpenAI GPT, Google Gemini, and Anthropic Claude
- **Intelligent Responses**: Context-aware, comprehensive pet care advice
- **Seamless Fallback**: Automatically falls back to built-in knowledge if APIs unavailable

### 🎤 Voice Capabilities
- **Voice Input**: Speak your questions using Web Speech API
- **Voice Output**: Text-to-speech using ElevenLabs (with emotional tones)
- **Natural Interaction**: Hands-free pet care consultations

### 🎨 Modern UI/UX
- **Beautiful Design**: Gradient backgrounds, smooth animations, modern interface
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile
- **Real-time Updates**: Instant responses with typing indicators

### 📚 Comprehensive Pet Knowledge
- **Multi-Pet Support**: Dogs, cats, birds, rabbits, fish, and more
- **Emergency Detection**: Automatically flags urgent pet situations
- **Expert Advice**: Food, vaccines, health, behavior, training guidance.

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **API Keys** (Optional - works with fallback mode):
  - [OpenAI API Key](https://platform.openai.com/api-keys)
  - [Google Gemini API Key](https://makersuite.google.com/app/apikey) (Free tier available)
  - [ElevenLabs API Key](https://elevenlabs.io/) (For voice output)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ajaykannagit/pet_chatbot.git
   cd pet_chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**

   Edit `config.py`:
   ```python
   AI_PROVIDER = "gemini"  # or "openai", "anthropic"
   
   OPENAI_API_KEY = "your-openai-key-here"
   GEMINI_API_KEY = "your-gemini-key-here"
   ELEVENLABS_API_KEY = "your-elevenlabs-key-here"
   ```
   
   Or use environment variables:
   ```bash
   export OPENAI_API_KEY="your-key"
   export GEMINI_API_KEY="your-key"
   export ELEVENLABS_API_KEY="your-key"
   ```

4. **Run the server**
   ```bash
   python server.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## 📖 Usage

### Text Input
Type your question in the input box and press **Send** or **Enter**

### Voice Input
Click the **🎤 Mic** button to speak your question (requires browser microphone permission)

### Example Questions
- "How do I train my dog?"
- "What should I feed my cat?"
- "My dog is vomiting, what should I do?"
- "Tell me about cat vaccinations"
- "How to tame a puppy?"

---

## 🏗️ Project Structure

```
pet_chatbot/
├── server.py              # Flask web server
├── pet_bot_main.py        # Main chatbot logic
├── ai_provider.py         # AI API integration (OpenAI, Gemini, Claude)
├── pet_data_loader.py     # Pet care knowledge base manager
├── config.py              # Configuration and API keys
├── run_production.py      # Production server runner
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── static/
│   ├── index.html        # Frontend UI
│   └── script.js         # Client-side JavaScript
├── data/                 # Local pet care data files
│   ├── dogs.json
│   ├── cats.json
│   └── emergency.json
└── docs/                 # Documentation files
    ├── AI_SETUP.md
    ├── PRODUCTION_DEPLOYMENT.md
    └── VS_CODE_RUN_INSTRUCTIONS.md
```

---

## 🔧 Configuration

### AI Provider Selection

Edit `config.py`:

```python
# Choose your AI provider
AI_PROVIDER = "gemini"  # Options: "openai", "anthropic", "gemini", "none"
```

### Available Models

| Provider | Models |
|----------|--------|
| **OpenAI** | `gpt-4o-mini`, `gpt-4`, `gpt-3.5-turbo` |
| **Gemini** | `gemini-2.0-flash`, `gemini-2.5-flash` |
| **Anthropic** | `claude-3-5-sonnet`, `claude-3-haiku` |

---

## 🎯 Features in Detail

### AI Integration
- Automatically tries AI first for all queries
- Falls back gracefully if API unavailable
- Supports context enhancement from pet data
- Markdown cleaning for clean responses

### Emergency Detection
- Recognizes urgent keywords (bleeding, poison, not breathing, etc.)
- Immediately advises contacting veterinarian
- Emergency emotion tone for voice output

### Smart Fallback
- Uses built-in pet knowledge base if AI fails
- Works offline with local data
- No errors shown to users

### Voice Features
- ElevenLabs TTS with emotional tones
- Browser SpeechSynthesis fallback
- Real-time listening indicators

---

## 📚 Documentation

Comprehensive guides available in the repository:

- **[AI Setup Guide](AI_SETUP.md)** - Detailed AI API configuration
- **[Production Deployment](PRODUCTION_DEPLOYMENT.md)** - Deploy to production servers
- **[VS Code Instructions](VS_CODE_RUN_INSTRUCTIONS.md)** - Development setup guide
- **[Quick Start Guide](QUICK_START.md)** - Quick reference

---

## 🛠️ Development

### Development Server

```bash
python server.py
```

Runs on `http://localhost:5000` with hot-reload enabled.

### Production Server

```bash
python run_production.py
```

Uses Waitress WSGI server for production-ready deployment.

---

## 🚢 Deployment

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Create app: `heroku create your-app-name`
3. Set environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=your-key
   heroku config:set GEMINI_API_KEY=your-key
   ```
4. Deploy: `git push heroku main`

### Docker

```bash
docker build -t pet-chatbot .
docker run -p 5000:5000 -e GEMINI_API_KEY=your-key pet-chatbot
```

### PythonAnywhere / DigitalOcean / AWS

See [PRODUCTION_DEPLOYMENT.md](PRODUCTION_DEPLOYMENT.md) for detailed instructions.

---

## 🔒 Security

- ⚠️ **Never commit API keys to Git**
- Use environment variables for production
- `.gitignore` excludes sensitive files
- Placeholder keys in repository are safe

---

## 🌟 Key Technologies

- **Backend**: Flask, Python
- **AI**: OpenAI GPT, Google Gemini, Anthropic Claude
- **Voice**: ElevenLabs TTS, Web Speech API
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Deployment**: Waitress, Gunicorn, Docker

---

## 📊 Features Comparison

| Feature | With AI | Fallback Mode |
|---------|---------|---------------|
| Response Quality | ⭐⭐⭐⭐⭐ Intelligent | ⭐⭐⭐ Basic |
| Response Variety | Unlimited | Limited |
| Internet Required | ✅ Yes | ❌ No |
| Setup Required | API Keys | None |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [ElevenLabs](https://elevenlabs.io/) - Voice synthesis
- [OpenAI](https://openai.com/) - GPT models
- [Google Gemini](https://gemini.google.com/) - AI models
- [Anthropic](https://www.anthropic.com/) - Claude models

---

## 📧 Support & Contact

- **GitHub Issues**: [Report a bug](https://github.com/Ajaykannagit/pet_chatbot/issues)
- **Discussions**: [Ask questions](https://github.com/Ajaykannagit/pet_chatbot/discussions)

---

<div align="center">

**Made with ❤️ for pet lovers everywhere 🐾**

⭐ Star this repo if you find it helpful!

[⬆ Back to Top](#-smart-pet-care-chatbot)

</div>
