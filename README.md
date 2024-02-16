# 🐬Dash Notes📝
*An AI learning support (note-taking) app*

## Background Story
When one of our learning support teachers asked me if there were any AI tools that would take notes for students, I could think of several solutions, but decided to create one myself and use this as an opportunity to test whether open-source resources (which help solve issues of privacy and cost) would be performant enough to be fit for purpose.

## An Open-Source Proof of Concept
To be clear, Dash Notes (named after our dolphin mascot at International School of Panama) is not only in beta: it is a proof of concept. It will transcribe and summarize voice recordings (such as class recordings) - but it will make you wait for it, and might very well make mistakes.

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

## Alternatives
The output could be improved (and made faster!) by using proprietary models and various paid subscriptions, but Dash Notes can be used without any API key or cost -- it is plug-and-play and free for anyone to use. All you need is a device to record the mp3 and run the code (if you use Voice Notes on an iPhone, websites such as *freeconvert.com* will convert the m4a to mp3 for you). 

I will probably create a GPT4-based version in the future, though. If you are more interested in the functionality than in the underlying experiment, many videochat note-taking apps (such as *Fathom*) can already help.

## 🤗 HuggingFace Space
You can also test Dash Notes at https://huggingface.co/spaces/jeremierostan/DashNotes - but your audio will obviosuly not be processed locally.
