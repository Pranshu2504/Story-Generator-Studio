import streamlit as st
import os

st.set_page_config(page_title="🎙️ One-Click Story Studio", layout="centered")
st.title("🎙️ One-Click Story Studio")

# Map prompt names to audio filenames
prompt_map = {
    "Storytelling Parent": "storytelling_parent.wav",
    "EdTech Creator": "edtech_creator.wav",
    "Indie Creator": "indie_creator.wav"
}

# Let user pick a category
choice = st.radio("Choose a content type:", list(prompt_map.keys()))

# Get the matching audio file
audio_path = prompt_map[choice]

# Load and play audio
if os.path.exists(audio_path):
    audio_bytes = open(audio_path, "rb").read()
    st.audio(audio_bytes, format="audio/wav")
else:
    st.error(f"Audio file not found: {audio_path}")
