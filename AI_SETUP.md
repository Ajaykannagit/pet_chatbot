# AI API Setup Guide

Your pet chatbot now supports multiple AI providers for enhanced, unlimited responses! 🚀

## Supported AI Providers

1. **OpenAI** (GPT-4, GPT-3.5) - Recommended for best results
2. **Anthropic** (Claude) - Great for detailed responses
3. **Google Gemini** - Free tier available

## Quick Setup

### Option 1: OpenAI (Recommended)

1. Get your API key from: https://platform.openai.com/api-keys
2. Set it as an environment variable:
   ```powershell
   $env:OPENAI_API_KEY = "sk-your-key-here"
   ```
   Or edit `config.py` and set:
   ```python
   OPENAI_API_KEY = "sk-your-key-here"
   ```

3. Set provider to OpenAI (default):
   ```powershell
   $env:AI_PROVIDER = "openai"
   ```

### Option 2: Anthropic (Claude)

1. Get your API key from: https://console.anthropic.com/
2. Set it:
   ```powershell
   $env:ANTHROPIC_API_KEY = "sk-ant-your-key-here"
   $env:AI_PROVIDER = "anthropic"
   ```

### Option 3: Google Gemini (Free Tier Available)

1. Get your API key from: https://makersuite.google.com/app/apikey
2. Set it:
   ```powershell
   $env:GEMINI_API_KEY = "your-key-here"
   $env:AI_PROVIDER = "gemini"
   ```

## Installation

Install the required packages:

```powershell
pip install -r requirements.txt
```

This will install:
- `openai` (for OpenAI)
- `anthropic` (for Claude)
- `google-generativeai` (for Gemini)

## Configuration

Edit `config.py` to set your API keys and preferred provider:

```python
# Choose provider: "openai", "anthropic", "gemini", or "none" for fallback
AI_PROVIDER = "openai"

# Set your API keys
OPENAI_API_KEY = "sk-your-key-here"
# or
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
# or
GEMINI_API_KEY = "your-key-here"
```

## How It Works

1. **With AI Enabled**: The chatbot uses AI to generate comprehensive, context-aware responses about any pet care topic
2. **Fallback Mode**: If no API key is set, it uses the built-in pet data (limited responses)
3. **Hybrid Approach**: The AI receives context from your pet data for even better responses

## Testing

After setting up, restart your server:

```powershell
python server.py
```

You should see:
```
[ai] OpenAI initialized with model: gpt-4o-mini
[bot] AI-enhanced mode enabled using openai
```

Then visit: http://localhost:5000

## Troubleshooting

- **"AI provider disabled"**: Check that `AI_PROVIDER` is set correctly and not "none"
- **"API key not set"**: Make sure your API key is correct and matches the provider
- **Import errors**: Run `pip install -r requirements.txt` to install missing packages
- **API errors**: Check your API key is valid and you have credits/quota

## Cost Considerations

- **OpenAI GPT-4o-mini**: Very affordable (~$0.15 per 1M input tokens)
- **Anthropic Claude**: Competitive pricing
- **Google Gemini**: Free tier available (with rate limits)

## Disabling AI

To use only the fallback responses, set:
```python
AI_PROVIDER = "none"
```

Enjoy unlimited, intelligent pet care responses! 🐾

