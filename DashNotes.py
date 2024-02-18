import streamlit as st
from transformers import pipeline
import whisper
import tempfile

model = whisper.load_model("tiny")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

def segment_text(text, segment_size=500):
    words = text.split()
    return [' '.join(words[i:i+segment_size]) for i in range(0, len(words), segment_size)]

def generate_summary(text):
    segments = segment_text(text)
    bullet_points = [summarizer(segment, max_length=100, min_length=5, do_sample=False)[0]['summary_text'] for segment in segments]
    return '\n'.join([f"• {point}" for point in bullet_points])

st.title('🐬Dash Notes📝')

audio_file = st.file_uploader("Upload an MP3 class recording", type=['mp3'])

if audio_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
        tmp.write(audio_file.getvalue())
        audio_path = tmp.name

    st.audio(audio_path, format='audio/mp3')

    if st.button('Transcribe'):
        transcription = transcribe_audio(audio_path)
        st.text_area("Transcription", value=transcription, height=300)
        
        summary = generate_summary(transcription)
        st.subheader("Summary")
        st.text(summary)  # Use st.text to maintain formatting
