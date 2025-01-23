import streamlit as st

def page_audio(tab):
    tab.markdown("Audio")

def page_mic(tab):
    tab.markdown("Mic")

def page_video(tab):
    tab.markdown("Video")

def main():
    st.header("🎙️ Transcripts Leticia's App 🎙️", divider=True)
    st.markdown("##### Transcribe your audio, recorded and video")
    st.markdown("")

    tab_audio, tab_mic, tab_video = st.tabs(["Audio", "Recorded Voice", "Video"])
    page_audio(tab_audio)
    page_mic(tab_mic)
    page_video(tab_video)

if __name__ == "__main__":
    main()