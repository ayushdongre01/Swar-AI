# 🎤 Swar AI - Voice Assistant

A powerful voice-based AI assistant that transcribes speech, generates intelligent responses using DeepSeek, and converts them back to audio. Built with **Streamlit**, **Groq Whisper**, and **GitHub Models (DeepSeek)**.

---

## 🚀 Features

✨ **Speech-to-Text**: Real-time audio transcription using Groq's Whisper Large V3 model  
🧠 **AI-Powered Responses**: Intelligent conversational responses via DeepSeek-V3  
🔊 **Text-to-Speech**: Automatic voice generation of AI responses using gTTS  
🎙️ **Voice Recording**: Built-in audio recorder directly in the web interface  
📱 **Responsive UI**: Clean, modern interface with interactive cards  
⚡ **Fast Processing**: Optimized for quick responses  

---

## 🌐 Live Demo

👉 Try the app here:  
🔗 [https://blogflow-ai.streamlit.app/](https://blogflow-ai.streamlit.app/)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend Framework** | Streamlit |
| **Speech-to-Text** | Groq (Whisper Large V3) |
| **LLM Model** | DeepSeek-V3 via GitHub Models |
| **Text-to-Speech** | gTTS (Google Text-to-Speech) |
| **Audio Recording** | audio-recorder-streamlit |
| **Language** | Python 3.8+ |

---

## 📋 Prerequisites

Before running the app, ensure you have:

- **Python 3.8 or higher**
- **Groq API Key** 
- **GitHub Token** (with access to GitHub Models) 

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd "Swar AI"
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
Create a `.streamlit/secrets.toml` file in your project directory:

```toml
GROQ_API_KEY = "your-groq-api-key-here"
GITHUB_TOKEN = "your-github-token-here"
```

*Alternatively*, enter your API keys directly in the sidebar when running the app.

---

## 🎯 Usage

### Run Locally
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501/`

### How to Use

1. **Enter API Keys** (if not using secrets.toml):
   - Paste your Groq API Key
   - Paste your GitHub Token

2. **Record Audio**:
   - Click the microphone button to start recording
   - Speak clearly
   - Stop recording when done

3. **View Results**:
   - 📝 See your transcribed text
   - 🤖 Read the AI's response
   - 🔊 Listen to the voice response (auto-plays)

---

## 📸 Sample Output Images

![Swar AI – Sample Image 1](https://github.com/ayushdongre01/Swar-AI/blob/main/images/1.png)
![Swar AI – Sample Image 2](https://github.com/ayushdongre01/Swar-AI/blob/main/images/2.png)

---

## 🔑 API Keys Required

### Groq API Key
- Purpose: Speech-to-Text (Whisper Large V3) and audio transcription
- Get key: https://console.groq.com/
- Free tier: ✅ Yes (with rate limits)

### GitHub Token (for DeepSeek)
- Purpose: Access DeepSeek-V3 model via GitHub Models
- Get token: https://github.com/settings/tokens
- Required permissions: `read:user` (minimum)

---

## ⚙️ Configuration

The app uses the following default settings:

| Setting | Value | Description |
|---------|-------|-----------|
| **Transcription Model** | whisper-large-v3 | Latest Whisper model for high accuracy |
| **LLM Model** | DeepSeek-V3 | State-of-the-art reasoning model |
| **Temperature** | 0.7 | Balance between creativity and coherence |
| **Max Tokens** | 1024 | Maximum response length |
| **Top-P** | 0.9 | Nucleus sampling for diversity |

---

## 🛠️ Troubleshooting

### Issue: "Invalid API Key" Error
**Solution**: Double-check your API keys are correct and have been copied fully without extra spaces.

### Issue: "No speech detected" Warning
**Solution**: 
- Ensure your microphone works properly
- Speak clearly and loudly
- Check microphone permissions in browser

### Issue: Slow Response Time
**Solution**:
- First-time model loading takes longer
- Check your internet connection
- Verify API rate limits aren't exceeded

### Issue: Audio Playback Not Working
**Solution**:
- Ensure browser allows audio autoplay
- Check if audio was generated without errors
- Try refreshing the page

### Issue: "Connection Error" to Groq/GitHub
**Solution**:
- Check your internet connection
- Verify API keys are valid and not revoked
- Wait a few minutes if hitting rate limits

---

## 📝 Requirements File

Create `requirements.txt`:

```
streamlit
audio-recorder-streamlit
groq
azure-ai-inference
azure-core
gtts
```

### Install:
```bash
pip install -r requirements.txt
```

---

## 🚀 Deployment

### Deploy on Streamlit Cloud

1. **Push code to GitHub**
```bash
git add .
git commit -m "Deploy Swar AI"
git push origin main
```

2. **Deploy on Streamlit Cloud**:
   - Go to https://streamlit.io/cloud
   - Click "New app" → Select your repo
   - Set main file to `app.py`
   - Add secrets in deployment settings

3. **Add Secrets**:
   - In Streamlit Cloud dashboard
   - Go to Settings → Secrets
   - Add your API keys:
   ```
   GROQ_API_KEY = "your-key"
   GITHUB_TOKEN = "your-token"
   ```

---

## 🎨 UI/UX Features

- **Real-time Recording**: Live audio input with visual feedback
- **Styled Cards**: Modern card-based display for each response
- **Auto-playing Audio**: Responses automatically play without user interaction
- **Error Handling**: Clear error messages for debugging
- **Loading Spinners**: Visual progress indicators during processing

---

## 📊 Architecture Flow

```
┌─────────────┐
│   Record    │
│   Audio     │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Groq Whisper     │
│ (Speech-to-Text) │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ DeepSeek-V3      │
│ (AI Response)    │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ gTTS             │
│ (Text-to-Speech) │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Play Audio       │
│ Response         │
└──────────────────┘
```

---

## 💡 Tips & Best Practices

- **Microphone Quality**: Use a good quality microphone for better transcription
- **Clear Speech**: Speak naturally but clearly for accurate transcription
- **Quiet Environment**: Reduce background noise for better results
- **API Rate Limits**: Be aware of rate limits on free Groq and GitHub Models tiers
- **Response Length**: Keep prompts concise for faster responses

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. **Report Issues**: Found a bug? Create an issue
2. **Suggest Features**: Have ideas? Open a discussion
3. **Submit PRs**: Improvements welcome!

---

## 🔗 Links

- 🌐 **Live Demo**: [https://blogflow-ai.streamlit.app/](https://blogflow-ai.streamlit.app/)
- 📖 **Streamlit Docs**: https://docs.streamlit.io/
- 🤖 **Groq Documentation**: https://console.groq.com/docs
- 🧠 **DeepSeek Model**: https://deepseek.com/
- 🎙️ **GitHub Models**: https://github.com/marketplace/models

---

## ❓ FAQ

### Q: Can I use this with other TTS services?
**A**: Yes! You can modify the `text_to_audio()` function to use Azure Speech, Eleven Labs, or other services.

### Q: Is there a cost to use this app?
**A**: 
- Groq: Free tier available (with rate limits)
- GitHub Models: Free tier available
- gTTS: Free
- Streamlit Cloud: Free tier available

### Q: Can I deploy this privately?
**A**: Yes! You can deploy it on your own server using Docker or any Python hosting service.

### Q: Does it work offline?
**A**: No, it requires internet connection for Groq and GitHub Model API calls.

### Q: What languages are supported?
**A**: Whisper supports 99+ languages. gTTS supports 100+ languages. Configure in the code as needed.

---

## 📞 Support

If you encounter issues:
1. Check the **Troubleshooting** section above
2. Review API documentation for Groq and GitHub Models
3. Check Streamlit documentation: https://docs.streamlit.io/

---

**Made with ❤️ using Streamlit, Groq, and DeepSeek**
