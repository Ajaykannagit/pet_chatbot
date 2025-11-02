# Quick Start Guide - Pet Chatbot

## ✅ Your Setup is Ready!

Your chatbot is configured with:
- ✅ **OpenAI API** - Enabled (gpt-4o-mini)
- ✅ **Gemini API** - Available as backup
- ✅ **ElevenLabs TTS** - Enabled for voice responses
- ✅ **Anthropic** - Disabled (as requested)

## 🚀 How to Run in VS Code

### Step 1: Open VS Code Terminal
1. Open VS Code
2. Press `` Ctrl + ` `` (backtick) to open terminal
3. OR go to: **Terminal** → **New Terminal**

### Step 2: Navigate to Project (if needed)
```powershell
cd c:\Users\user\Desktop\pet_chatbot
```

### Step 3: Install Dependencies (first time only)
```powershell
pip install -r requirements.txt
```

### Step 4: Start the Server
```powershell
python server.py
```

### Step 5: Open in Browser
- The server will show: `Running on http://0.0.0.0:5000`
- Open your browser and go to: **http://localhost:5000**

## 🎯 What You'll See

When the server starts:
```
[info] Initializing pet data...
[ai] OpenAI initialized with model: gpt-4o-mini
[bot] AI-enhanced mode enabled using openai
 * Running on http://0.0.0.0:5000
```

In your browser:
- 🐾 Smart Pet Care Chatbot interface
- Text input box
- Mic button (for voice input)
- Send button

## 🛑 How to Stop the Server

1. Click in the VS Code terminal window
2. Press `Ctrl+C`
3. Server stops gracefully

## 🔧 Troubleshooting

### Port 5000 Already in Use
```powershell
# Find and kill the process
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

### Module Not Found
```powershell
pip install -r requirements.txt
```

### AI Not Working
- Check that your OpenAI API key in `config.py` is correct
- The chatbot will still work with fallback responses

## 💡 Tips

- **Restart Server**: After changing `config.py`, restart the server (Ctrl+C, then run again)
- **View Logs**: Check the VS Code terminal for server output and errors
- **AI Responses**: With OpenAI enabled, you get unlimited, intelligent responses!
- **Voice**: Click the mic button to speak your questions

## 🎉 You're All Set!

Your chatbot now has:
- 🤖 AI-powered unlimited responses (OpenAI)
- 🎤 Voice input support
- 🔊 Voice output (ElevenLabs TTS)
- 📚 Smart fallback to pet data

Enjoy your enhanced pet care chatbot! 🐾

