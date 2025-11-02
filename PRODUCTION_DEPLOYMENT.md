# Production Deployment Guide

## ⚠️ Important: Development vs Production

**Current Setup**: The `server.py` uses Flask's built-in development server which is:
- ❌ NOT suitable for production
- ❌ Single-threaded (can't handle multiple requests well)
- ❌ Not secure for public use
- ✅ Good for local development only

## 🚀 Production Deployment Options

### Option 1: Waitress (Recommended for Windows/Cross-Platform)

**Install:**
```powershell
pip install waitress
```

**Run:**
```powershell
python run_production.py
```

Or directly:
```powershell
waitress-serve --host=0.0.0.0 --port=5000 server:app
```

### Option 2: Gunicorn (Linux/Mac)

**Install:**
```bash
pip install gunicorn
```

**Run:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 server:app
```

### Option 3: uWSGI (Advanced)

**Install:**
```bash
pip install uwsgi
```

**Run:**
```bash
uwsgi --http :5000 --wsgi-file server.py --callable app --processes 4 --threads 2
```

## 📋 Deployment Platforms

### Heroku

1. Create `Procfile`:
   ```
   web: waitress-serve --host=0.0.0.0 --port=$PORT server:app
   ```

2. Deploy:
   ```bash
   git push heroku main
   ```

### PythonAnywhere

1. Use Waitress or Gunicorn in your WSGI configuration file
2. Point to `server:app`

### DigitalOcean / AWS / Azure

1. Use Waitress or Gunicorn with a reverse proxy (Nginx)
2. Set up SSL with Let's Encrypt
3. Use process manager like systemd or PM2

### Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "run_production.py"]
```

Build and run:
```bash
docker build -t pet-chatbot .
docker run -p 5000:5000 pet-chatbot
```

## 🔒 Security Considerations

1. **Set Environment Variables**: Don't hardcode API keys
   ```powershell
   $env:OPENAI_API_KEY = "your-key"
   $env:GEMINI_API_KEY = "your-key"
   ```

2. **Use HTTPS**: Always use HTTPS in production (Let's Encrypt)

3. **Firewall**: Only expose necessary ports

4. **Rate Limiting**: Consider adding rate limiting for API endpoints

5. **CORS**: Review CORS settings for production

## 🧪 Testing Production Server Locally

1. Install waitress:
   ```powershell
   pip install waitress
   ```

2. Run production server:
   ```powershell
   python run_production.py
   ```

3. Test at: `http://localhost:5000`

## 📝 Quick Reference

| Command | Use Case |
|---------|----------|
| `python server.py` | Development only (with warnings) |
| `python run_production.py` | Production (recommended) |
| `waitress-serve --host=0.0.0.0 --port=5000 server:app` | Production (alternative) |

## ✅ Best Practices

- ✅ Always use a production WSGI server (Waitress/Gunicorn/uWSGI)
- ✅ Set `debug=False` in production
- ✅ Use environment variables for secrets
- ✅ Set up proper logging
- ✅ Use a reverse proxy (Nginx) for SSL and static files
- ✅ Monitor your application (logs, performance)

## 🔧 Environment Variables

Create a `.env` file (or set system environment variables):
```
FLASK_ENV=production
PORT=5000
OPENAI_API_KEY=your-key
GEMINI_API_KEY=your-key
ELEVENLABS_API_KEY=your-key
```

## 📞 Need Help?

For specific platform deployment, refer to:
- [Waitress Documentation](https://docs.pylonsproject.org/projects/waitress/en/latest/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/latest/deploying/)

