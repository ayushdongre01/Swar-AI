import os
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import base64

from groq import Groq

# DeepSeek via GitHub Models
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

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


# ------------------ DEEPSEEK RESPONSE ------------------

def fetch_ai_response(github_token, input_text):
    client = ChatCompletionsClient(
        endpoint="https://models.github.ai/inference",
        credential=AzureKeyCredential(github_token),
    )

    response = client.complete(
        messages=[
            SystemMessage("You are a helpful voice assistant. Keep responses concise and conversational."),
            UserMessage(input_text),
        ],
        temperature=0.7,
        top_p=0.9,
        max_tokens=1024,
        model="deepseek/DeepSeek-V3-0324"
    )

    return response.choices[0].message.content


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
    github_token = st.sidebar.text_input("GitHub Token (DeepSeek)", type="password")

    st.title("🎤 Swar AI (Whisper Large v3 + DeepSeek)")
    st.write("Speak → Transcribe → AI Response → Voice Output 🚀")

    if groq_api_key and github_token:

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

            # 🧠 DeepSeek Response
            with st.spinner("Generating AI response..."):
                try:
                    ai_response = fetch_ai_response(github_token, transcribed_text)
                    create_text_card(ai_response, "🤖 AI Response")
                except Exception as e:
                    st.error(f"DeepSeek Error: {e}")
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
        st.warning("Please enter both API keys to continue.")


if __name__ == "__main__":
    main()