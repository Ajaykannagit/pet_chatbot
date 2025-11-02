# config.py - AI API and ElevenLabs configuration
import os

# === AI API Configuration ===
# Choose which AI provider to use: "openai", "anthropic", "gemini", or None for fallback mode
AI_PROVIDER = os.environ.get("AI_PROVIDER", "gemini").lower()  # Options: openai, anthropic, gemini, none

# OpenAI API Key (get from https://platform.openai.com/api-keys)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "your-openai-key-here")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")  # or "gpt-4", "gpt-3.5-turbo"

# Anthropic API Key (get from https://console.anthropic.com/)
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "your-anthropic-key-here")
ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")  # or "claude-3-haiku-20240307"

# Google Gemini API Key (get from https://makersuite.google.com/app/apikey)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "your-gemini-key-here")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")  # Available: "gemini-2.0-flash", "gemini-2.5-flash", "gemini-pro-latest"

# === ElevenLabs Configuration ===
# Get this from elevenlabs.io → Profile → API Key
# Prefer environment variable, fallback to hardcoded placeholder
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY", "your-elevenlabs-key-here")

# Data sources - Using reliable pet care APIs
DATA_SOURCES = {
    "dogs": "https://dog.ceo/api/breeds/list/all",
    "cats": "https://api.thecatapi.com/v1/breeds", 
    "emergency": "https://api.github.com/repos/microsoft/vscode"  # Placeholder - will use fallback
}

# Comprehensive pet knowledge
FALLBACK_DATA = {
    "dogs": {
        "food": "Dogs need balanced dog food. Puppies eat 3-4 times daily, adults 2 times. Avoid chocolate, grapes, onions, garlic, and xylitol.",
        "vaccine": "Core vaccines: rabies, distemper, parvovirus. Puppies start at 6-8 weeks. Adults need yearly boosters.",
        "health": "Watch for vomiting, diarrhea, lethargy. Regular vet checks every 6-12 months.",
        "behavior": "Dogs need daily exercise and mental stimulation. Barking can mean boredom or anxiety.",
        "training": "Use positive reinforcement with treats. Start with sit, stay, come commands.",
        "emergency": "Emergency signs: difficulty breathing, seizures, poisoning, trauma, bloated abdomen."
    },
    "cats": {
        "food": "Cats need high-protein food. Feed 2-3 times daily. Avoid onions, garlic, chocolate, lilies.",
        "vaccine": "Core vaccines: rabies, feline distemper. Kittens start at 6-8 weeks.",
        "health": "Cats hide illness well. Watch for changes in eating, litter habits, or behavior.",
        "behavior": "Provide scratching posts, vertical space. Sudden changes may mean illness.",
        "litter": "Have 1 more litter box than cats. Scoop daily, clean weekly.",
        "emergency": "URGENT: Straining to urinate (blockage), not eating 24+ hours, difficulty breathing."
    },
    "emergency": {
        "keywords": ["emergency", "bleeding", "poison", "not breathing", "unconscious", "seizure", "choking", "trauma"],
        "response": "🚨 THIS IS AN EMERGENCY! Contact your veterinarian or emergency animal hospital immediately!",
        "emotion": "emergency"
    }
}

