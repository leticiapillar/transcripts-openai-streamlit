import streamlit as st
from utils_transcription import audio_to_text, video_to_text, voice_to_text

def page_audio(tab):
    input_prompt = tab.text_input("Type your prompt (optional)", key="prompt_audio")
    audio_file = tab.file_uploader("Choose your mp3 file", type=[".mp3"])
    if not audio_file is None:
        transcription_markdown(tab, audio_to_text(audio_file,input_prompt))

def page_mic(tab):
    input_prompt = tab.text_input("Type your prompt (optional)", key="prompt_mic")
    audio_value = tab.audio_input("Record a voice message")
    if audio_value:
        tab.audio(audio_value)
        transcription_markdown(tab, voice_to_text(audio_value,input_prompt))

def page_video(tab):
    input_prompt = tab.text_input("Type your prompt (optional)", key="prompt_video")
    video_file = tab.file_uploader("Choose your mp4 file", type=[".mp4"])
    if not video_file is None:
        transcription_markdown(tab, video_to_text(video_file, input_prompt))

def transcription_markdown(tab, text):
    tab.markdown("")
    tab.markdown("**Transcription:**")
    tab.markdown(text)


def main():
    st.header("🎙️ Transcripts Leticia's App 🎙️", divider=True)
    st.markdown("##### Transcribe your audio, recorded voice, and video")
    st.markdown("")

    tab_audio, tab_mic, tab_video = st.tabs(["Audio", "Recorded Voice", "Video"])
    
    with tab_audio:
        page_audio(tab_audio)
    with tab_mic:
        page_mic(tab_mic)
    with tab_video:
        page_video(tab_video)

if __name__ == "__main__":
    main()