# 🐾 Smart Pet Care Chatbot

An intelligent, AI-powered chatbot for pet care advice with voice input/output capabilities. Built with Flask, Python, and modern web technologies.

## ✨ Features

- 🤖 **AI-Powered Responses** - Uses Gemini AI (or OpenAI/Anthropic) for unlimited, intelligent pet care advice
- 🎤 **Voice Input** - Speak your questions using Web Speech API
- 🔊 **Voice Output** - Text-to-speech using ElevenLabs
- 🎨 **Beautiful UI** - Modern, responsive design with gradient backgrounds
- 📱 **Mobile-Friendly** - Works perfectly on all devices
- 🐕 **Comprehensive Pet Data** - Built-in knowledge base for dogs, cats, and more

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API Keys (optional):
  - OpenAI API Key (for GPT models)
  - Google Gemini API Key (free tier available)
  - ElevenLabs API Key (for voice output)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pet_chatbot.git
   cd pet_chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys:**
   
   Edit `config.py` and add your API keys:
   ```python
   OPENAI_API_KEY = "your-key-here"
   GEMINI_API_KEY = "your-key-here"
   ELEVENLABS_API_KEY = "your-key-here"
   ```
   
   Or use environment variables:
   ```bash
   export OPENAI_API_KEY="your-key"
   export GEMINI_API_KEY="your-key"
   export ELEVENLABS_API_KEY="your-key"
   ```

4. **Run the server:**
   ```bash
   python server.py
   ```

5. **Open in browser:**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
pet_chatbot/
├── server.py              # Flask server
├── pet_bot_main.py        # Main chatbot logic
├── ai_provider.py         # AI API integration
├── pet_data_loader.py     # Pet care data management
├── config.py              # Configuration and API keys
├── requirements.txt       # Python dependencies
├── static/
│   ├── index.html         # Frontend UI
│   └── script.js          # Client-side JavaScript
└── data/                  # Pet care data files
```

## 🎯 Usage

1. **Text Input**: Type your question in the input box and press Send or Enter
2. **Voice Input**: Click the 🎤 Mic button to speak your question
3. **Voice Output**: Responses are automatically read aloud (if ElevenLabs is configured)

## 🔧 Configuration

### AI Provider Selection

Edit `config.py` to choose your AI provider:

```python
AI_PROVIDER = "gemini"  # Options: "openai", "anthropic", "gemini", "none"
```

### Models

- **OpenAI**: `gpt-4o-mini`, `gpt-4`, `gpt-3.5-turbo`
- **Anthropic**: `claude-3-5-sonnet-20241022`, `claude-3-haiku-20240307`
- **Gemini**: `gemini-2.0-flash`, `gemini-2.5-flash`

## 📚 Documentation

- [AI Setup Guide](AI_SETUP.md) - Detailed AI API configuration
- [Production Deployment](PRODUCTION_DEPLOYMENT.md) - Deploy to production
- [VS Code Instructions](VS_CODE_RUN_INSTRUCTIONS.md) - Development setup
- [Quick Start Guide](QUICK_START.md) - Quick reference

## 🛠️ Development

### Run Development Server

```bash
python server.py
```

### Run Production Server

```bash
python run_production.py
```

## 🚢 Deployment

### Heroku

1. Install Heroku CLI
2. Create `Procfile` (already included)
3. Deploy:
   ```bash
   heroku create
   git push heroku main
   ```

### Docker

```bash
docker build -t pet-chatbot .
docker run -p 5000:5000 pet-chatbot
```

See [PRODUCTION_DEPLOYMENT.md](PRODUCTION_DEPLOYMENT.md) for more options.

## 🔒 Security

- ⚠️ **Never commit API keys to Git**
- Use environment variables for production
- The `.gitignore` file excludes sensitive files

## 📝 Features in Detail

- **AI Integration**: Seamlessly switches between AI providers
- **Fallback Mode**: Works without AI using built-in pet data
- **Emergency Detection**: Automatically flags urgent pet situations
- **Emotion Detection**: Adjusts voice tone based on response context
- **Markdown Cleaning**: Automatically removes formatting for clean display

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [ElevenLabs](https://elevenlabs.io/) - Voice synthesis
- [OpenAI](https://openai.com/) - GPT models
- [Google Gemini](https://gemini.google.com/) - AI models
- [Anthropic](https://www.anthropic.com/) - Claude models

## 📧 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

Made with ❤️ for pet lovers everywhere 🐾

