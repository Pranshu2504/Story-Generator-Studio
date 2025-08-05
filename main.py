from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Map prompt names to audio files
audio_map = {
    "storytelling_parent": "storytelling_parent.wav",
    "edtech_creator": "edtech_creator.wav",
    "indie_creator": "indie_creator.wav"
}

@app.get("/")
def root():
    return {"message": "One-Click Story Studio API is live!"}

@app.get("/audio/{prompt_name}")
def get_audio(prompt_name: str):
    filename = audio_map.get(prompt_name.lower())
    if filename and os.path.exists(filename):
        return FileResponse(filename, media_type="audio/wav")
    raise HTTPException(status_code=404, detail="Audio not found")
