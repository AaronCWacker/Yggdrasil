In my app.py below I am saving a .md file three times for one input.  I would like instead to save it once at the end with each of the three different result sets together as a single md file.  I would also like to add a new feature that lists each paper with abstract and pdf link at the end and for each provide the summary as a textbox input with key autonamed by paper, and then with the paper add a buttont for each that says "Generate app.py" which if clicked generates a gradio app.py with a new call to claude for each paper which asks to create an app.py application that implements what is stated in the paper and summary.  Save the md before this new feature and with the new feature also randomize which TTS voice is used and then pick one and at end of the app.py creation with the claude call add the keyword list to a new file name with the keywords from each paper shortening it to 1/2 of max file length for windows.  With the app.py that is generated, have a button labeled Run that can run the app.py with my code which I will add.  for now just make a function for it with variables for inputs.   import streamlit as st
import anthropic
import openai
import base64
import cv2
import glob
import json
import math
import os
import pytz
import random
import re
import requests
#import textract
import time
import zipfile
import plotly.graph_objects as go
import streamlit.components.v1 as components
from datetime import datetime
from audio_recorder_streamlit import audio_recorder
from bs4 import BeautifulSoup
from collections import defaultdict, deque, Counter
from dotenv import load_dotenv
from gradio_client import Client
from huggingface_hub import InferenceClient
from io import BytesIO
from PIL import Image
from PyPDF2 import PdfReader
from urllib.parse import quote
from xml.etree import ElementTree as ET
from openai import OpenAI
import extra_streamlit_components as stx
from streamlit.runtime.scriptrunner import get_script_run_ctx
import asyncio
import edge_tts
from streamlit_marquee import streamlit_marquee
from typing import Tuple, Optional
import pandas as pd

# Patch the asyncio event loop to allow nested use of asyncio.run()
import nest_asyncio
nest_asyncio.apply()

# ─────────────────────────────────────────────────────────
# 1. CORE CONFIGURATION & SETUP
# ─────────────────────────────────────────────────────────

st.set_page_config(
    page_title="🚲TalkingAIResearcher🏆",
    page_icon="🚲🏆",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://huggingface.co/awacke1',
        'Report a bug': 'https://huggingface.co/spaces/awacke1',
        'About': "🚲TalkingAIResearcher🏆"
    }
)
load_dotenv()

# ▶ Available English voices for Edge TTS
EDGE_TTS_VOICES = [
    "en-US-AriaNeural",
    "en-US-GuyNeural",
    "en-US-JennyNeural",
    "en-GB-SoniaNeural",
    "en-GB-RyanNeural",
    "en-AU-NatashaNeural",
    "en-AU-WilliamNeural",
    "en-CA-ClaraNeural",
    "en-CA-LiamNeural"
]

# ▶ Initialize Session State
if 'marquee_settings' not in st.session_state:
    st.session_state['marquee_settings'] = {
        "background": "#1E1E1E",
        "color": "#FFFFFF",
        "font-size": "14px",
        "animationDuration": "20s",
        "width": "100%",
        "lineHeight": "35px"
    }
if 'tts_voice' not in st.session_state:
    st.session_state['tts_voice'] = EDGE_TTS_VOICES[0]
if 'audio_format' not in st.session_state:
    st.session_state['audio_format'] = 'mp3'
if 'transcript_history' not in st.session_state:
    st.session_state['transcript_history'] = []
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = "gpt-4o-2024-05-13"
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'last_voice_input' not in st.session_state:
    st.session_state['last_voice_input'] = ""
if 'editing_file' not in st.session_state:
    st.session_state['editing_file'] = None
if 'edit_new_name' not in st.session_state:
    st.session_state['edit_new_name'] = ""
if 'edit_new_content' not in st.session_state:
    st.session_state['edit_new_content'] = ""
if 'viewing_prefix' not in st.session_state:
    st.session_state['viewing_prefix'] = None
if 'should_rerun' not in st.session_state:
    st.session_state['should_rerun'] = False
if 'old_val' not in st.session_state:
    st.session_state['old_val'] = None
if 'last_query' not in st.session_state:
    st.session_state['last_query'] = ""
if 'marquee_content' not in st.session_state:
    st.session_state['marquee_content'] = "🚀 Welcome to TalkingAIResearcher | 🤖 Your Research Assistant"

# ▶ Additional keys for performance, caching, etc.
if 'audio_cache' not in st.session_state:
    st.session_state['audio_cache'] = {}
if 'download_link_cache' not in st.session_state:
    st.session_state['download_link_cache'] = {}
if 'operation_timings' not in st.session_state:
    st.session_state['operation_timings'] = {}
if 'performance_metrics' not in st.session_state:
    st.session_state['performance_metrics'] = defaultdict(list)
if 'enable_audio' not in st.session_state:
    st.session_state['enable_audio'] = True  # Turn TTS on/off

# ▶ API Keys
openai_api_key = os.getenv('OPENAI_API_KEY', "")
anthropic_key = os.getenv('ANTHROPIC_API_KEY_3', "")
xai_key = os.getenv('xai',"")
if 'OPENAI_API_KEY' in st.secrets:
    openai_api_key = st.secrets['OPENAI_API_KEY']
if 'ANTHROPIC_API_KEY' in st.secrets:
    anthropic_key = st.secrets["ANTHROPIC_API_KEY"]

openai.api_key = openai_api_key
openai_client = OpenAI(api_key=openai.api_key, organization=os.getenv('OPENAI_ORG_ID'))
HF_KEY = os.getenv('HF_KEY')
API_URL = os.getenv('API_URL')

# ▶ Helper constants
FILE_EMOJIS = {
    "md": "📝",
    "mp3": "🎵",
    "wav": "🔊"
}

# ─────────────────────────────────────────────────────────
# 2. PERFORMANCE MONITORING & TIMING
# ─────────────────────────────────────────────────────────

class PerformanceTimer:
    """
    ⏱️ A context manager for timing operations with automatic logging.
    Usage:
        with PerformanceTimer("my_operation"):
            # do something
    The duration is stored into `st.session_state['operation_timings']`
    and appended to the `performance_metrics` list.
    """
    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.start_time = None
        
    def __enter__(self):
        self.start_time = time.time()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:  # Only log if no exception occurred
            duration = time.time() - self.start_time
            st.session_state['operation_timings'][self.operation_name] = duration
            st.session_state['performance_metrics'][self.operation_name].append(duration)

def log_performance_metrics():
    """
    📈 Display performance metrics in the sidebar, including a timing breakdown
    and a small bar chart of average times.
    """
    st.sidebar.markdown("### ⏱️ Performance Metrics")
    
    metrics = st.session_state['operation_timings']
    if metrics:
        total_time = sum(metrics.values())
        st.sidebar.write(f"**Total Processing Time:** {total_time:.2f}s")
        
        # Break down each operation time
        for operation, duration in metrics.items():
            percentage = (duration / total_time) * 100
            st.sidebar.write(f"**{operation}:** {duration:.2f}s ({percentage:.1f}%)")
            
        # Show timing history chart
        history_data = []
        for op, times in st.session_state['performance_metrics'].items():
            if times:  # Only if we have data
                avg_time = sum(times) / len(times)
                history_data.append({"Operation": op, "Avg Time (s)": avg_time})
        
        if history_data:
            st.sidebar.markdown("### 📊 Timing History (Avg)")
            chart_data = pd.DataFrame(history_data)
            st.sidebar.bar_chart(chart_data.set_index("Operation"))

# ─────────────────────────────────────────────────────────
# 3. HELPER FUNCTIONS (FILENAMES, LINKS, MARQUEE, ETC.)
# ─────────────────────────────────────────────────────────

def get_central_time():
    """🌎 Get current time in US Central timezone."""
    central = pytz.timezone('US/Central')
    return datetime.now(central)

def format_timestamp_prefix():
    """📅 Generate a timestamp prefix"""
    ct = get_central_time()
    return ct.strftime("%Y%m%d_%H%M%S")

def initialize_marquee_settings():
    """🌈 Initialize marquee defaults if needed."""
    if 'marquee_settings' not in st.session_state:
        st.session_state['marquee_settings'] = {
            "background": "#1E1E1E",
            "color": "#FFFFFF",
            "font-size": "14px",
            "animationDuration": "20s",
            "width": "100%",
            "lineHeight": "35px"
        }

def get_marquee_settings():
    """🔧 Retrieve marquee settings from session."""
    initialize_marquee_settings()
    return st.session_state['marquee_settings']

def update_marquee_settings_ui():
    """🖌 Add color pickers & sliders for marquee config in the sidebar."""
    st.sidebar.markdown("### 🎯 Marquee Settings")
    cols = st.sidebar.columns(2)
    with cols[0]:
        bg_color = st.color_picker("🎨 Background", 
                                  st.session_state['marquee_settings']["background"], 
                                  key="bg_color_picker")
        text_color = st.color_picker("✍️ Text", 
                                    st.session_state['marquee_settings']["color"], 
                                    key="text_color_picker")
    with cols[1]:
        font_size = st.slider("📏 Size", 10, 24, 14, key="font_size_slider")
        duration = st.slider("⏱️ Speed (secs)", 1, 20, 20, key="duration_slider")

    st.session_state['marquee_settings'].update({
        "background": bg_color,
        "color": text_color,
        "font-size": f"{font_size}px",
        "animationDuration": f"{duration}s"
    })

def display_marquee(text, settings, key_suffix=""):
    """
    🎉 Show a marquee text with style from the marquee settings.
    Automatically truncates text to ~280 chars to avoid overflow.
    """
    truncated_text = text[:280] + "..." if len(text) > 280 else text
    streamlit_marquee(
        content=truncated_text,
        **settings,
        key=f"marquee_{key_suffix}"
    )
    st.write("")

def get_high_info_terms(text: str, top_n=10) -> list:
    """
    📌 Extract top_n frequent words & bigrams (excluding common stopwords).
    Useful for generating short descriptive keywords from Q/A content.
    """
    stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with'])
    words = re.findall(r'\b\w+(?:-\w+)*\b', text.lower())
    bi_grams = [' '.join(pair) for pair in zip(words, words[1:])]
    combined = words + bi_grams
    filtered = [term for term in combined if term not in stop_words and len(term.split()) <= 2]
    counter = Counter(filtered)
    return [term for term, freq in counter.most_common(top_n)]

def clean_text_for_filename(text: str) -> str:
    """
    🏷️ Remove special chars & short unhelpful words from text for safer filenames.
    Returns a lowercased, underscore-joined token string.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    words = text.split()
    stop_short = set(['the', 'and', 'for', 'with', 'this', 'that', 'ai', 'library'])
    filtered = [w for w in words if len(w) > 3 and w not in stop_short]
    return '_'.join(filtered)[:200]

def generate_filename(prompt, response, file_type="md", max_length=200):
    """
    📁 Create a shortened filename based on prompt+response content:
      1) Extract top info terms,
      2) Combine snippet from prompt+response,
      3) Remove duplicates,
      4) Append word counts and estimated duration tokens,
      5) Truncate if needed.
    """
    prefix = format_timestamp_prefix() + "_"
    combined_text = (prompt + " " + response)[:200]
    info_terms = get_high_info_terms(combined_text, top_n=5)
    snippet = (prompt[:40] + " " + response[:40]).strip()
    snippet_cleaned = clean_text_for_filename(snippet)
    
    # Remove duplicates
    name_parts = info_terms + [snippet_cleaned]
    seen = set()
    unique_parts = []
    for part in name_parts:
        if part not in seen:
            seen.add(part)
            unique_parts.append(part)
    
    # NEW: Compute word counts for title (prompt) and summary (response) and estimated duration
    wct = len(prompt.split())
    sw = len(response.split())
    # Estimated duration (seconds) assuming a reading speed of 2.5 words per second
    estimated_duration = round((wct + sw) / 2.5)
    
    base_name = '_'.join(unique_parts).strip('_')
    # NEW: Append new tokens for word counts and duration
    extra_tokens = f"_wct{wct}_sw{sw}_dur{estimated_duration}"
    leftover_chars = max_length - len(prefix) - len(file_type) - 1
    if len(base_name) + len(extra_tokens) > leftover_chars:
        base_name = base_name[:leftover_chars - len(extra_tokens)]
    full_name = base_name + extra_tokens
    
    return f"{prefix}{full_name}.{file_type}"

def create_file(prompt, response, file_type="md"):
    """
    📝 Create a text file from prompt + response with a sanitized filename.
    Returns the created filename.
    """
    filename = generate_filename(prompt.strip(), response.strip(), file_type)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(prompt + "\n\n" + response)
    return filename

def get_download_link(file, file_type="zip"):
    """
    Convert a file to base64 and return an HTML link for download.
    """
    with open(file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    if file_type == "zip":
        return f'<a href="data:application/zip;base64,{b64}" download="{os.path.basename(file)}">📂 Download {os.path.basename(file)}</a>'
    elif file_type == "mp3":
        return f'<a href="data:audio/mpeg;base64,{b64}" download="{os.path.basename(file)}">🎵 Download {os.path.basename(file)}</a>'
    elif file_type == "wav":
        return f'<a href="data:audio/wav;base64,{b64}" download="{os.path.basename(file)}">🔊 Download {os.path.basename(file)}</a>'
    elif file_type == "md":
        return f'<a href="data:text/markdown;base64,{b64}" download="{os.path.basename(file)}">📝 Download {os.path.basename(file)}</a>'
    else:
        return f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.basename(file)}">Download {os.path.basename(file)}</a>'

def clean_for_speech(text: str) -> str:
    """Clean up text for TTS output."""
    text = text.replace("\n", " ")
    text = text.replace("</s>", " ")
    text = text.replace("#", "")
    text = re.sub(r"\(https?:\/\/[^\)]+\)", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# ─────────────────────────────────────────────────────────
# 5 MINUTE RESEARCH PAPER FEATURE (NEW CODE) 🚀📚
# ─────────────────────────────────────────────────────────

def generate_pdf_link(url: str) -> str:
    """
    🔗 Generate PDF link from abstract URL by replacing 'abs' with 'pdf' and appending .pdf if needed.
    """
    if "abs" in url:
        pdf_url = url.replace("abs", "pdf")
        if not pdf_url.endswith(".pdf"):
            pdf_url += ".pdf"
        return pdf_url
    return url

def generate_5min_feature_markdown(paper: dict) -> str:
    """
    ✨ Generate detailed markdown for a paper including:
        - Word count for title and summary
        - High info words list (up to 15 terms)
        - PDF link (derived from abstract URL)
        - A pseudo ROUGE score
        - A mermaid graph code block for the 15 concepts
    """
    title = paper.get('title', '')
    summary = paper.get('summary', '')
    authors = paper.get('authors', '')
    date = paper.get('date', '')
    url = paper.get('url', '')
    pdf_link = generate_pdf_link(url)
    title_wc = len(title.split())
    summary_wc = len(summary.split())
    high_info_terms = get_high_info_terms(summary, top_n=15)
    terms_str = ", ".join(high_info_terms)
    # Compute a pseudo ROUGE score as percentage of high info terms to summary words
    rouge_score = round((len(high_info_terms) / max(len(summary.split()), 1)) * 100, 2)
    
    # Generate mermaid graph code block connecting terms sequentially
    mermaid_code = "```mermaid\nflowchart TD\n"
    for i in range(len(high_info_terms) - 1):
        mermaid_code += f'    T{i+1}["{high_info_terms[i]}"] --> T{i+2}["{high_info_terms[i+1]}"]\n'
    mermaid_code += "```"
    
    md = f"""
## 📄 {title}

**Authors:** {authors}  
**Date:** {date}  
**Word Count (Title):** {title_wc} | **Word Count (Summary):** {summary_wc}  

**Links:** [Abstract]({url}) | [PDF]({pdf_link})

**High Info Terms:** {terms_str}  
**ROUGE Score:** {rouge_score}%

### 🎤 TTF Read Aloud
- **Title:** {title}
- **Key Terms:** {terms_str}
- **ROUGE:** {rouge_score}%

#### Mermaid Graph of Key Concepts
{mermaid_code}

---
"""
    return md

def create_detailed_paper_md(papers: list) -> str:
    """
    📝 Create a detailed markdown string for all papers including 5 minute research paper features.
    """
    md_parts = ["# Detailed Research Paper Summary\n"]
    for idx, paper in enumerate(papers, start=1):
        md_parts.append(generate_5min_feature_markdown(paper))
    return "\n".join(md_parts)

# ─────────────────────────────────────────────────────────
# 4. OPTIMIZED AUDIO GENERATION (ASYNC TTS + CACHING)
# ─────────────────────────────────────────────────────────

def clean_for_speech(text: str) -> str:
    """
    🔉 Clean up text for TTS output with enhanced cleaning.
    Removes markdown, code blocks, links, etc.
    """
    with PerformanceTimer("text_cleaning"):
        # Remove markdown headers
        text = re.sub(r'#+ ', '', text)
        # Remove link formats [text](url)
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        # Remove emphasis markers (*, _, ~, `)
        text = re.sub(r'[*_~`]', '', text)
        # Remove code blocks
        text = re.sub(r'```[\s\S]*?```', '', text)
        text = re.sub(r'`[^`]*`', '', text)
        # Remove excess whitespace
        text = re.sub(r'\s+', ' ', text).replace("\n", " ")
        # Remove hidden S tokens
        text = text.replace("</s>", " ")
        # Remove URLs
        text = re.sub(r'https?://\S+', '', text)
        text = re.sub(r'\(https?://[^\)]+\)', '', text)
        text = text.strip()
        return text

async def async_edge_tts_generate(
    text: str,
    voice: str,
    rate: int = 0,
    pitch: int = 0,
    file_format: str = "mp3"
) -> Tuple[Optional[str], float]:
    """
    🎶 Asynchronous TTS generation with caching and performance tracking.
    Returns (filename, generation_time).
    """
    with PerformanceTimer("tts_generation") as timer:
        # ▶ Clean & validate text
        text = clean_for_speech(text)
        if not text.strip():
            return None, 0
        
        # ▶ Check cache (avoid regenerating the same TTS)
        cache_key = f"{text[:100]}_{voice}_{rate}_{pitch}_{file_format}"
        if cache_key in st.session_state['audio_cache']:
            return st.session_state['audio_cache'][cache_key], 0
        
        try:
            # ▶ Generate audio
            rate_str = f"{rate:+d}%"
            pitch_str = f"{pitch:+d}Hz"
            communicate = edge_tts.Communicate(text, voice, rate=rate_str, pitch=pitch_str)
            
            # ▶ Generate unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"audio_{timestamp}_{random.randint(1000, 9999)}.{file_format}"
            
            # ▶ Save audio file
            await communicate.save(filename)
            
            # ▶ Store in cache
            st.session_state['audio_cache'][cache_key] = filename
            
            # ▶ Return path + timing
            return filename, time.time() - timer.start_time
        
        except Exception as e:
            st.error(f"❌ Error generating audio: {str(e)}")
            return None, 0

# NEW: Define speak_with_edge_tts using our async function and return only the filename
def speak_with_edge_tts(text, voice="en-US-AriaNeural", rate=0, pitch=0, file_format="mp3"):
    """Wrapper for the async TTS generate call. Returns only the filename."""
    result = asyncio.run(async_edge_tts_generate(text, voice, rate, pitch, file_format))
    if isinstance(result, tuple):
        return result[0]
    return result

async def async_save_qa_with_audio(
    question: str,
    answer: str,
    voice: Optional[str] = None
) -> Tuple[str, Optional[str], float, float]:
    """
    📝 Asynchronously save Q&A to markdown, then generate audio if enabled.
    Returns (md_file, audio_file, md_time, audio_time).
    """
    voice = voice or st.session_state['tts_voice']
    
    with PerformanceTimer("qa_save") as timer:
        # ▶ Save Q/A as markdown
        md_start = time.time()
        md_file = create_file(question, answer, "md")
        md_time = time.time() - md_start
        
        # ▶ Generate audio (if globally enabled)
        audio_file = None
        audio_time = 0
        if st.session_state['enable_audio']:
            audio_text = f"{question}\n\nAnswer: {answer}"
            audio_file, audio_time = await async_edge_tts_generate(
                audio_text,
                voice=voice,
                file_format=st.session_state['audio_format']
            )
        
        return md_file, audio_file, md_time, audio_time

def save_qa_with_audio(question, answer, voice=None):
    """Save Q&A to markdown and also generate audio."""
    if not voice:
        voice = st.session_state['tts_voice']
    
    combined_text = f"# Question\n{question}\n\n# Answer\n{answer}"
    md_file = create_file(question, answer, "md")
    audio_text = f"{question}\n\nAnswer: {answer}"
    audio_file = speak_with_edge_tts(
        audio_text,
        voice=voice,
        file_format=st.session_state['audio_format']
    )
    return md_file, audio_file

def create_download_link_with_cache(file_path: str, file_type: str = "mp3") -> str:
    """
    ⬇️ Create a download link for a file with caching & error handling.
    """
    with PerformanceTimer("download_link_generation"):
        cache_key = f"dl_{file_path}"
        if cache_key in st.session_state['download_link_cache']:
            return st.session_state['download_link_cache'][cache_key]
        
        try:
            with open(file_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            filename = os.path.basename(file_path)
            
            if file_type == "mp3":
                link = f'<a href="data:audio/mpeg;base64,{b64}" download="{filename}">🎵 Download {filename}</a>'
            elif file_type == "wav":
                link = f'<a href="data:audio/wav;base64,{b64}" download="{filename}">🔊 Download {filename}</a>'
            elif file_type == "md":
                link = f'<a href="data:text/markdown;base64,{b64}" download="{filename}">📝 Download {filename}</a>'
            else:
                link = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">⬇️ Download {filename}</a>'
            
            st.session_state['download_link_cache'][cache_key] = link
            return link
        
        except Exception as e:
            st.error(f"❌ Error creating download link: {str(e)}")
            return ""

# NEW: Define play_and_download_audio to play audio and provide a download link.
def play_and_download_audio(file_path, file_type="mp3"):
    """Streamlit audio + a quick download link."""
    if file_path and isinstance(file_path, str) and os.path.exists(file_path):
        st.audio(file_path)
        dl_link = get_download_link(file_path, file_type=file_type)
        st.markdown(dl_link, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# 5. RESEARCH / ARXIV FUNCTIONS
# ─────────────────────────────────────────────────────────

def parse_arxiv_refs(ref_text: str):
    """
    📜 Given a multi-line markdown with Arxiv references,
    parse them into a list of dicts: {date, title, url, authors, summary}.
    """
    if not ref_text:
        return []
    results = []
    current_paper = {}
    lines = ref_text.split('\n')
    
    for i, line in enumerate(lines):
        if line.count('|') == 2:
            # Found a new paper line
            if current_paper:
                results.append(current_paper)
                if len(results) >= 20:
                    break
            try:
                header_parts = line.strip('* ').split('|')
                date = header_parts[0].strip()
                title = header_parts[1].strip()
                url_match = re.search(r'(https://arxiv.org/\S+)', line)
                url = url_match.group(1) if url_match else f"paper_{len(results)}"
                
                current_paper = {
                    'date': date,
                    'title': title,
                    'url': url,
                    'authors': '',
                    'summary': '',
                    'full_audio': None,
                    'download_base64': '',
                }
            except Exception as e:
                st.warning(f"⚠️ Error parsing paper header: {str(e)}")
                current_paper = {}
                continue
        elif current_paper:
            # If authors not set, fill it; otherwise, fill summary
            if not current_paper['authors']:
                current_paper['authors'] = line.strip('* ')
            else:
                if current_paper['summary']:
                    current_paper['summary'] += ' ' + line.strip()
                else:
                    current_paper['summary'] = line.strip()
    
    if current_paper:
        results.append(current_paper)
    
    return results[:20]

def create_paper_links_md(papers):
    """
    🔗 Create a minimal .md content linking to each paper's Arxiv URL.
    """
    lines = ["# Paper Links\n"]
    for i, p in enumerate(papers, start=1):
        lines.append(f"{i}. **{p['title']}** — [Arxiv Link]({p['url']})")
    return "\n".join(lines)

async def create_paper_audio_files(papers, input_question):
    """
    🎧 For each paper, generate TTS audio summary and store the path in `paper['full_audio']`.
    Also creates a base64 download link in `paper['download_base64']`.
    """
    for paper in papers:
        try:
            audio_text = f"{paper['title']} by {paper['authors']}. {paper['summary']}"
            audio_text = clean_for_speech(audio_text)
            file_format = st.session_state['audio_format']
            audio_file, _ = await async_edge_tts_generate(
                audio_text, 
                voice=st.session_state['tts_voice'], 
                file_format=file_format
            )
            paper['full_audio'] = audio_file
            
            if audio_file:
                # Convert to base64 link
                ext = file_format
                download_link = create_download_link_with_cache(audio_file, file_type=ext)
                paper['download_base64'] = download_link

        except Exception as e:
            st.warning(f"⚠️ Error processing paper {paper['title']}: {str(e)}")
            paper['full_audio'] = None
            paper['download_base64'] = ''

def display_papers(papers, marquee_settings):
    """
    📑 Display paper info in the main area with marquee + expanders + audio.
    """
    st.write("## 🔎 Research Papers")
    for i, paper in enumerate(papers, start=1):
        marquee_text = f"📄 {paper['title']} | 👤 {paper['authors'][:120]} | 📝 {paper['summary'][:200]}"
        display_marquee(marquee_text, marquee_settings, key_suffix=f"paper_{i}")
        
        with st.expander(f"{i}. 📄 {paper['title']}", expanded=True):
            st.markdown(f"**{paper['date']} | {paper['title']}** — [Arxiv Link]({paper['url']})")
            # NEW: Add PDF link next to abstract link
            pdf_link = generate_pdf_link(paper['url'])
            st.markdown(f"**PDF Link:** [PDF]({pdf_link})")
            st.markdown(f"*Authors:* {paper['authors']}")
            st.markdown(paper['summary'])
            # NEW: Append detailed 5min feature markdown for this paper
            st.markdown(generate_5min_feature_markdown(paper))
            if paper.get('full_audio'):
                st.write("📚 **Paper Audio**")
                st.audio(paper['full_audio'])
                if paper['download_base64']:
                    st.markdown(paper['download_base64'], unsafe_allow_html=True)

def display_papers_in_sidebar(papers):
    """
    🔎 Mirrors the paper listing in the sidebar with expanders, audio, etc.
    """
    st.sidebar.title("🎶 Papers & Audio")
    for i, paper in enumerate(papers, start=1):
        with st.sidebar.expander(f"{i}. {paper['title']}"):
            st.markdown(f"**Arxiv:** [Link]({paper['url']})")
            # NEW: Add PDF link in sidebar as well
            pdf_link = generate_pdf_link(paper['url'])
            st.markdown(f"**PDF:** [PDF]({pdf_link})")
            if paper['full_audio']:
                st.audio(paper['full_audio'])
                if paper['download_base64']:
                    st.markdown(paper['download_base64'], unsafe_allow_html=True)
            st.markdown(f"**Authors:** {paper['authors']}")
            if paper['summary']:
                st.markdown(f"**Summary:** {paper['summary'][:300]}...")
            # NEW: Show 5min feature summary in sidebar expander
            st.markdown(generate_5min_feature_markdown(paper))

# ─────────────────────────────────────────────────────────
# 6. ZIP FUNCTION
# ─────────────────────────────────────────────────────────

def create_zip_of_files(md_files, mp3_files, wav_files, input_question):
    """
    📦 Zip up all relevant files, generating a short name from high-info terms.
    Returns the zip filename if created, else None.
    """
    md_files = [f for f in md_files if os.path.basename(f).lower() != 'readme.md']
    all_files = md_files + mp3_files + wav_files
    if not all_files:
        return None

    all_content = []
    for f in all_files:
        if f.endswith('.md'):
            with open(f, "r", encoding='utf-8') as file:
                all_content.append(file.read())
        elif f.endswith('.mp3') or f.endswith('.wav'):
            basename = os.path.splitext(os.path.basename(f))[0]
            words = basename.replace('_', ' ')
            all_content.append(words)
    
    all_content.append(input_question)
    combined_content = " ".join(all_content)
    info_terms = get_high_info_terms(combined_content, top_n=10)
    
    timestamp = format_timestamp_prefix()
    name_text = '-'.join(term for term in info_terms[:5])  
    short_zip_name = (timestamp + "_" + name_text)[:20] + ".zip"

    with zipfile.ZipFile(short_zip_name, 'w') as z:
        for f in all_files:
            z.write(f)
    return short_zip_name

# ─────────────────────────────────────────────────────────
# 7. MAIN AI LOGIC: LOOKUP & TAB HANDLERS
# ─────────────────────────────────────────────────────────

def perform_ai_lookup(q, vocal_summary=True, extended_refs=False, 
                     titles_summary=True, full_audio=False, useArxiv=True, useArxivAudio=False):
    """Main routine that uses Anthropic (Claude) + Gradio ArXiv RAG pipeline."""
    start = time.time()
    ai_constitution = """
    You are a medical and machine learning review board expert and streamlit python and html5 expert. You are tasked with creating a streamlit app.py and requirements.txt for a solution that answers the questions with a working app to demonstrate. You are to use the paper list below to answer the question thinking through step by step how to create a streamlit app.py and requirements.txt for the solution that answers the questions with a working app to demonstrate.
    """

    # --- 1) Claude API
    client = anthropic.Anthropic(api_key=anthropic_key)
    user_input = q
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": user_input}
        ])
    st.write("Claude's reply 🧠:")
    st.markdown(response.content[0].text)

    # Save & produce audio
    result = response.content[0].text
    create_file(q, result) 
    md_file, audio_file = save_qa_with_audio(q, result)
    st.subheader("📝 Main Response Audio")
    play_and_download_audio(audio_file, st.session_state['audio_format'])

    if useArxiv:
        q = q + result   # Feed Arxiv the question and Claude's answer for prompt fortification to get better answers and references
        # --- 2) Arxiv RAG
        st.write('Running Arxiv RAG with Claude inputs.')
        client = Client("awacke1/Arxiv-Paper-Search-And-QA-RAG-Pattern")
        refs = client.predict(
            q, 
            10, 
            "Semantic Search", 
            "mistralai/Mixtral-8x7B-Instruct-v0.1",
            api_name="/update_with_rag_md"
        )[0]
        
        result = f"🔎 {q}\n\n{refs}"  # use original question q with result paired with paper references for best prompt fortification
        
        md_file, audio_file = save_qa_with_audio(q, result)
        st.subheader("📝 Main Response Audio")
        play_and_download_audio(audio_file, st.session_state['audio_format'])

        # --- 3) Parse + handle papers
        papers = parse_arxiv_refs(refs)
        if papers:
            # Create minimal links page first
            paper_links = create_paper_links_md(papers)
            links_file = create_file(q, paper_links, "md")
            st.markdown(paper_links)

            # NEW: Create detailed markdown with 5 minute research paper features
            detailed_md = create_detailed_paper_md(papers)
            detailed_file = create_file(q, detailed_md, "md")
            st.markdown(detailed_md)

            # Then create audio for each paper if desired
            if useArxivAudio:
                asyncio.run(create_paper_audio_files(papers, input_question=q))

            display_papers(papers, get_marquee_settings())  # scrolling marquee per paper and summary
            display_papers_in_sidebar(papers)  # sidebar entry per paper and summary
        else:
            st.warning("No papers found in the response.")

        # --- 4) Claude API with arxiv list of papers to app.py
        client = anthropic.Anthropic(api_key=anthropic_key)
        user_input = q + '\n\n' + 'Use the reference papers below to answer the question by creating a python streamlit app.py and requirements.txt with python libraries for creating a single app.py application that answers the questions with working code to demonstrate.'+ '\n\n'
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": user_input}
            ])
        r2 = response.content[0].text
        st.write("Claude's reply 🧠:")
        st.markdown(r2)
        
    elapsed = time.time() - start
    st.write(f"**Total Elapsed:** {elapsed:.2f} s")
    return result

def perform_ai_lookup_old(
    q,
    vocal_summary=True,
    extended_refs=False,
    titles_summary=True,
    full_audio=False
):
    """
    🔮 Main routine that uses Anthropic (Claude) + optional Gradio ArXiv RAG pipeline.
    Currently demonstrates calling Anthropic and returning the text.
    """
    with PerformanceTimer("ai_lookup"):
        start = time.time()
        
        # ▶ Example call to Anthropic (Claude)
        client = anthropic.Anthropic(api_key=anthropic_key)
        user_input = q
        
        # Here we do a minimal prompt, just to show the call
        # (You can enhance your prompt engineering as needed)
        response = client.completions.create(
            model="claude-2",
            max_tokens_to_sample=512,
            prompt=f"{anthropic.HUMAN_PROMPT} {user_input}{anthropic.AI_PROMPT}"
        )
        
        result_text = response.completion.strip()
        
        # ▶ Print and store
        st.write("### Claude's reply 🧠:")
        st.markdown(result_text)
        
        # ▶ We'll add to the chat history
        st.session_state.chat_history.append({"user": q, "claude": result_text})
        
        # ▶ Return final text
        end = time.time()
        st.write(f"**Elapsed:** {end - start:.2f}s")

    return result_text

async def process_voice_input(text):
    """
    🎤 When user sends a voice query, we run the AI lookup + Q/A with audio.
    Then we store the resulting markdown & audio in session or disk.
    """
    if not text:
        return
    st.subheader("🔍 Search Results")
    
    # ▶ Call AI
    result = perform_ai_lookup(
        text, 
        vocal_summary=True,
        extended_refs=False,
        titles_summary=True,
        full_audio=True
    )
    
    # ▶ Save Q&A as Markdown + audio (async)
    md_file, audio_file, md_time, audio_time = await async_save_qa_with_audio(text, result)

    st.subheader("📝 Generated Files")
    st.write(f"**Markdown:** {md_file} (saved in {md_time:.2f}s)")
    if audio_file:
        st.write(f"**Audio:** {audio_file} (generated in {audio_time:.2f}s)")
        st.audio(audio_file)
        dl_link = create_download_link_with_cache(audio_file, file_type=st.session_state['audio_format'])
        st.markdown(dl_link, unsafe_allow_html=True)

def display_voice_tab():
    """
    🎙️ Display the voice input tab with TTS settings and real-time usage.
    """
    
    # ▶ Voice Settings
    st.sidebar.markdown("### 🎤 Voice Settings")
    caption_female = 'Top: 🌸 **Aria** – 🎶 **Jenny** – 🌺 **Sonia** – 🌌 **Natasha** – 🌷 **Clara**'
    caption_male   = 'Bottom: 🌟 **Guy** – 🛠️ **Ryan** – 🎻 **William** – 🌟 **Liam**'
    
    # Optionally, replace with your own local image or comment out
    try:
        st.sidebar.image('Group Picture - Voices.png', caption=caption_female + ' | ' + caption_male)
    except:
        st.sidebar.write('.')

    selected_voice = st.sidebar.selectbox(
        "👄 Select TTS Voice:",
        options=EDGE_TTS_VOICES,
        index=EDGE_TTS_VOICES.index(st.session_state['tts_voice'])
    )
    
    st.sidebar.markdown("""
    # 🎙️ Voice Character Agent Selector 🎭
    *Female Voices*:
    - 🌸 **Aria** – Elegant, creative storytelling  
    - 🎶 **Jenny** – Friendly, conversational  
    - 🌺 **Sonia** – Bold, confident  
    - 🌌 **Natasha** – Sophisticated, mysterious  
    - 🌷 **Clara** – Cheerful, empathetic  

    *Male Voices*:
    - 🌟 **Guy** – Authoritative, versatile  
    - 🛠️ **Ryan** – Approachable, casual  
    - 🎻 **William** – Classic, scholarly  
    - 🌟 **Liam** – Energetic, engaging
    """)
    
    # ▶ Audio Format
    st.markdown("### 🔊 Audio Format")
    selected_format = st.radio(
        "Choose Audio Format:",
        options=["MP3", "WAV"],
        index=0
    )

    # ▶ Update session state if changed
    if selected_voice != st.session_state['tts_voice']:
        st.session_state['tts_voice'] = selected_voice
        st.rerun()
    if selected_format.lower() != st.session_state['audio_format']:
        st.session_state['audio_format'] = selected_format.lower()
        st.rerun()

    # ▶ Text Input
    user_text = st.text_area("💬 Message:", height=100)
    user_text = user_text.strip().replace('\n', ' ')

    # ▶ Send Button
    if st.button("📨 Send"):
        # Run our process_voice_input as an async function
        asyncio.run(process_voice_input(user_text))

    # ▶ Chat History
    st.subheader("📜 Chat History")
    for c in st.session_state.chat_history:
        st.write("**You:**", c["user"])
        st.write("**Response:**", c["claude"])

def display_file_history_in_sidebar():
    """
    📂 Shows a history of local .md, .mp3, .wav files (newest first),
    with quick icons and optional download links.
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📂 File History")

    # ▶ Gather all files
    md_files = glob.glob("*.md")
    mp3_files = glob.glob("*.mp3")
    wav_files = glob.glob("*.wav")
    all_files = md_files + mp3_files + wav_files

    if not all_files:
        st.sidebar.write("No files found.")
        return

    # ▶ Sort newest first
    all_files = sorted(all_files, key=os.path.getmtime, reverse=True)

    # Group files by their query prefix (timestamp_query)
    grouped_files = {}
    for f in all_files:
        fname = os.path.basename(f)
        prefix = '_'.join(fname.split('_')[:6])  # Get timestamp part
        if prefix not in grouped_files:
            grouped_files[prefix] = {'md': [], 'audio': [], 'loaded': False}
        
        ext = os.path.splitext(fname)[1].lower()
        if ext == '.md':
            grouped_files[prefix]['md'].append(f)
        elif ext in ['.mp3', '.wav']:
            grouped_files[prefix]['audio'].append(f)

    # Sort groups by timestamp (newest first)
    sorted_groups = sorted(grouped_files.items(), key=lambda x: x[0], reverse=True)

    # 🗑⬇️ Sidebar delete all and zip all download
    col1, col4 = st.sidebar.columns(2)
    with col1:
        if st.button("🗑 Delete All"):
            for f in all_files:
                os.remove(f)
            st.rerun()
            st.session_state.should_rerun = True
    with col4:
        if st.button("⬇️ Zip All"):
            zip_name = create_zip_of_files(md_files, mp3_files, wav_files, 
                                         st.session_state.get('last_query', ''))
            if zip_name:
                st.sidebar.markdown(get_download_link(zip_name, "zip"), 
                                  unsafe_allow_html=True)

    # Display grouped files
    for prefix, files in sorted_groups:
        # Get a preview of content from first MD file
        preview = ""
        if files['md']:
            with open(files['md'][0], "r", encoding="utf-8") as f:
                preview = f.read(200).replace("\n", " ")
                if len(preview) > 200:
                    preview += "..."
        # Create unique key for this group
        group_key = f"group_{prefix}"
        if group_key not in st.session_state:
            st.session_state[group_key] = False

        # Display group expander
        with st.sidebar.expander(f"📑 Query Group: {prefix}"):
            st.write("**Preview:**")
            st.write(preview)
            
            # Load full content button
            if st.button("📖 View Full Content", key=f"btn_{prefix}"):
                st.session_state[group_key] = True

            # Only show full content and audio if button was clicked
            if st.session_state[group_key]:
                # Display markdown files
                for md_file in files['md']:
                    with open(md_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    st.markdown("**Full Content:**")
                    st.markdown(content)
                    st.markdown(get_download_link(md_file, file_type="md"), 
                              unsafe_allow_html=True)

                # Display audio files
                usePlaySidebar=False
                if usePlaySidebar:
                    for audio_file in files['audio']:
                        ext = os.path.splitext(audio_file)[1].replace('.', '')
                        st.audio(audio_file)
                        st.markdown(get_download_link(audio_file, file_type=ext), 
                                  unsafe_allow_html=True)

def main():
    # ▶ 1) Setup marquee UI in the sidebar
    update_marquee_settings_ui()
    marquee_settings = get_marquee_settings()

    # ▶ 2) Display the marquee welcome
    display_marquee(
        st.session_state['marquee_content'], 
        {**marquee_settings, "font-size": "28px", "lineHeight": "50px"},
        key_suffix="welcome"
    )

    # ▶ 3) Main action tabs and model use choices
    tab_main = st.radio("Action:", ["🎤 Voice", "📸 Media", "🔍 ArXiv", "📝 Editor"], 
                        horizontal=True)
    
    useArxiv = st.checkbox("Search Arxiv for Research Paper Answers", value=True)
    useArxivAudio = st.checkbox("Generate Audio File for Research Paper Answers", value=False)

    # ▶ 4) Show or hide custom component (optional example)
    mycomponent = components.declare_component("mycomponent", path="mycomponent")
    val = mycomponent(my_input_value="Hello from MyComponent")

    if val:
        val_stripped = val.replace('\\n', ' ')
        edited_input = st.text_area("✏️ Edit Input:", value=val_stripped, height=100)
        run_option = st.selectbox("Model:", ["Arxiv", "Other (demo)"])
        col1, col2 = st.columns(2)
        with col1:
            autorun = st.checkbox("⚙ AutoRun", value=True)
        with col2:
            full_audio = st.checkbox("📚FullAudio", value=False)

        input_changed = (val != st.session_state.old_val)

        if autorun and input_changed:
            st.session_state.old_val = val
            st.session_state.last_query = edited_input
            perform_ai_lookup(edited_input, 
                              vocal_summary=True, 
                              extended_refs=False, 
                              titles_summary=True, 
                              full_audio=full_audio, useArxiv=useArxiv, useArxivAudio=useArxivAudio)
        else:
            if st.button("▶ Run"):
                st.session_state.old_val = val
                st.session_state.last_query = edited_input
                perform_ai_lookup(edited_input, 
                                  vocal_summary=True, 
                                  extended_refs=False, 
                                  titles_summary=True, 
                                  full_audio=full_audio, useArxiv=useArxiv, useArxivAudio=useArxivAudio)

    # ─────────────────────────────────────────────────────────
    # TAB: ArXiv
    # ─────────────────────────────────────────────────────────
    if tab_main == "🔍 ArXiv":
        st.subheader("🔍 Query ArXiv")
        q = st.text_input("🔍 Query:", key="arxiv_query")
        
        st.markdown("### 🎛 Options")
        vocal_summary = st.checkbox("🎙ShortAudio", value=True, key="option_vocal_summary")
        extended_refs = st.checkbox("📜LongRefs", value=False, key="option_extended_refs")
        titles_summary = st.checkbox("🔖TitlesOnly", value=True, key="option_titles_summary")
        full_audio = st.checkbox("📚FullAudio", value=False, key="option_full_audio")
        full_transcript = st.checkbox("🧾FullTranscript", value=False, key="option_full_transcript")
        
        if q and st.button("🔍Run"):
            st.session_state.last_query = q
            result = perform_ai_lookup(q, 
                                       vocal_summary=vocal_summary, 
                                       extended_refs=extended_refs, 
                                       titles_summary=titles_summary, 
                                       full_audio=full_audio)
            if full_transcript:
                create_file(q, result, "md")

    # ─────────────────────────────────────────────────────────
    # TAB: Voice
    # ─────────────────────────────────────────────────────────
    elif tab_main == "🎤 Voice":
        display_voice_tab()

    # ─────────────────────────────────────────────────────────
    # TAB: Media
    # ─────────────────────────────────────────────────────────
    elif tab_main == "📸 Media":
        st.header("📸 Media Gallery")
        tabs = st.tabs(["🎵 Audio", "🖼 Images", "🎥 Video"])
        
        # ▶ AUDIO sub-tab
        with tabs[0]:
            st.subheader("🎵 Audio Files")
            audio_files = glob.glob("*.mp3") + glob.glob("*.wav")
            if audio_files:
                for a in audio_files:
                    with st.expander(os.path.basename(a)):
                        st.audio(a)
                        ext = os.path.splitext(a)[1].replace('.', '')
                        dl_link = get_download_link(a, file_type=ext)
                        st.markdown(dl_link, unsafe_allow_html=True)
            else:
                st.write("No audio files found.")
        
        # ▶ IMAGES sub-tab
        with tabs[1]:
            st.subheader("🖼 Image Files")
            imgs = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg")
            if imgs:
                c = st.slider("Cols", 1, 5, 3, key="cols_images")
                cols = st.columns(c)
                for i, f in enumerate(imgs):
                    with cols[i % c]:
                        st.image(Image.open(f), use_container_width=True)
            else:
                st.write("No images found.")
        
        # ▶ VIDEO sub-tab
        with tabs[2]:
            st.subheader("🎥 Video Files")
            vids = glob.glob("*.mp4") + glob.glob("*.mov") + glob.glob("*.avi")
            if vids:
                for v in vids:
                    with st.expander(os.path.basename(v)):
                        st.video(v)
            else:
                st.write("No videos found.")

    # ─────────────────────────────────────────────────────────
    # TAB: Editor
    # ─────────────────────────────────────────────────────────
    elif tab_main == "📝 Editor":
        st.write("### 📝 File Editor (Minimal Demo)")
        st.write("Select or create a file to edit. More advanced features can be added as needed.")

    # ─────────────────────────────────────────────────────────
    # SIDEBAR: FILE HISTORY + PERFORMANCE METRICS
    # ─────────────────────────────────────────────────────────
    display_file_history_in_sidebar()
    log_performance_metrics()

    # ▶ Some light CSS styling
    st.markdown("""
    <style>
        .main { background: linear-gradient(to right, #1a1a1a, #2d2d2d); color: #fff; }
        .stMarkdown { font-family: 'Helvetica Neue', sans-serif; }
        .stButton>button { margin-right: 0.5rem; }
    </style>
    """, unsafe_allow_html=True)

    # ▶ Rerun if needed
    if st.session_state.should_rerun:
        st.session_state.should_rerun = False
        st.rerun()

if __name__ == "__main__":
    main()
