"""
Production server for Pet Care Chatbot
Uses Waitress - a production-ready WSGI server for Windows and cross-platform use
"""
from waitress import serve
from server import app
import os

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"🚀 Starting production server on {host}:{port}")
    print("   Press Ctrl+C to stop")
    
    # Serve the Flask app using Waitress
    # Waitress is production-ready, supports Windows, and handles multiple requests
    serve(
        app,
        host=host,
        port=port,
        threads=4,  # Number of threads to handle requests
        channel_timeout=120  # Timeout for slow requests
    )

