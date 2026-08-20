import os
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import base64

from groq import Groq

# Free TTS
from gtts import gTTS


# ------------------ SPEECH TO TEXT (GROQ WHISPER) ------------------

def transcribe_audio_groq(groq_api_key, audio_path):
    client = Groq(api_key=groq_api_key)

    with open(audio_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(audio_path, file.read()),
            model="whisper-large-v3",
            temperature=0,
            response_format="verbose_json",
        )

    return transcription.text


# ------------------ AI RESPONSE (GROQ) ------------------

def fetch_ai_response(groq_api_key, input_text):
    client = Groq(api_key=groq_api_key)

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful voice assistant. Keep responses concise and conversational."
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=0.7,
        top_p=0.9,
        max_tokens=1024,
    )

    return completion.choices[0].message.content


# ------------------ TEXT TO SPEECH (gTTS) ------------------

def text_to_audio(text, audio_path):
    tts = gTTS(text=text, lang="en")
    tts.save(audio_path)


# ------------------ UI HELPERS ------------------

def create_text_card(text, title="Response"):
    st.markdown(f"""
    <div style="box-shadow:0 4px 8px rgba(0,0,0,0.2); padding:15px; border-radius:10px; margin:10px 0;">
        <h4>{title}</h4>
        <p>{text}</p>
    </div>
    """, unsafe_allow_html=True)


def auto_play_audio(audio_file):
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()

    base64_audio = base64.b64encode(audio_bytes).decode("utf-8")

    st.markdown(
        f'<audio src="data:audio/mp3;base64,{base64_audio}" controls autoplay></audio>',
        unsafe_allow_html=True
    )


# ------------------ MAIN APP ------------------

def main():
    st.set_page_config(layout="wide")

    st.sidebar.title("🔑 API CONFIG")

    groq_api_key = st.sidebar.text_input("Groq API Key", type="password")

    st.title("🎤 Swar AI (Whisper Large v3 + GPT-OSS 120B)")
    st.write("Speak → Transcribe → AI Response → Voice Output 🚀")

    if groq_api_key:

        recorded_audio = audio_recorder()

        if recorded_audio:
            audio_file = "audio.mp3"

            with open(audio_file, "wb") as f:
                f.write(recorded_audio)

            # 🎤 Speech → Text
            with st.spinner("Transcribing audio..."):
                try:
                    transcribed_text = transcribe_audio_groq(groq_api_key, audio_file)
                    if not transcribed_text.strip():
                        st.warning("No speech detected. Please try again.")
                        return
                    create_text_card(transcribed_text, "📝 Transcription")
                except Exception as e:
                    st.error(f"Transcription Error: {e}")
                    return

            # 🧠 AI Response
            with st.spinner("Generating AI response..."):
                try:
                    ai_response = fetch_ai_response(groq_api_key, transcribed_text)
                    create_text_card(ai_response, "🤖 AI Response")
                except Exception as e:
                    st.error(f"AI Response Error: {e}")
                    return

            # 🔊 Text → Speech
            with st.spinner("Generating voice response..."):
                try:
                    response_audio_file = "response.mp3"
                    text_to_audio(ai_response, response_audio_file)
                    auto_play_audio(response_audio_file)
                except Exception as e:
                    st.error(f"TTS Error: {e}")

    else:
        st.warning("Please enter your Groq API key to continue.")


if __name__ == "__main__":
    main()