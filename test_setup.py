#!/usr/bin/env python
"""Quick test to verify everything works"""
import sys

try:
    from server import app
    print("[OK] Server imports OK")
except Exception as e:
    print(f"[FAIL] Server import failed: {e}")
    sys.exit(1)

try:
    from pet_bot_main import PetCareChatbot
    print("[OK] Chatbot imports OK")
except Exception as e:
    print(f"[FAIL] Chatbot import failed: {e}")
    sys.exit(1)

try:
    bot = PetCareChatbot()
    print("[OK] Chatbot initialized OK")
except Exception as e:
    print(f"[FAIL] Chatbot initialization failed: {e}")
    sys.exit(1)

try:
    # Test basic response (without API)
    result = bot.get_response("test")
    print(f"[OK] Basic response test OK: {result[0][:50]}...")
except Exception as e:
    print(f"[FAIL] Response test failed: {e}")
    sys.exit(1)

print("\n[SUCCESS] All tests passed! Ready for GitHub upload.")

