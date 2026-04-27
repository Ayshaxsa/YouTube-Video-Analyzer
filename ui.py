import streamlit as st
from youtube_analyzer import build_yt_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered"
)

st.title("📹AI YouTube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_yt_agent()

agent = get_agent()

video_url = st.text_input("Enter YouTube Video URL: ")

button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing Video..."):
        response = agent.run(
            f"Analyze this Video: {video_url}"
        )
    st.markdown("Analysis Report of Video: ")
    st.markdown(response.content)

