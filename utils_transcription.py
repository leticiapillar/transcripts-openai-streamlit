import streamlit as st
from pathlib import Path
from moviepy import VideoFileClip
from utils_openai import audio_transcriptions

PATH_TEMP = Path(__file__).parent/"temp"
PATH_TEMP.mkdir(exist_ok=True)
FILE_AUDIO = PATH_TEMP/"audio.mp3"
FILE_VIDEO = PATH_TEMP/"video.mp3"

def audio_to_text(file, prompt):
    return audio_transcriptions(file=file,
                                prompt=prompt,
                                api_key=st.session_state["api_key"],
                                model=st.session_state["model"],
                                language=st.session_state["language"])

def video_to_text(file, prompt):
    with open(FILE_VIDEO, "wb") as f:
        f.write(file.read())
    
    moviepay_video = VideoFileClip(str(FILE_VIDEO))
    moviepay_video.audio.write_audiofile(str(FILE_AUDIO))

    with open(FILE_AUDIO, "rb") as f:
        transcription = audio_transcriptions(file=FILE_AUDIO,
                                            prompt=prompt,
                                            api_key=st.session_state["api_key"],
                                            model=st.session_state["model"],
                                            language=st.session_state["language"])
        return transcription
    return ""

def voice_to_text(file, prompt):
    return audio_transcriptions(file=file,
                                prompt=prompt,
                                api_key=st.session_state["api_key"],
                                model=st.session_state["model"],
                                language=st.session_state["language"])
