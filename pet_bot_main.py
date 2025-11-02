# pet_bot_main.py - Main chatbot application with AI API support
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import speech_recognition as sr
from pet_data_loader import pet_data
from config import ELEVENLABS_API_KEY
from ai_provider import ai_provider

class PetCareChatbot:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # Enable TTS only if a plausible API key is present
        self.tts_enabled = bool(ELEVENLABS_API_KEY and ELEVENLABS_API_KEY != "your-elevenlabs-key-here")
        self.elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY) if self.tts_enabled else None
        
        # AI provider for enhanced responses
        self.ai_enabled = ai_provider.enabled
        
        # Initialize all pet data
        pet_data.initialize_all_data()
        
        if self.ai_enabled:
            print(f"[bot] AI-enhanced mode enabled using {ai_provider.provider}")
        else:
            print("[bot] Using fallback mode with basic pet data")
        
    def listen(self):
        """Listen to user input via microphone when available; fallback to text input."""
        # Try microphone speech recognition first
        try:
            with sr.Microphone() as source:
                print("[mic] Listening... (speak now, or press Enter to type)")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=15)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"[you] (voice): {text}")
                return text
            except sr.UnknownValueError:
                print("[stt] Didn't catch that. Please type your question:")
            except sr.RequestError as e:
                print(f"[stt] Service error: {e}. Please type your question:")
        except Exception:
            # Microphone not available or permission denied
            pass

        # Fallback to typed input
        try:
            print("[type] Please type your question:")
            return input("👤 You: ")
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def speak(self, text, emotion="calm"):
        """Make the bot speak with emotion"""
        print(f"[bot] {text}")
        
        # Emotional voice settings
        emotions = {
            "happy": {"stability": 0.3, "similarity_boost": 0.7},
            "concerned": {"stability": 0.5, "similarity_boost": 0.8},
            "emergency": {"stability": 0.2, "similarity_boost": 0.9},
            "calm": {"stability": 0.7, "similarity_boost": 0.5}
        }
        
        settings = emotions.get(emotion, emotions["calm"])
        
        if not self.tts_enabled:
            print("[tts] disabled: set ELEVENLABS_API_KEY to enable TTS.")
            return

        try:
            from elevenlabs import VoiceSettings
            audio_stream = self.elevenlabs_client.text_to_speech.convert(
                text=text,
                voice_id="EXAVITQu4vr4xnSDxMaL",
                model_id="eleven_monolingual_v1",
                voice_settings=VoiceSettings(
                    stability=settings["stability"],
                    similarity_boost=settings["similarity_boost"]
                )
            )
            # The SDK returns a streaming iterator; play supports streaming
            play(audio_stream)
        except Exception as e:
            print(f"[tts] error: {e}")
            print("(Text response still works!)")
    
    def get_response(self, user_input):
        """Generate response using AI API (if enabled) or fallback to pet data"""
        original_input = user_input
        user_input_lower = user_input.lower()
        
        # First, check for emergencies (always priority)
        emergency_response, emotion = pet_data.check_emergency(user_input_lower)
        if emergency_response:
            return emergency_response, emotion
        
        # ALWAYS try AI provider first if enabled (for ALL queries)
        if self.ai_enabled:
            # Try to get context from pet data for better AI responses
            context = None
            animals = ["dog", "cat", "bird", "rabbit", "fish"]
            problems = ["food", "vaccine", "vaccination", "health", "sick", "behavior", "training", "emergency", "eat", "diet", "litter", "bark", "scratch"]
            
            # Gather context if we can find relevant pet data
            for animal in animals:
                if animal in user_input_lower:
                    for problem in problems:
                        if problem in user_input_lower:
                            advice = pet_data.get_pet_advice(animal, problem)
                            if advice:
                                context = advice  # Use as context for AI
                                break
                    break  # Found animal, no need to check others
            
            # ALWAYS call AI for any query when enabled
            try:
                ai_response = ai_provider.get_response(original_input, context)
                if ai_response and ai_response[0]:  # Make sure we got a valid response
                    return ai_response
            except Exception as e:
                print(f"[error] AI provider error: {e}")
                # Fall through to fallback
        
        # Fallback to basic pet data responses (only if AI disabled or failed)
        animals = ["dog", "cat", "bird", "rabbit", "fish"]
        problems = ["food", "vaccine", "vaccination", "health", "sick", "behavior", "training", "emergency", "eat", "diet", "litter", "bark", "scratch"]
        
        for animal in animals:
            if animal in user_input_lower:
                for problem in problems:
                    if problem in user_input_lower:
                        advice = pet_data.get_pet_advice(animal, problem)
                        if advice:
                            return advice, "calm"
                # If animal detected but no specific problem
                return f"For {animal} care, I can help with: food, vaccines, health issues, behavior training, and emergencies. What specifically do you need help with?", "calm"
        
        # General response
        return "I can help with pet care advice for dogs, cats, birds, rabbits, and fish. What pet do you have and what's your question?", "calm"
    
    def run(self):
        """Main program loop"""
        print("[start] Starting Smart Pet Care Chatbot...")
        print("[data] Using comprehensive pet data!")
        self.speak("Hello! I'm your pet care assistant. I have information about dog and cat care, health, and emergencies. How can I help you today?", "happy")
        
        while True:
            user_text = self.listen()
            
            if user_text is None:
                continue
                
            if any(word in user_text.lower() for word in ["bye", "exit", "quit", "goodbye"]):
                self.speak("Goodbye! Remember to contact a vet for serious health concerns. Take care of your pets!", "happy")
                break
            
            response, emotion = self.get_response(user_text)
            self.speak(response, emotion)

# === START THE BOT ===
if __name__ == "__main__":
    bot = PetCareChatbot()
    bot.run()