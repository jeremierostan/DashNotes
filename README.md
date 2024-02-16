# 🐬Dash Notes📝
An AI learning support (note-taking) app brought to you by International School of Panama


## Background Story
When one of our learning support teachers asked me if there were any AI tools that would take notes for students, I could think of several options, but decided to create one myself - not only to use this as a learning opportunity, but also for obvious privacy reasons.

## An Open-Source Proof of Concept
To be clear, Dash Notes (named after our dolphin mascot at International School of Panama) is not only in beta: it is a proof of concept. It will transcribe and summarize class recordings for you and your students - but it will make you wait for it, and might very well make mistakes.

Dash Notes should thus be used with caution. This app is the first to come out of our nascent AI Lab here at ISP, and inherent to this experiment was the idea of testing the viabilty of using 100% open-source resources. The output could be improved by using the most performant models, but Dash Notes can be used without any APY key or cost -- it is plug-and-play and free for anyone to use.

## Transcription and Summarization Tasks
The transcription is operated through OpenAI Whisper, an automatic speech recognition system designed to convert spoken language into written text. Made available as an open-source project, Whisper is free to use. Running Dash Notes locally also means that your audio (voice recording) will be processed on your computer, and not shared with anyone.

The summarization is performed with the facebook/bart-large-cnn model, a bidirectional and auto-regressive transformer specifically designed for this task (the model was fine-tuned on a dataset of CNN news articles and their corresponding highlights). 

## Running Dash Notes locally:

To run Dash Notes locally:
1) Download a free code editor
2) Download Python
3) Open DashNotes.py
4) Create a virtual environment (optional)
5) Install streamlit, transformers, and whisper:
   
```
pip install streamlit
pip install transformers
pip install whisper
```

6) Run the app:

```
streamlit run DashNotes.py
```
