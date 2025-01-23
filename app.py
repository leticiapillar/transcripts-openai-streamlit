import streamlit as st
from utils_openai import audio_transcriptions

def page_audio(tab):
    input_prompt = tab.text_input("Type your prompt (optional)", key="input_prompt")
    audio_file = tab.file_uploader("Choose your mp3 file", type=[".mp3"])
    if not audio_file is None:
        transcription = audio_transcriptions(file=audio_file,
                                            prompt=input_prompt,
                                            language="pt")
        tab.markdown("")
        tab.markdown("**Transcription:**")
        tab.markdown(transcription)

def page_mic(tab):
    tab.markdown("Mic")

def page_video(tab):
    tab.markdown("Video")

def main():
    st.header("🎙️ Transcripts Leticia's App 🎙️", divider=True)
    st.markdown("##### Transcribe your audio, recorded voice, and video")
    st.markdown("")

    tab_audio, tab_mic, tab_video = st.tabs(["Audio", "Recorded Voice", "Video"])
    page_audio(tab_audio)
    page_mic(tab_mic)
    page_video(tab_video)

if __name__ == "__main__":
    main()