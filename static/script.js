const logEl = document.getElementById('log');
const textEl = document.getElementById('text');
const micBtn = document.getElementById('mic');
const sendBtn = document.getElementById('send');
const stopBtn = document.getElementById('stop');
const statusEl = document.getElementById('status');
const player = document.getElementById('player');

function appendMsg(who, content) {
  // Remove empty state if it exists
  const emptyState = logEl.querySelector('.empty-state');
  if (emptyState) {
    emptyState.remove();
  }
  
  const div = document.createElement('div');
  div.className = `msg ${who}`;
  
  // Create avatar
  const avatar = document.createElement('div');
  avatar.className = 'avatar';
  avatar.textContent = who === 'me' ? '👤' : '🐾';
  
  // Create content wrapper
  const contentWrapper = document.createElement('div');
  contentWrapper.className = 'content';
  
  // Create label
  const label = document.createElement('div');
  label.className = 'label';
  label.textContent = who === 'me' ? 'You' : 'Assistant';
  
  // Create text content
  const text = document.createElement('div');
  text.textContent = content;
  
  // Assemble message
  contentWrapper.appendChild(label);
  contentWrapper.appendChild(text);
  div.appendChild(avatar);
  div.appendChild(contentWrapper);
  
  logEl.appendChild(div);
  logEl.scrollTop = logEl.scrollHeight;
}

async function callChatAPI(text) {
  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  if (!res.ok) throw new Error(`Chat error ${res.status}`);
  return res.json();
}

function withTimeout(promise, ms) {
  return Promise.race([
    promise,
    new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), ms))
  ]);
}

async function playTTS(text, emotion) {
  try {
    const res = await withTimeout(fetch('/api/tts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, emotion })
    }), 15000); // 15s safety timeout
    if (res.status === 501) {
      // TTS not configured: fallback to browser SpeechSynthesis if available
      if ('speechSynthesis' in window) {
        const u = new SpeechSynthesisUtterance(text);
        window.speechSynthesis.speak(u);
      }
      return;
    }
    if (!res.ok) throw new Error(`TTS error ${res.status}`);
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    player.src = url;
    await player.play();
  } catch (e) {
    console.warn('TTS playback failed:', e);
  }
}

async function handleSend() {
  const text = (textEl.value || '').trim();
  if (!text) return;
  appendMsg('me', text);
  textEl.value = '';
  statusEl.textContent = '🤔 Thinking...';
  try {
    const { response, emotion } = await callChatAPI(text);
    appendMsg('bot', response);
    await playTTS(response, emotion);
    statusEl.textContent = '';
  } catch (e) {
    statusEl.textContent = `❌ Error: ${e.message}`;
    setTimeout(() => { statusEl.textContent = ''; }, 5000);
  }
}

sendBtn.addEventListener('click', handleSend);
textEl.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') handleSend();
});

// Mic (Web Speech API)
let recognition = null;
let recognizing = false;

function setupRecognition() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) {
    micBtn.disabled = true;
    micBtn.textContent = '🎤 N/A';
    statusEl.textContent = '🎤 Mic not supported';
    return null;
  }
  const r = new SR();
  r.lang = 'en-US';
  r.interimResults = false;
  r.maxAlternatives = 1;
  r.onstart = () => { 
    recognizing = true; 
    statusEl.textContent = '🎤 Listening...';
    micBtn.classList.add('listening');
  };
  r.onend = () => { 
    recognizing = false; 
    statusEl.textContent = '';
    micBtn.classList.remove('listening');
  };
  r.onerror = (e) => { 
    statusEl.textContent = `🎤 Error: ${e.error}`;
    micBtn.classList.remove('listening');
    setTimeout(() => { statusEl.textContent = ''; }, 5000);
  };
  r.onresult = (e) => {
    const transcript = e.results[0][0].transcript;
    appendMsg('me', transcript);
    callChatAPI(transcript)
      .then(({ response, emotion }) => {
        appendMsg('bot', response);
        return playTTS(response, emotion);
      })
      .catch((err) => { 
        statusEl.textContent = `❌ Error: ${err.message}`;
        setTimeout(() => { statusEl.textContent = ''; }, 5000);
      });
  };
  return r;
}

recognition = setupRecognition();

micBtn.addEventListener('click', () => {
  if (!recognition) return;
  if (!recognizing) {
    try { recognition.start(); } catch (_) {}
  } else {
    try { recognition.stop(); } catch (_) {}
  }
});

stopBtn.addEventListener('click', () => {
  try { if (recognition && recognizing) recognition.stop(); } catch (_) {}
  try { player.pause(); player.currentTime = 0; } catch (_) {}
  try { if ('speechSynthesis' in window) window.speechSynthesis.cancel(); } catch (_) {}
});

// Basic ready check so the UI doesn't feel stuck
fetch('/api/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text: 'ping' }) })
  .then(() => { 
    statusEl.textContent = '✅ Connected';
    setTimeout(() => { statusEl.textContent = ''; }, 2000);
  })
  .catch(() => { statusEl.textContent = '🔄 Connecting...'; });


