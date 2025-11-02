# ai_provider.py - AI API integration for enhanced responses
import os
from config import (
    AI_PROVIDER, 
    OPENAI_API_KEY, OPENAI_MODEL,
    ANTHROPIC_API_KEY, ANTHROPIC_MODEL,
    GEMINI_API_KEY, GEMINI_MODEL
)

class AIProvider:
    """Unified interface for multiple AI providers"""
    
    def __init__(self):
        self.provider = AI_PROVIDER
        self.client = None
        self.enabled = False
        
        # Pet care system prompt
        self.system_prompt = """You are a helpful and knowledgeable pet care assistant. 
You provide accurate, empathetic, and practical advice about pet care including:
- Dogs, cats, birds, rabbits, fish, and other common pets
- Food and nutrition
- Health issues and symptoms
- Vaccinations and preventive care
- Behavior and training
- Emergency situations (always advise contacting a veterinarian immediately)

Important guidelines:
- Be concise but informative (2-4 sentences usually)
- For emergencies, immediately advise contacting a veterinarian
- Always prioritize pet safety and well-being
- If unsure, recommend consulting a veterinarian
- Be friendly and empathetic in your responses
- IMPORTANT: Do NOT use markdown formatting like asterisks (*) or underscores (_) in your responses. Write in plain text only."""
        
        self._initialize()
    
    def _initialize(self):
        """Initialize the selected AI provider"""
        if not self.provider or self.provider == "none":
            print("[ai] AI provider disabled - using fallback responses")
            return
        
        try:
            if self.provider == "openai":
                self._init_openai()
            elif self.provider == "anthropic":
                self._init_anthropic()
            elif self.provider == "gemini":
                self._init_gemini()
            else:
                print(f"[ai] Unknown provider '{self.provider}' - using fallback")
        except Exception as e:
            print(f"[ai] Failed to initialize {self.provider}: {e}")
            print("[ai] Falling back to basic responses")
            self.enabled = False
    
    def _init_openai(self):
        """Initialize OpenAI client"""
        if not OPENAI_API_KEY or OPENAI_API_KEY == "your-openai-key-here":
            print("[ai] OpenAI API key not set")
            return
        
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=OPENAI_API_KEY)
            self.enabled = True
            print(f"[ai] OpenAI initialized with model: {OPENAI_MODEL}")
        except ImportError:
            print("[ai] OpenAI library not installed. Run: pip install openai")
    
    def _init_anthropic(self):
        """Initialize Anthropic client"""
        if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == "your-anthropic-key-here":
            print("[ai] Anthropic API key not set")
            return
        
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
            self.enabled = True
            print(f"[ai] Anthropic initialized with model: {ANTHROPIC_MODEL}")
        except ImportError:
            print("[ai] Anthropic library not installed. Run: pip install anthropic")
    
    def _init_gemini(self):
        """Initialize Google Gemini client"""
        if not GEMINI_API_KEY or GEMINI_API_KEY == "your-gemini-key-here":
            print("[ai] Gemini API key not set")
            return
        
        try:
            import google.generativeai as genai
            genai.configure(api_key=GEMINI_API_KEY)
            model_name = GEMINI_MODEL
            
            # Try the model name as-is first
            try:
                self.client = genai.GenerativeModel(model_name)
                self.enabled = True
                print(f"[ai] Gemini initialized with model: {model_name}")
            except Exception as e1:
                # Fallback to gemini-2.0-flash
                try:
                    self.client = genai.GenerativeModel("gemini-2.0-flash")
                    self.enabled = True
                    print(f"[ai] Gemini initialized with fallback model: gemini-2.0-flash")
                except Exception as e2:
                    raise Exception(f"Failed to initialize with {model_name} or gemini-2.0-flash: {e1}, {e2}")
        except ImportError:
            print("[ai] Google Generative AI library not installed. Run: pip install google-generativeai")
        except Exception as e:
            print(f"[ai] Gemini initialization error: {e}")
            print("[ai] Try checking your API key or model name")
    
    def _clean_markdown(self, text):
        """Remove markdown formatting from text"""
        import re
        # Remove bold/italic markdown: **text** or *text* or __text__ or _text_
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Remove **bold**
        text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Remove *italic*
        text = re.sub(r'__([^_]+)__', r'\1', text)      # Remove __bold__
        text = re.sub(r'_([^_]+)_', r'\1', text)        # Remove _italic_
        # Remove standalone asterisks
        text = re.sub(r'\*{1,3}', '', text)
        # Clean up multiple spaces
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def get_response(self, user_input, context_data=None):
        """
        Get AI-generated response with pet care context
        
        Args:
            user_input: User's question
            context_data: Optional context from pet data (for better responses)
        
        Returns:
            tuple: (response_text, emotion) or None if AI unavailable
        """
        if not self.enabled or not self.client:
            return None
        
        # Build enhanced prompt with context if available
        prompt = user_input
        if context_data:
            prompt = f"Context: {context_data}\n\nUser question: {user_input}"
        
        try:
            if self.provider == "openai":
                response = self._get_openai_response(prompt)
            elif self.provider == "anthropic":
                response = self._get_anthropic_response(prompt)
            elif self.provider == "gemini":
                response = self._get_gemini_response(prompt)
            else:
                return None
            
            # Response already cleaned in individual methods
            if response:
                return response
            return None
        except Exception as e:
            print(f"[ai] Error getting AI response: {e}")
            return None
    
    def _get_openai_response(self, prompt):
        """Get response from OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            text = response.choices[0].message.content.strip()
            text = self._clean_markdown(text)
            emotion = self._detect_emotion(text)
            return text, emotion
        except Exception as e:
            print(f"[ai] OpenAI API error: {e}")
            raise
    
    def _get_anthropic_response(self, prompt):
        """Get response from Anthropic"""
        message = self.client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=300,
            temperature=0.7,
            system=self.system_prompt,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        text = message.content[0].text.strip()
        text = self._clean_markdown(text)
        emotion = self._detect_emotion(text)
        return text, emotion
    
    def _get_gemini_response(self, prompt):
        """Get response from Google Gemini"""
        full_prompt = f"{self.system_prompt}\n\n{prompt}"
        response = self.client.generate_content(
            full_prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 300,
            }
        )
        text = response.text.strip()
        text = self._clean_markdown(text)
        emotion = self._detect_emotion(text)
        return text, emotion
    
    def _detect_emotion(self, text):
        """Detect emotion from response text for TTS"""
        text_lower = text.lower()
        
        # Emergency indicators
        if any(word in text_lower for word in ["emergency", "urgent", "immediately", "contact vet", "call vet", "🚨"]):
            return "emergency"
        
        # Concern indicators
        if any(word in text_lower for word in ["concern", "worried", "watch", "careful", "caution"]):
            return "concerned"
        
        # Happy/positive indicators
        if any(word in text_lower for word in ["great", "wonderful", "excellent", "good news", "happy", "healthy"]):
            return "happy"
        
        # Default to calm
        return "calm"


# Create global instance
ai_provider = AIProvider()

