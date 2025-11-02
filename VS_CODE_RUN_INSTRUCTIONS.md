# How to Run Pet Chatbot in VS Code

## Method 1: Using VS Code Terminal (Easiest)

1. **Open the project in VS Code**
   - Open VS Code
   - File → Open Folder → Select `pet_chatbot` folder

2. **Open Terminal in VS Code**
   - Press `` Ctrl + ` `` (backtick) OR
   - Go to: **Terminal** → **New Terminal** from the menu

3. **Install Dependencies** (if not already installed)
   ```powershell
   pip install -r requirements.txt
   ```

4. **Start the Server**
   ```powershell
   python server.py
   ```

5. **Access the Chatbot**
   - Open your web browser
   - Go to: `http://localhost:5000`
   - You should see the Pet Care Chatbot interface!

## Method 2: Using VS Code Run Configuration

1. **Create Launch Configuration**
   - Press `F5` or go to **Run and Debug** (Ctrl+Shift+D)
   - Click "create a launch.json file"
   - Select "Python File"
   - Replace the content with:

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python: Pet Chatbot Server",
               "type": "debugpy",
               "request": "launch",
               "program": "${workspaceFolder}/server.py",
               "console": "integratedTerminal",
               "justMyCode": true
           }
       ]
   }
   ```

2. **Run the Server**
   - Press `F5` to start debugging
   - OR click the green play button in the Run and Debug panel
   - The server will start and show output in the terminal

3. **Access the Chatbot**
   - Open browser to: `http://localhost:5000`

## Method 3: Using VS Code Tasks

1. **Create Tasks Configuration**
   - Press `Ctrl+Shift+P` → Type "Tasks: Configure Task"
   - Select "Create tasks.json file from template"
   - Select "Others"
   - Replace with:

   ```json
   {
       "version": "2.0.0",
       "tasks": [
           {
               "label": "Start Pet Chatbot Server",
               "type": "shell",
               "command": "python",
               "args": ["server.py"],
               "options": {
                   "cwd": "${workspaceFolder}"
               },
               "problemMatcher": [],
               "presentation": {
                   "reveal": "always",
                   "panel": "new"
               },
               "runOptions": {
                   "runOn": "default"
               }
           }
       ]
   }
   ```

2. **Run the Task**
   - Press `Ctrl+Shift+P`
   - Type "Tasks: Run Task"
   - Select "Start Pet Chatbot Server"

## Quick Access Tips

### Keyboard Shortcuts:
- **Terminal**: `` Ctrl + ` ``
- **Stop Server**: `Ctrl+C` in the terminal
- **New Terminal**: `` Ctrl + Shift + ` ``

### Viewing Output:
- Check the **Terminal** panel at the bottom for server logs
- Look for messages like:
  - `[ai] OpenAI initialized with model: gpt-4o-mini`
  - `[bot] AI-enhanced mode enabled using openai`
  - ` * Running on http://0.0.0.0:5000`

### Stopping the Server:
- Click in the terminal window
- Press `Ctrl+C`
- Server will stop gracefully

## Troubleshooting

### Port Already in Use:
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual number)
taskkill /PID <PID> /F
```

### Module Not Found:
```powershell
# Install all dependencies
pip install -r requirements.txt
```

### Python Not Found:
- Make sure Python is installed and in PATH
- In VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter"
- Choose your Python installation

## What You Should See

When the server starts successfully, you'll see:
```
[info] Initializing pet data...
[ai] OpenAI initialized with model: gpt-4o-mini
[bot] AI-enhanced mode enabled using openai
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

Then open `http://localhost:5000` in your browser! 🐾

