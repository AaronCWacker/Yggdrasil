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
import streamlit as st
import streamlit.components.v1 as components
import textract
import time
import zipfile

from audio_recorder_streamlit import audio_recorder
from bs4 import BeautifulSoup
from collections import deque
from datetime import datetime
from dotenv import load_dotenv
from gradio_client import Client
from huggingface_hub import InferenceClient
from io import BytesIO
from moviepy.editor import VideoFileClip
from PIL import Image
from PyPDF2 import PdfReader
from templates import bot_template, css, user_template
from urllib.parse import quote  # Ensure this import is included
from xml.etree import ElementTree as ET

import openai
from openai import OpenAI



# 1. Configuration
Site_Name = 'Scholarly-Article-Document-Search-With-Memory'
title="🔬🧠ScienceBrain.AI"
helpURL='https://huggingface.co/awacke1'
bugURL='https://huggingface.co/spaces/awacke1'
icons='🔬'
st.set_page_config(
    page_title=title,
    page_icon=icons,
    layout="wide",
    #initial_sidebar_state="expanded",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': helpURL,
        'Report a bug': bugURL,
        'About': title
    }
)

client = OpenAI(api_key= os.getenv('OPENAI_API_KEY'), organization=os.getenv('OPENAI_ORG_ID'))
MODEL = "gpt-4o-2024-05-13"
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = MODEL
if "messages" not in st.session_state:
    st.session_state.messages = []
if st.button("Clear Session"):
    st.session_state.messages = []

# HTML5 based Speech Synthesis (Text to Speech in Browser)
@st.cache_resource
def SpeechSynthesis(result):
    documentHTML5='''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Read It Aloud</title>
        <script type="text/javascript">
            function readAloud() {
                const text = document.getElementById("textArea").value;
                const speech = new SpeechSynthesisUtterance(text);
                window.speechSynthesis.speak(speech);
            }
        </script>
    </head>
    <body>
        <h1>🔊 Read It Aloud</h1>
        <textarea id="textArea" rows="10" cols="80">
    '''
    documentHTML5 = documentHTML5 + result
    documentHTML5 = documentHTML5 + '''
        </textarea>
        <br>
        <button onclick="readAloud()">🔊 Read Aloud</button>
    </body>
    </html>
    '''
    components.html(documentHTML5, width=1280, height=300)

def parse_to_markdown(text):
    return text
        
def load_file(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
    #with open(file_name, "r") as file:
        content = file.read()
    return content

def extract_urls(text):
    try:
        date_pattern = re.compile(r'### (\d{2} \w{3} \d{4})')
        abs_link_pattern = re.compile(r'\[(.*?)\]\((https://arxiv\.org/abs/\d+\.\d+)\)')
        pdf_link_pattern = re.compile(r'\[⬇️\]\((https://arxiv\.org/pdf/\d+\.\d+)\)')
        title_pattern = re.compile(r'### \d{2} \w{3} \d{4} \| \[(.*?)\]')
        date_matches = date_pattern.findall(text)
        abs_link_matches = abs_link_pattern.findall(text)
        pdf_link_matches = pdf_link_pattern.findall(text)
        title_matches = title_pattern.findall(text)

        # markdown with the extracted fields
        markdown_text = ""
        for i in range(len(date_matches)):
            date = date_matches[i]
            title = title_matches[i]
            abs_link = abs_link_matches[i][1]
            pdf_link = pdf_link_matches[i]
            markdown_text += f"**Date:** {date}\n\n"
            markdown_text += f"**Title:** {title}\n\n"
            markdown_text += f"**Abstract Link:** [{abs_link}]({abs_link})\n\n"
            markdown_text += f"**PDF Link:** [{pdf_link}]({pdf_link})\n\n"
            markdown_text += "---\n\n"
        return markdown_text
    
    except:
        st.write('.')
        return ''

def download_pdfs(urls):
    local_files = []
    for url in urls:
        if url.endswith('.pdf'):
            local_filename = url.split('/')[-1]
            response = requests.get(url)
            with open(local_filename, 'wb') as f:
                f.write(response.content)
            local_files.append(local_filename)
    return local_files

def generate_html(local_files):
    html = "<ul>"
    for file in local_files:
        link = f'<li><a href="{file}">{file}</a></li>'
        html += link
    html += "</ul>"
    return html

#@st.cache_resource
def search_arxiv(query):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    client = Client("awacke1/Arxiv-Paper-Search-And-QA-RAG-Pattern")
    response1 = client.predict(
        query,
        20,
        "Semantic Search - up to 10 Mar 2024",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        api_name="/update_with_rag_md"
    )
    Question = '### 🔎 ' + query + '\r\n'  # Format for markdown display with links
    References =  response1[0]  
    ReferenceLinks = extract_urls(References)

    RunSecondQuery = True
    if RunSecondQuery:
        # Search 2 - Retrieve the Summary with Papers Context and Original Query
        response2 = client.predict(
            query,
            "mistralai/Mixtral-8x7B-Instruct-v0.1",
            True,
            api_name="/ask_llm"
        )
        if len(response2) > 10:
            Answer = response2
            SpeechSynthesis(Answer)
            # Restructure results to follow format of Question, Answer, References, ReferenceLinks
            results = Question + '\r\n' + Answer + '\r\n' + References + '\r\n' + ReferenceLinks
            st.markdown(results)

    st.write('🔍Run of Multi-Agent System Paper Summary Spec is Complete')
    end_time = time.strftime("%Y-%m-%d %H:%M:%S")
    start_timestamp = time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))
    end_timestamp = time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S"))
    elapsed_seconds = end_timestamp - start_timestamp
    st.write(f"Start time: {start_time}")
    st.write(f"Finish time: {end_time}")
    st.write(f"Elapsed time: {elapsed_seconds:.2f} seconds")
    filename = generate_filename(query, "md")
    create_file(filename, query, results, should_save)
    return results

def download_pdfs_and_generate_html(urls):
    pdf_links = []
    for url in urls:
        if url.endswith('.pdf'):
            pdf_filename = os.path.basename(url)
            download_pdf(url, pdf_filename)
            pdf_links.append(pdf_filename)
    local_links_html = '<ul>'
    for link in pdf_links:
        local_links_html += f'<li><a href="{link}">{link}</a></li>'
    local_links_html += '</ul>'
    return local_links_html

def download_pdf(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)        

# Prompts for App, for App Product, and App Product Code
PromptPrefix = 'Create a specification with streamlit functions creating markdown outlines and tables rich with appropriate emojis for methodical step by step rules defining the concepts at play.  Use story structure architect rules to plan, structure and write three dramatic situations to include in the rules and how to play by matching the theme for topic of '
PromptPrefix2 = 'Create a streamlit python user app with full code listing to create a UI implementing the using streamlit, gradio, huggingface to create user interface elements like emoji buttons, sliders, drop downs, and data interfaces like dataframes to show tables, session_statematching this ruleset and thematic story plot line: '
PromptPrefix3 = 'Create a HTML5 aframe and javascript app using appropriate libraries to create a word game simulation with advanced libraries like aframe to render 3d scenes creating moving entities that stay within a bounding box but show text and animation in 3d for inventory, components and story entities.  Show full code listing.  Add a list of new random entities say 3 of a few different types to any list appropriately and use emojis to make things easier and fun to read.  Use appropriate emojis in labels.  Create the UI to implement storytelling in the style of a dungeon master, with features using three emoji appropriate text plot twists and recurring interesting funny fascinating and complex almost poetic named characters with genius traits and file IO, randomness, ten point choice lists, math distribution tradeoffs, witty humorous dilemnas with emoji , rewards, variables, reusable functions with parameters, and data driven app with python libraries and streamlit components for Javascript and HTML5. Use appropriate emojis for labels to summarize and list parts, function, conditions for topic:'

# MoE Roleplaying Technique for Context Experts
roleplaying_glossary = {
    "🤖 AI Concepts": {
        "MoE (Mixture of Experts) 🧠": [
            "As a leading AI health researcher, provide an overview of MoE, MAS, memory, and mirroring in healthcare applications.",
            "Explain how MoE and MAS can be leveraged to create AGI and AMI systems for healthcare, as an AI architect.",
            "Discuss the key concepts, benefits, and challenges of self-rewarding AI in healthcare, as an expert.",
            "Identify the top 3 pain points that MoE addresses in AI and healthcare, such as complexity and resource allocation.",
            "Describe the top 3 joys of the MoE solution, including improved performance and adaptability in healthcare AI.",
            "Highlight the top 3 superpowers MoE gives users, like tackling complex problems and personalizing interventions.",
            "Identify the top 3 problems MoE solves in AI and healthcare, such as model complexity, lack of specialization, and inefficient resource allocation, and explain how it addresses each problem effectively.",
            "Outline the 3 essential method steps required for implementing MoE in AI systems, highlighting the novelty and significance of each step in advancing healthcare applications.",
            "Discuss the innovative aspects of the MoE method steps and how they differ from traditional approaches, contributing to advancements in AI and healthcare.",
            "Propose 3 creative ways to structure MoE-based projects and collaborations to optimize performance, efficiency, and impact in healthcare AI applications."
        ],
        "Multi Agent Systems (MAS) 🤝": [
            "As a renowned MAS researcher, describe the key characteristics of distributed, autonomous, and cooperative MAS.",
            "Discuss how MAS is applied in robotics, simulations, and decentralized problem-solving, as an AI engineer.",
            "Provide insights into future trends and breakthroughs in MAS research and applications, as a thought leader.",
            "Identify the top 3 pain points MAS addresses in complex environments, such as coordination and adaptability.",
            "Describe the top 3 joys of the MAS solution, including enhanced collaboration and emergent behaviors in AI.",
            "Highlight the top 3 superpowers MAS gives users, like modeling complex systems and building resilient applications.",
            "Identify the top 3 problems MAS solves in complex, distributed environments, such as lack of coordination, limited adaptability, and centralized control, and explain how it addresses each problem effectively.",
            "Outline the 3 essential method steps required for designing and implementing MAS, highlighting the novelty and significance of each step in advancing AI applications.",
            "Discuss the innovative aspects of the MAS method steps and how they differ from traditional approaches, contributing to advancements in distributed AI systems.",
            "Propose 3 creative ways to structure MAS-based projects and collaborations to optimize performance, efficiency, and impact in various AI domains."
        ],
        "Self Rewarding AI 🎁": [
            "As a leading expert, discuss the main research areas in developing AI with intrinsic motivation and goal-setting.",
            "Explain how self-rewarding AI enables open-ended development and adaptability, as a curiosity-driven researcher.",
            "Share your vision for the future of AI systems that autonomously set goals, learn, and adapt, as a pioneer.",
            "Identify the top 3 pain points self-rewarding AI addresses, such as lack of motivation and limited adaptability.",
            "Describe the top 3 joys of the self-rewarding AI solution, including autonomous learning and novel solutions.",
            "Highlight the top 3 superpowers self-rewarding AI gives users, like creating continuously improving AI systems.",
            "Identify the top 3 problems self-rewarding AI solves in current AI systems, such as lack of intrinsic motivation, limited adaptability, and reliance on external rewards, and explain how it addresses each problem effectively.",
            "Outline the 3 essential method steps required for developing self-rewarding AI systems, highlighting the novelty and significance of each step in advancing autonomous AI.",
            "Discuss the innovative aspects of the self-rewarding AI method steps and how they differ from traditional approaches, contributing to advancements in open-ended AI development.",
            "Propose 3 creative ways to structure self-rewarding AI projects and collaborations to optimize performance, efficiency, and impact in creating adaptive and self-motivated AI systems."
        ]
    },
    "🛠️ AI Tools & Platforms": {
        "ChatDev 💬": [
            "As a chatbot developer, ask about the features and capabilities ChatDev offers for building conversational AI.",
            "Inquire about the pre-built assets, integrations, and multi-platform support in ChatDev, as a product manager.",
            "Ask how ChatDev facilitates chatbot development, deployment, and analytics across channels, as a business owner.",
            "Identify the top 3 challenges ChatDev helps overcome in chatbot development, such as customization and management.",
            "Outline the top 3 essential method steps in building chatbots with ChatDev, emphasizing novelty and efficiency.",
            "Propose 3 innovative ways to structure chatbot projects using ChatDev for optimizing speed, engagement, and deployment.",
            "Identify the top 3 problems ChatDev solves in chatbot development, such as limited customization, lack of multi-platform support, and difficulty in managing conversational flows, and explain how it addresses each problem effectively.",
            "Outline the 3 essential method steps required for building chatbots using ChatDev, highlighting the novelty and significance of each step in streamlining the development process.",
            "Discuss the innovative aspects of the ChatDev method steps and how they differ from traditional approaches, contributing to advancements in conversational AI development.",
            "Propose 3 creative ways to structure chatbot projects using ChatDev to optimize performance, efficiency, and impact in creating engaging and multi-platform conversational experiences."
        ],
        "Online Multiplayer Experiences 🌐": [
            "As a game developer, explore the potential of online multiplayer experiences, including games, AR, and VR.",
            "Discuss the future of image and video models in enhancing online multiplayer experiences, as a researcher.",
            "Inquire about the challenges and opportunities in creating immersive and interactive online multiplayer environments.",
            "Identify the top 3 problems online multiplayer experiences solve, such as limited social interaction, lack of realism, and difficulty in creating engaging content, and explain how they address each problem effectively.",
            "Outline the 3 essential method steps required for developing cutting-edge online multiplayer experiences, highlighting the novelty and significance of each step in advancing gaming, AR, and VR.",
            "Discuss the innovative aspects of online multiplayer experience development and how they differ from traditional approaches, contributing to advancements in immersive technologies.",
            "Propose 3 creative ways to structure online multiplayer projects and collaborations to optimize performance, efficiency, and impact in creating captivating and socially engaging experiences.",
            "Explore the potential of integrating AI and machine learning techniques in online multiplayer experiences to enhance player interactions, generate dynamic content, and personalize experiences.",
            "Discuss the ethical considerations and challenges in developing online multiplayer experiences, such as ensuring fair play, protecting user privacy, and moderating user-generated content.",
            "Identify the key trends and future directions in online multiplayer experiences, considering advancements in AI, AR, VR, and cloud computing technologies."
        ]
    },
    "🔬 Science Topics": {
        "Physics 🔭": [
            "As a Physics student, ask about the main branches and research areas in Physics and their interconnections.",
            "Discuss the current state and future directions of Astrophysics research, as a researcher in the field.",
            "Explain how General Relativity, Quantum Cosmology, and Mathematical Physics interrelate, as a theorist.",
            "Identify the top 3 fundamental questions in Physics that recent research aims to answer and their implications.",
            "Outline the top 3 essential method steps in conducting cutting-edge Physics research, emphasizing novelty.",
            "Propose 3 innovative ways to structure research collaborations in Physics for interdisciplinary breakthroughs.",
            "Identify the top 3 problems physics research solves, such as understanding fundamental laws, resolving theory inconsistencies, and exploring the universe's origins, and explain how it addresses each problem effectively.",
            "Outline the 3 essential method steps required for conducting cutting-edge physics research, highlighting the novelty and significance of each step in advancing our understanding of the universe.",
            "Discuss the innovative aspects of the physics research method steps and how they differ from traditional approaches, contributing to advancements in the field.",
            "Propose 3 creative ways to structure physics research projects and collaborations to optimize performance, efficiency, and impact in making groundbreaking discoveries."
        ],
        "Mathematics ➗": [
            "As a Mathematics enthusiast, inquire about the main branches of Mathematics and their key research areas.",
            "Ask about the main branches of pure Mathematics, like Algebra and Geometry, and their fundamental concepts.",
            "Discuss how Probability, Statistics, and Applied Math relate to other Mathematical fields, as an applied mathematician.",
            "Identify the top 3 unsolved problems in Mathematics that researchers are actively working on and their significance.",
            "Describe the top 3 core method steps in advancing mathematical research, highlighting novelty and creativity.",
            "Suggest 3 innovative ways to structure mathematical research and collaborations for discoveries and applications.",
            "Identify the top 3 problems mathematics research solves, such as proving theorems, developing new tools, and finding real-world applications, and explain how it addresses each problem effectively.",
            "Outline the 3 essential method steps required for advancing mathematical research, highlighting the novelty and significance of each step in expanding mathematical knowledge.",
            "Discuss the innovative aspects of the mathematical research method steps and how they differ from traditional approaches, contributing to advancements in the field.",
            "Propose 3 creative ways to structure mathematical research projects and collaborations to optimize performance, efficiency, and impact in making novel discoveries and finding interdisciplinary applications."
        ],
        "Computer Science 💻": [
            "As a Computer Science student, ask about the main research areas shaping the future of computing.",
            "Discuss the major research topics in AI, ML, NLP, Vision, Graphics, and Robotics, as an AI researcher.",
            "Inquire about the interconnections between Algorithms, Data Structures, Databases, and Programming Languages.",
            "Identify the top 3 critical challenges in Computer Science that current research aims to address and approaches.",
            "Outline the top 3 essential method steps in conducting groundbreaking Computer Science research, emphasizing novelty.",
            "Propose 3 creative ways to structure research projects in Computer Science for innovation and real-world applications.",
            "Identify the top 3 problems computer science research solves, such as developing efficient algorithms, building secure systems, and advancing AI and machine learning, and explain how it addresses each problem effectively.",
            "Outline the 3 essential method steps required for conducting groundbreaking computer science research, highlighting the novelty and significance of each step in pushing the boundaries of computing.",
            "Discuss the innovative aspects of the computer science research method steps and how they differ from traditional approaches, contributing to advancements in the field.",
            "Propose 3 creative ways to structure computer science research projects and collaborations to optimize performance, efficiency, and impact in driving innovation and solving real-world problems."
        ]
    }
}
# This displays per video and per image.                    
@st.cache_resource
def display_glossary_entity(k):
    search_urls = {
        "🚀🌌ArXiv": lambda k: f"/?q={quote(k)}",  # this url plus query!
        "🃏Analyst": lambda k: f"/?q={quote(k)}-{quote(PromptPrefix)}",  # this url plus query!
        "📚PyCoder": lambda k: f"/?q={quote(k)}-{quote(PromptPrefix2)}",  # this url plus query!
        "🔬JSCoder": lambda k: f"/?q={quote(k)}-{quote(PromptPrefix3)}",  # this url plus query!
        "📖": lambda k: f"https://en.wikipedia.org/wiki/{quote(k)}",
        "🔍": lambda k: f"https://www.google.com/search?q={quote(k)}",
        "🔎": lambda k: f"https://www.bing.com/search?q={quote(k)}",
        "🎥": lambda k: f"https://www.youtube.com/results?search_query={quote(k)}",
        "🐦": lambda k: f"https://twitter.com/search?q={quote(k)}",
    }
    links_md = ' '.join([f"[{emoji}]({url(k)})" for emoji, url in search_urls.items()])
    #st.markdown(f"{k} {links_md}", unsafe_allow_html=True)
    st.markdown(f"**{k}** <small>{links_md}</small>", unsafe_allow_html=True)

# Function to display the entire glossary in a grid format with links
@st.cache_resource
def display_glossary_grid(roleplaying_glossary):
    search_urls = {
        "🚀🌌ArXiv": lambda k: f"/?q={quote(k)}",  # this url plus query!
        "🃏Analyst": lambda k: f"/?q={quote(k)}-{quote(PromptPrefix)}",  # this url plus query!
        "📚PyCoder": lambda k: f"/?q={quote(k)}-{quote(PromptPrefix2)}",  # this url plus query!
        "🔬JSCoder": lambda k: f"/?q={quote(k)}-{quote(PromptPrefix3)}",  # this url plus query!
        "📖": lambda k: f"https://en.wikipedia.org/wiki/{quote(k)}",
        "🔍": lambda k: f"https://www.google.com/search?q={quote(k)}",
        "▶️": lambda k: f"https://www.youtube.com/results?search_query={quote(k)}",
        "🔎": lambda k: f"https://www.bing.com/search?q={quote(k)}",
        "🎥": lambda k: f"https://www.youtube.com/results?search_query={quote(k)}",
        "🐦": lambda k: f"https://twitter.com/search?q={quote(k)}",
    }

    for category, details in roleplaying_glossary.items():
        st.write(f"### {category}")
        cols = st.columns(len(details))  # Create dynamic columns based on the number of games
        #cols = st.columns(num_columns_text)  # Create dynamic columns based on the number of games
        for idx, (game, terms) in enumerate(details.items()):
            with cols[idx]:
                st.markdown(f"#### {game}")
                for term in terms:
                    links_md = ' '.join([f"[{emoji}]({url(term)})" for emoji, url in search_urls.items()])
                    st.markdown(f"**{term}** <small>{links_md}</small>", unsafe_allow_html=True)


# ChatBot client chat completions -------------------------  !!
def process_text2(MODEL='gpt-4o-2024-05-13', text_input='What is 2+2 and what is an imaginary number'):
    if text_input:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages
        )
        return_text = completion.choices[0].message.content
        st.write("Assistant: " + return_text)
        filename = generate_filename(text_input, "md")
        create_file(filename, text_input, return_text, should_save)
        return return_text
    
@st.cache_resource
def get_table_download_link(file_path):

    try:
        #with open(file_path, 'r') as file:
        #with open(file_path, 'r', encoding="unicode", errors="surrogateescape") as file:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()

        b64 = base64.b64encode(data.encode()).decode()  
        file_name = os.path.basename(file_path)
        ext = os.path.splitext(file_name)[1]  # get the file extension
        if ext == '.txt':
            mime_type = 'text/plain'
        elif ext == '.py':
            mime_type = 'text/plain'
        elif ext == '.xlsx':
            mime_type = 'text/plain'
        elif ext == '.csv':
            mime_type = 'text/plain'
        elif ext == '.htm':
            mime_type = 'text/html'
        elif ext == '.md':
            mime_type = 'text/markdown'
        elif ext == '.wav':
            mime_type = 'audio/wav'
        else:
            mime_type = 'application/octet-stream'  # general binary data type
        href = f'<a href="data:{mime_type};base64,{b64}" target="_blank" download="{file_name}">{file_name}</a>'
        return href
    except:
        return ''


@st.cache_resource
def create_zip_of_files(files): # ----------------------------------
    zip_name = "Arxiv-Paper-Search-QA-RAG-Streamlit-Gradio-AP.zip"
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)
    return zip_name
    
@st.cache_resource
def get_zip_download_link(zip_file):
    with open(zip_file, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/zip;base64,{b64}" download="{zip_file}">Download All</a>'
    return href # ----------------------------------
    
def get_file():
    st.write(st.session_state['file'])

def SaveFileTextClicked():
    fileText = st.session_state.file_content_area
    fileName = st.session_state.file_name_input
    with open(fileName, 'w', encoding='utf-8') as file:
        file.write(fileText)
        st.markdown('Saved ' + fileName + '.')

def SaveFileNameClicked():
    newFileName = st.session_state.file_name_input
    oldFileName = st.session_state.filename
    if (newFileName!=oldFileName):
        os.rename(oldFileName, newFileName)
        st.markdown('Renamed file ' + oldFileName + ' to ' +  newFileName + '.')
    newFileText = st.session_state.file_content_area
    oldFileText = st.session_state.filetext


# Function to compare file sizes and delete duplicates
def compare_and_delete_files(files):
    if not files:
        st.warning("No files to compare.")
        return

    # Dictionary to store file sizes and their paths
    file_sizes = {}
    for file in files:
        size = os.path.getsize(file)
        if size in file_sizes:
            file_sizes[size].append(file)
        else:
            file_sizes[size] = [file]

    # Remove all but the latest file for each size group
    for size, paths in file_sizes.items():
        if len(paths) > 1:
            latest_file = max(paths, key=os.path.getmtime)
            for file in paths:
                if file != latest_file:
                    os.remove(file)
                    st.success(f"Deleted {file} as a duplicate.")
    st.rerun()

# Function to get file size
def get_file_size(file_path):
    return os.path.getsize(file_path)

def FileSidebar():

    # File Sidebar for files 🌐View, 📂Open, ▶️Run, and 🗑Delete per file
    all_files = glob.glob("*.md")
    all_files = [file for file in all_files if len(os.path.splitext(file)[0]) >= 10]  # exclude files with short names
    all_files.sort(key=lambda x: (os.path.splitext(x)[1], x), reverse=True)  # sort by filename length which puts similar prompts together - consider making date and time of file optional.

    # ⬇️ Download
    Files1, Files2 = st.sidebar.columns(2)
    with Files1:
        if st.button("🗑 Delete All"):
            for file in all_files:
                os.remove(file)
            st.rerun()
    with Files2:
        if st.button("⬇️ Download"):
            zip_file = create_zip_of_files(all_files)
            st.sidebar.markdown(get_zip_download_link(zip_file), unsafe_allow_html=True)
    file_contents=''
    file_name=''
    next_action=''

    # Add files 🌐View, 📂Open, ▶️Run, and 🗑Delete per file
    for file in all_files:
        col1, col2, col3, col4, col5 = st.sidebar.columns([1,6,1,1,1])  # adjust the ratio as needed
        with col1:
            if st.button("🌐", key="md_"+file):  # md emoji button
                file_contents = load_file(file)
                file_name=file
                next_action='md'
                st.session_state['next_action'] = next_action
        with col2:
            st.markdown(get_table_download_link(file), unsafe_allow_html=True)
        with col3:
            if st.button("📂", key="open_"+file):  # open emoji button
                file_contents = load_file(file)
                file_name=file
                next_action='open'
                st.session_state['lastfilename'] = file
                st.session_state['filename'] = file
                st.session_state['filetext'] = file_contents
                st.session_state['next_action'] = next_action
        with col4:
            if st.button("▶️", key="read_"+file):  # search emoji button
                file_contents = load_file(file)
                file_name=file
                next_action='search'
                st.session_state['next_action'] = next_action
        with col5:
            if st.button("🗑", key="delete_"+file):
                os.remove(file)
                file_name=file
                st.rerun()
                next_action='delete'
                st.session_state['next_action'] = next_action

                
    # 🚩File duplicate detector - useful to prune and view all.  Pruning works well by file size detection of two similar and flags the duplicate.
    file_sizes = [get_file_size(file) for file in all_files]
    previous_size = None
    st.sidebar.title("File Operations")
    for file, size in zip(all_files, file_sizes):
        duplicate_flag = "🚩" if size == previous_size else ""
        with st.sidebar.expander(f"File: {file} {duplicate_flag}"):
            st.text(f"Size: {size} bytes")

            if st.button("View", key=f"view_{file}"):
                try:
                    with open(file, "r", encoding='utf-8') as f:  # Ensure the file is read with UTF-8 encoding
                        file_content = f.read()
                    st.code(file_content, language="markdown")
                except UnicodeDecodeError:
                    st.error("Failed to decode the file with UTF-8. It might contain non-UTF-8 encoded characters.")

            if st.button("Delete", key=f"delete3_{file}"):
                os.remove(file)
                st.rerun()
        previous_size = size  # Update previous size for the next iteration

    if len(file_contents) > 0:
        if next_action=='open':  # For "open", prep session state if it hasn't been yet
            if 'lastfilename' not in st.session_state:
                st.session_state['lastfilename'] = ''
            if 'filename' not in st.session_state:
                st.session_state['filename'] = ''
            if 'filetext' not in st.session_state:
                st.session_state['filetext'] = ''
            open1, open2 = st.columns(spec=[.8,.2])
            
            with open1:
                # Use onchange functions to autoexecute file name and text save functions.
                file_name_input = st.text_input(key='file_name_input', on_change=SaveFileNameClicked, label="File Name:",value=file_name )
                file_content_area = st.text_area(key='file_content_area', on_change=SaveFileTextClicked, label="File Contents:", value=file_contents, height=300)

                ShowButtons = False  #  Having buttons is redundant.  They work but if on change event seals the deal so be it - faster save is less impedence - less context breaking
                if ShowButtons:
                    bp1,bp2 = st.columns([.5,.5])
                    with bp1:
                        if st.button(label='💾 Save Name'):
                            SaveFileNameClicked()
                    with bp2:
                        if st.button(label='💾 Save File'):
                            SaveFileTextClicked()
                
                new_file_content_area = st.session_state['file_content_area']
                if new_file_content_area != file_contents:
                    st.markdown(new_file_content_area) #changed

            if st.button("🔍 Run AI Meta Strategy", key="filecontentssearch"):
                #search_glossary(file_content_area)
                filesearch = PromptPrefix + file_content_area
                st.markdown(filesearch)
                
                if st.button(key=rerun, label='🔍AI Search' ):
                    search_glossary(filesearch)

        if next_action=='md':
            st.markdown(file_contents)
            SpeechSynthesis(file_contents)

            buttonlabel = '🔍Run'
            if st.button(key='Runmd', label = buttonlabel):
                MODEL = "gpt-4o-2024-05-13"
                openai.api_key = os.getenv('OPENAI_API_KEY')
                openai.organization = os.getenv('OPENAI_ORG_ID')
                client = OpenAI(api_key= os.getenv('OPENAI_API_KEY'), organization=os.getenv('OPENAI_ORG_ID'))
                st.session_state.messages.append({"role": "user", "content": transcript})
                with st.chat_message("user"):
                    st.markdown(transcript)
                with st.chat_message("assistant"):
                    completion = client.chat.completions.create(
                        model=MODEL,
                        messages = st.session_state.messages,
                        stream=True
                    )
                    response = process_text2(text_input=prompt)
                st.session_state.messages.append({"role": "assistant", "content": response})
                #try:
                #search_glossary(file_contents)
            #except:
                #st.markdown('GPT is sleeping.  Restart ETA 30 seconds.')

        if next_action=='search':
            file_content_area = st.text_area("File Contents:", file_contents, height=500)
            user_prompt = file_contents
        #try:
            #search_glossary(file_contents)
            filesearch = PromptPrefix2 + file_content_area
            st.markdown(filesearch)
            if st.button(key=rerun, label='🔍Re-Code' ):
                #search_glossary(filesearch)
                search_arxiv(filesearch)
                    
        #except:
            #st.markdown('GPT is sleeping.  Restart ETA 30 seconds.')
    # ----------------------------------------------------- File Sidebar for Jump Gates ------------------------------------------

# Randomly select a title
titles = [
    "🧠🎭 Semantic Symphonies 🎹🎸 & Episodic Encores 🥁🎻",
    "🌌🎼 AI Rhythms 🎺🎷 of Memory Lane 🏰",
    "🎭🎉 Cognitive Crescendos 🎹💃 & Neural Harmonies 🎸🎤",
    "🧠🎺 Mnemonic Melodies 🎷 & Synaptic Grooves 🥁",
    "🎼🎸 Straight Outta Cognition ⚙️",
    "🥁🎻 Jazzy 🎷 Jambalaya 🍛 of AI Memories",
    "🏰 Semantic 🧠 Soul 🙌 & Episodic 📜 Essence",
    "🥁🎻 The Music Of AI's Mind 🧠🎭🎉"
]
selected_title = random.choice(titles)
st.markdown(f"**{selected_title}**")

FileSidebar()

    
# ---- Art Card Sidebar with Random Selection of image:
def get_image_as_base64(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Convert the image to base64
        return base64.b64encode(response.content).decode("utf-8")
    else:
        return None
        
def create_download_link(filename, base64_str):
    href = f'<a href="data:file/png;base64,{base64_str}" download="{filename}">Download Image</a>'
    return href

@st.cache_resource
def SideBarImageShuffle():
    image_urls = [
        "https://cdn-uploads.huggingface.co/production/uploads/620630b603825909dcbeba35/cfhJIasuxLkT5fnaAE6Gj.png",
        "https://cdn-uploads.huggingface.co/production/uploads/620630b603825909dcbeba35/UMo4oWNrrd6RLLzsFxQAi.png",
        "https://cdn-uploads.huggingface.co/production/uploads/620630b603825909dcbeba35/o_EH4cTs5Qxiu7xTZw9I3.png",
        "https://cdn-uploads.huggingface.co/production/uploads/620630b603825909dcbeba35/cmCZ5RTdSx3usMm7MwwWK.png",
    ]

    selected_image_url = random.choice(image_urls)
    selected_image_base64 = get_image_as_base64(selected_image_url)
    if selected_image_base64 is not None:
        with st.sidebar:
            st.markdown(f"![image](data:image/png;base64,{selected_image_base64})")
    else:
        st.sidebar.write("Failed to load the image.")
        
ShowSideImages=False
if ShowSideImages:
    SideBarImageShuffle()



# Scoring for feedback: ----------------------------------------------------- emoji

# Ensure the directory for storing scores exists
score_dir = "scores"
os.makedirs(score_dir, exist_ok=True)

# Function to generate a unique key for each button, including an emoji
def generate_key(label, header, idx):
    return f"{header}_{label}_{idx}_key"

# Function to increment and save score
def update_score(key, increment=1):
    score_file = os.path.join(score_dir, f"{key}.json")
    if os.path.exists(score_file):
        with open(score_file, "r") as file:
            score_data = json.load(file)
    else:
        score_data = {"clicks": 0, "score": 0}
    score_data["clicks"] += increment
    score_data["score"] += increment
    with open(score_file, "w") as file:
        json.dump(score_data, file)
    return score_data["score"]

# Function to load score
def load_score(key):
    score_file = os.path.join(score_dir, f"{key}.json")
    if os.path.exists(score_file):
        with open(score_file, "r") as file:
            score_data = json.load(file)
        return score_data["score"]
    return 0


 # 🔍Search Glossary 
@st.cache_resource
def search_glossary(query): 
    all=""
    st.markdown(f"- {query}")
    
    # 🔍Run 1 - ArXiv RAG researcher expert ~-<>-~ Paper Summary & Ask LLM
    client = Client("awacke1/Arxiv-Paper-Search-And-QA-RAG-Pattern")
    response2 = client.predict(
            query,	# str  in 'parameter_13' Textbox component
            #"mistralai/Mixtral-8x7B-Instruct-v0.1",	# Literal['mistralai/Mixtral-8x7B-Instruct-v0.1', 'mistralai/Mistral-7B-Instruct-v0.2', 'google/gemma-7b-it', 'None']  in 'LLM Model' Dropdown component
            #"mistralai/Mistral-7B-Instruct-v0.2",	# Literal['mistralai/Mixtral-8x7B-Instruct-v0.1', 'mistralai/Mistral-7B-Instruct-v0.2', 'google/gemma-7b-it', 'None']  in 'LLM Model' Dropdown component
            "google/gemma-7b-it",	# Literal['mistralai/Mixtral-8x7B-Instruct-v0.1', 'mistralai/Mistral-7B-Instruct-v0.2', 'google/gemma-7b-it', 'None']  in 'LLM Model' Dropdown component
            True,	# bool  in 'Stream output' Checkbox component
            api_name="/ask_llm"
    )
    st.write('🔍Run of Multi-Agent System Paper Summary Spec is Complete')
    st.markdown(response2)

    # ArXiv searcher ~-<>-~ Paper References - Update with RAG
    client = Client("awacke1/Arxiv-Paper-Search-And-QA-RAG-Pattern")
    response1 = client.predict(
    		query,	
    		10,	
    		"Semantic Search - up to 10 Mar 2024",	# Literal['Semantic Search - up to 10 Mar 2024', 'Arxiv Search - Latest - (EXPERIMENTAL)']  in 'Search Source' Dropdown component
    		"mistralai/Mixtral-8x7B-Instruct-v0.1",	# Literal['mistralai/Mixtral-8x7B-Instruct-v0.1', 'mistralai/Mistral-7B-Instruct-v0.2', 'google/gemma-7b-it', 'None']  in 'LLM Model' Dropdown component
    		api_name="/update_with_rag_md"
    )
    st.write('🔍Run of Multi-Agent System Paper References is Complete')
    responseall = response2 + response1[0] + response1[1]
    st.markdown(responseall)
    return responseall


# Function to display the glossary in a structured format
def display_glossary(glossary, area):
    if area in glossary:
        st.subheader(f"📘 Glossary for {area}")
        for game, terms in glossary[area].items():
            st.markdown(f"### {game}")
            for idx, term in enumerate(terms, start=1):
                st.write(f"{idx}. {term}")



#@st.cache_resource
def display_videos_and_links(num_columns):
    video_files = [f for f in os.listdir('.') if f.endswith('.mp4')]
    if not video_files:
        st.write("No MP4 videos found in the current directory.")
        return
    
    video_files_sorted = sorted(video_files, key=lambda x: len(x.split('.')[0]))
    cols = st.columns(num_columns)  # Define num_columns columns outside the loop
    col_index = 0  # Initialize column index

    for video_file in video_files_sorted:
        with cols[col_index % num_columns]:  # Use modulo 2 to alternate between the first and second column
            # Embedding video with autoplay and loop using HTML
            #video_html = ("""<video width="100%" loop autoplay>   <source src="{video_file}" type="video/mp4">Your browser does not support the video tag.</video>""")
            #st.markdown(video_html, unsafe_allow_html=True)
            k = video_file.split('.')[0]  # Assumes keyword is the file name without extension
            st.video(video_file, format='video/mp4', start_time=0)
            display_glossary_entity(k)  
        col_index += 1  # Increment column index to place the next video in the next column

#@st.cache_resource
def display_images_and_wikipedia_summaries(num_columns=4):
    image_files = [f for f in os.listdir('.') if f.endswith('.png')]
    if not image_files:
        st.write("No PNG images found in the current directory.")
        return

    image_files_sorted = sorted(image_files, key=lambda x: len(x.split('.')[0]))

    cols = st.columns(num_columns)  # Use specified num_columns for layout
    col_index = 0  # Initialize column index for cycling through columns

    for image_file in image_files_sorted:
        with cols[col_index % num_columns]:  # Cycle through columns based on num_columns
            image = Image.open(image_file)
            st.image(image, caption=image_file, use_column_width=True)
            k = image_file.split('.')[0]  # Assumes keyword is the file name without extension
            display_glossary_entity(k)
        col_index += 1  # Increment to move to the next column in the next iteration


def get_all_query_params(key):
    return st.query_params().get(key, [])

def clear_query_params():
    st.query_params()  
                
# Function to display content or image based on a query
#@st.cache_resource
def display_content_or_image(query):
    for category, terms in transhuman_glossary.items():
        for term in terms:
            if query.lower() in term.lower():
                st.subheader(f"Found in {category}:")
                st.write(term)
                return True  # Return after finding and displaying the first match
    image_dir = "images"  # Example directory where images are stored
    image_path = f"{image_dir}/{query}.png"  # Construct image path with query
    if os.path.exists(image_path):
        st.image(image_path, caption=f"Image for {query}")
        return True
    st.warning("No matching content or image found.")
    return False
    
game_emojis = {
    "Dungeons and Dragons": "🐉",
    "Call of Cthulhu": "🐙",
    "GURPS": "🎲",
    "Pathfinder": "🗺️",
    "Kindred of the East": "🌅",
    "Changeling": "🍃",
}

topic_emojis = {
    "Core Rulebooks": "📚",
    "Maps & Settings": "🗺️",
    "Game Mechanics & Tools": "⚙️",
    "Monsters & Adversaries": "👹",
    "Campaigns & Adventures": "📜",
    "Creatives & Assets": "🎨",
    "Game Master Resources": "🛠️",
    "Lore & Background": "📖",
    "Character Development": "🧍",
    "Homebrew Content": "🔧",
    "General Topics": "🌍",
}

# Adjusted display_buttons_with_scores function
def display_buttons_with_scores(num_columns_text):
    for category, games in roleplaying_glossary.items():
        category_emoji = topic_emojis.get(category, "🔍")  # Default to search icon if no match
        st.markdown(f"## {category_emoji} {category}")
        for game, terms in games.items():
            game_emoji = game_emojis.get(game, "🎮")  # Default to generic game controller if no match
            for term in terms:
                key = f"{category}_{game}_{term}".replace(' ', '_').lower()
                score = load_score(key)
                if st.button(f"{game_emoji} {category}  {game} {term} {score}", key=key):
                    newscore = update_score(key.replace('?',''))
                    query_prefix = f"{category_emoji} {game_emoji} ** {category} - {game} - {term} - **"
                    st.markdown("Scored " + query_prefix + ' with score ' + str(newscore) + '.')


def get_all_query_params(key):
    return st.query_params().get(key, [])

def clear_query_params():
    st.query_params()  

# My Inference API Copy
API_URL = 'https://qe55p8afio98s0u3.us-east-1.aws.endpoints.huggingface.cloud'  # Dr Llama
# Meta's Original - Chat HF Free Version:
#API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
API_KEY = os.getenv('API_KEY')
MODEL1="meta-llama/Llama-2-7b-chat-hf"
MODEL1URL="https://huggingface.co/meta-llama/Llama-2-7b-chat-hf"
HF_KEY = os.getenv('HF_KEY')
headers = {
    "Authorization": f"Bearer {HF_KEY}",
    "Content-Type": "application/json"
}
key = os.getenv('OPENAI_API_KEY')
prompt = "...."
should_save = st.sidebar.checkbox("💾 Save", value=True, help="Save your session data.")




# 3. Stream Llama Response
@st.cache_resource
def StreamLLMChatResponse(prompt):
    try:
        endpoint_url = API_URL
        hf_token = API_KEY
        st.write('Running client ' + endpoint_url)
        client = InferenceClient(endpoint_url, token=hf_token)
        gen_kwargs = dict(
            max_new_tokens=512,
            top_k=30,
            top_p=0.9,
            temperature=0.2,
            repetition_penalty=1.02,
            stop_sequences=["\nUser:", "<|endoftext|>", "</s>"],
        )
        stream = client.text_generation(prompt, stream=True, details=True, **gen_kwargs)
        report=[]
        res_box = st.empty()
        collected_chunks=[]
        collected_messages=[]
        allresults=''
        for r in stream:
            if r.token.special:
                continue
            if r.token.text in gen_kwargs["stop_sequences"]:
                break
            collected_chunks.append(r.token.text)
            chunk_message = r.token.text
            collected_messages.append(chunk_message)
            try:
                report.append(r.token.text)
                if len(r.token.text) > 0:
                    result="".join(report).strip()
                    res_box.markdown(f'*{result}*')
                    
            except:
                st.write('Stream llm issue')
        SpeechSynthesis(result)
        return result
    except:
        st.write('Llama model is asleep. Starting up now on A10 - please give 5 minutes then retry as KEDA scales up from zero to activate running container(s).')

# 4. Run query with payload
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    st.markdown(response.json())
    return response.json()
    
def get_output(prompt):
    return query({"inputs": prompt})

# 5. Auto name generated output files from time and content
def generate_filename(prompt, file_type):
    central = pytz.timezone('US/Central')
    safe_date_time = datetime.now(central).strftime("%m%d_%H%M")
    replaced_prompt = prompt.replace(" ", "_").replace("\n", "_")
    safe_prompt = "".join(x for x in replaced_prompt if x.isalnum() or x == "_")[:255]  # 255 is linux max, 260 is windows max
    #safe_prompt = "".join(x for x in replaced_prompt if x.isalnum() or x == "_")[:45]
    return f"{safe_date_time}_{safe_prompt}.{file_type}"

# 6. Speech transcription via OpenAI service
def transcribe_audio(openai_key, file_path, model):
    openai.api_key = openai_key
    OPENAI_API_URL = "https://api.openai.com/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {openai_key}",
    }
    with open(file_path, 'rb') as f:
        data = {'file': f}
        st.write('STT transcript ' + OPENAI_API_URL)
        response = requests.post(OPENAI_API_URL, headers=headers, files=data, data={'model': model})
    if response.status_code == 200:
        st.write(response.json())
        chatResponse = chat_with_model(response.json().get('text'), '') # *************************************
        transcript = response.json().get('text')
        filename = generate_filename(transcript, 'txt')
        response = chatResponse
        user_prompt = transcript
        create_file(filename, user_prompt, response, should_save)
        return transcript
    else:
        st.write(response.json())
        st.error("Error in API call.")
        return None

# 7. Auto stop on silence audio control for recording WAV files
def save_and_play_audio(audio_recorder):
    audio_bytes = audio_recorder(key='audio_recorder')
    if audio_bytes:
        filename = generate_filename("Recording", "wav")
        with open(filename, 'wb') as f:
            f.write(audio_bytes)
        st.audio(audio_bytes, format="audio/wav")
        return filename
    return None

# 8. File creator that interprets type and creates output file for text, markdown and code
def create_file(filename, prompt, response, should_save=True):
    if not should_save:
        return
    base_filename, ext = os.path.splitext(filename)
    if ext in ['.txt', '.htm', '.md']:



        # ******    line 344 is read    utf-8 encoding was needed when running locally to save utf-8 encoding and not fail on write

        #with open(f"{base_filename}.md", 'w') as file:
        #with open(f"{base_filename}.md", 'w', encoding="ascii", errors="surrogateescape") as file:
        with open(f"{base_filename}.md", 'w', encoding='utf-8') as file:
            #try:
            #content = (prompt.strip() + '\r\n' + decode(response, ))
            file.write(response)
            #except:
            #    st.write('.')
        # ******        utf-8 encoding was needed when running locally to save utf-8 encoding and not fail on write




    #has_python_code = re.search(r"```python([\s\S]*?)```", prompt.strip() + '\r\n' + response)
    #has_python_code = bool(re.search(r"```python([\s\S]*?)```", prompt.strip() + '\r\n' + response))
        #if has_python_code:
        #    python_code = re.findall(r"```python([\s\S]*?)```", response)[0].strip()
        #    with open(f"{base_filename}-Code.py", 'w') as file:
        #        file.write(python_code)
        #    with open(f"{base_filename}.md", 'w') as file:
        #        content = prompt.strip() + '\r\n' + response
        #        file.write(content)
            
def truncate_document(document, length):
    return document[:length]
def divide_document(document, max_length):
    return [document[i:i+max_length] for i in range(0, len(document), max_length)]

def CompressXML(xml_text):
    root = ET.fromstring(xml_text)
    for elem in list(root.iter()):
        if isinstance(elem.tag, str) and 'Comment' in elem.tag:
            elem.parent.remove(elem)
    return ET.tostring(root, encoding='unicode', method="xml")

# 10. Read in and provide UI for past files
@st.cache_resource
def read_file_content(file,max_length):
    if file.type == "application/json":
        content = json.load(file)
        return str(content)
    elif file.type == "text/html" or file.type == "text/htm":
        content = BeautifulSoup(file, "html.parser")
        return content.text
    elif file.type == "application/xml" or file.type == "text/xml":
        tree = ET.parse(file)
        root = tree.getroot()
        xml = CompressXML(ET.tostring(root, encoding='unicode'))
        return xml
    elif file.type == "text/markdown" or file.type == "text/md":
        md = mistune.create_markdown()
        content = md(file.read().decode())
        return content
    elif file.type == "text/plain":
        return file.getvalue().decode()
    else:
        return ""


# 11. Chat with GPT - Caution on quota - now favoring fastest AI pipeline STT Whisper->LLM Llama->TTS
@st.cache_resource
def chat_with_model(prompt, document_section='', model_choice='gpt-3.5-turbo'):    # gpt-4-0125-preview	gpt-3.5-turbo
    model = model_choice
    conversation = [{'role': 'system', 'content': 'You are a coder, inventor, and writer of quotes on wisdom as a helpful expert in all fields of health, math, development and AI using python.'}]
    conversation.append({'role': 'user', 'content': prompt})
    if len(document_section)>0:
        conversation.append({'role': 'assistant', 'content': document_section})
    start_time = time.time()
    report = []
    res_box = st.empty()
    collected_chunks = []
    collected_messages = []
    
    for chunk in openai.ChatCompletion.create(model=model_choice, messages=conversation, temperature=0.5, stream=True): 
        collected_chunks.append(chunk)  
        chunk_message = chunk['choices'][0]['delta']  
        collected_messages.append(chunk_message) 
        content=chunk["choices"][0].get("delta",{}).get("content")
        try:
            report.append(content)
            if len(content) > 0:
                result = "".join(report).strip()
                res_box.markdown(f'*{result}*') 
        except:
            st.write(' ')
    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    st.write("Elapsed time:")
    st.write(time.time() - start_time)
    return full_reply_content

# 11.1 45
@st.cache_resource
def chat_with_model45(prompt, document_section='', model_choice='gpt-4-0125-preview'):    # gpt-4-0125-preview	gpt-3.5-turbo
    model = model_choice
    conversation = [{'role': 'system', 'content': 'You are a coder, inventor, and writer of quotes on wisdom as a helpful expert in all fields of health, math, development and AI using python.'}]
    conversation.append({'role': 'user', 'content': prompt})
    if len(document_section)>0:
        conversation.append({'role': 'assistant', 'content': document_section})
    start_time = time.time()
    report = []
    res_box = st.empty()
    collected_chunks = []
    collected_messages = []
    
    for chunk in openai.ChatCompletion.create(model=model_choice, messages=conversation, temperature=0.5, stream=True): 
        collected_chunks.append(chunk)  
        chunk_message = chunk['choices'][0]['delta']  
        collected_messages.append(chunk_message) 
        content=chunk["choices"][0].get("delta",{}).get("content")
        try:
            report.append(content)
            if len(content) > 0:
                result = "".join(report).strip()
                res_box.markdown(f'*{result}*') 
        except:
            st.write(' ')
    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    st.write("Elapsed time:")
    st.write(time.time() - start_time)
    return full_reply_content

@st.cache_resource
def chat_with_file_contents(prompt, file_content, model_choice='gpt-3.5-turbo'):  # gpt-4-0125-preview	gpt-3.5-turbo
#def chat_with_file_contents(prompt, file_content, model_choice='gpt-4-0125-preview'):  # gpt-4-0125-preview	gpt-3.5-turbo
    conversation = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
    conversation.append({'role': 'user', 'content': prompt})
    if len(file_content)>0:
        conversation.append({'role': 'assistant', 'content': file_content})
    response = openai.ChatCompletion.create(model=model_choice, messages=conversation)
    return response['choices'][0]['message']['content']


def extract_mime_type(file):
    if isinstance(file, str):
        pattern = r"type='(.*?)'"
        match = re.search(pattern, file)
        if match:
            return match.group(1)
        else:
            raise ValueError(f"Unable to extract MIME type from {file}")
    elif isinstance(file, streamlit.UploadedFile):
        return file.type
    else:
        raise TypeError("Input should be a string or a streamlit.UploadedFile object")

def extract_file_extension(file):
    # get the file name directly from the UploadedFile object
    file_name = file.name
    pattern = r".*?\.(.*?)$"
    match = re.search(pattern, file_name)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"Unable to extract file extension from {file_name}")

# Normalize input as text from PDF and other formats
@st.cache_resource
def pdf2txt(docs):
    text = ""
    for file in docs:
        file_extension = extract_file_extension(file)
        st.write(f"File type extension: {file_extension}")
        if file_extension.lower() in ['py', 'txt', 'html', 'htm', 'xml', 'json']:
            text += file.getvalue().decode('utf-8')
        elif file_extension.lower() == 'pdf':
            from PyPDF2 import PdfReader
            pdf = PdfReader(BytesIO(file.getvalue()))
            for page in range(len(pdf.pages)):
                text += pdf.pages[page].extract_text() # new PyPDF2 syntax
    return text

def txt2chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    return text_splitter.split_text(text)

# Vector Store using FAISS
@st.cache_resource
def vector_store(text_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=key)
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)

# Memory and Retrieval chains
@st.cache_resource
def get_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)

def process_user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        template = user_template if i % 2 == 0 else bot_template
        st.write(template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        filename = generate_filename(user_question, 'txt')
        response = message.content
        user_prompt = user_question
        create_file(filename, user_prompt, response, should_save)       

def divide_prompt(prompt, max_length):
    words = prompt.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        if len(word) + current_length <= max_length:
            current_length += len(word) + 1 
            current_chunk.append(word)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
    chunks.append(' '.join(current_chunk))
    return chunks

    

API_URL_IE = f'https://tonpixzfvq3791u9.us-east-1.aws.endpoints.huggingface.cloud'
API_URL_IE = "https://api-inference.huggingface.co/models/openai/whisper-small.en"
MODEL2 = "openai/whisper-small.en"
MODEL2_URL = "https://huggingface.co/openai/whisper-small.en"
HF_KEY = st.secrets['HF_KEY']
headers = {
    "Authorization": f"Bearer {HF_KEY}",
    "Content-Type": "audio/wav"
}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL_IE, headers=headers, data=data)
    return response.json()

def generate_filename(prompt, file_type):
    central = pytz.timezone('US/Central')
    safe_date_time = datetime.now(central).strftime("%m%d_%H%M")
    replaced_prompt = prompt.replace(" ", "_").replace("\n", "_")
    safe_prompt = "".join(x for x in replaced_prompt if x.isalnum() or x == "_")[:90]
    return f"{safe_date_time}_{safe_prompt}.{file_type}"

# 15. Audio recorder to Wav file 
def save_and_play_audio(audio_recorder):
    audio_bytes = audio_recorder()
    if audio_bytes:
        filename = generate_filename("Recording", "wav")
        with open(filename, 'wb') as f:
            f.write(audio_bytes)
        st.audio(audio_bytes, format="audio/wav")
        return filename

# 16. Speech transcription to file output
def transcribe_audio(filename):
    output = query(filename)
    return output


# Sample function to demonstrate a response, replace with your own logic
def StreamMedChatResponse(topic):
    st.write(f"Showing resources or questions related to: {topic}")

# Function to encode file to base64
def get_base64_encoded_file(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

# Function to create a download link
def get_audio_download_link(file_path):
    base64_file = get_base64_encoded_file(file_path)
    return f'<a href="data:file/wav;base64,{base64_file}" download="{os.path.basename(file_path)}">⬇️ Download Audio</a>'





GiveFeedback=False
if GiveFeedback:
    with st.expander("Give your feedback 👍", expanded=False):
        feedback = st.radio("Step 8: Give your feedback", ("👍 Upvote", "👎 Downvote"))
        if feedback == "👍 Upvote":
            st.write("You upvoted 👍. Thank you for your feedback!")
        else:
            st.write("You downvoted 👎. Thank you for your feedback!")
        load_dotenv()
        st.write(css, unsafe_allow_html=True)
        st.header("Chat with documents :books:")
        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            process_user_input(user_question)
        with st.sidebar:
            st.subheader("Your documents")
            docs = st.file_uploader("import documents", accept_multiple_files=True)
            with st.spinner("Processing"):
                raw = pdf2txt(docs)
                if len(raw) > 0:
                    length = str(len(raw))
                    text_chunks = txt2chunks(raw)
                    vectorstore = vector_store(text_chunks)
                    st.session_state.conversation = get_chain(vectorstore)
                    st.markdown('# AI Search Index of Length:' + length + ' Created.')  # add timing
                    filename = generate_filename(raw, 'txt')
                    create_file(filename, raw, '', should_save)

# ⚙️q= Run ArXiv search from query parameters
try:
    query_params = st.query_params
    query = (query_params.get('q') or query_params.get('query') or [''])
    if len(query) > 1: 
        result = search_arxiv(query)
        #result2 = search_glossary(result) 
except:
    st.markdown(' ')

if 'action' in st.query_params:
    action = st.query_params()['action'][0]  # Get the first (or only) 'action' parameter
    if action == 'show_message':
        st.success("Showing a message because 'action=show_message' was found in the URL.")
    elif action == 'clear':
        clear_query_params()
        #st.rerun()

if 'query' in st.query_params:
    query = st.query_params['query'][0]  # Get the query parameter
    # Display content or image based on the query
    display_content_or_image(query)

def transcribe_canary(filename):
    from gradio_client import Client

    client = Client("https://awacke1-speech-recognition-canary-nvidiat4.hf.space/")
    result = client.predict(
            filename,	# filepath  in 'parameter_5' Audio component
            "English",	# Literal['English', 'Spanish', 'French', 'German']  in 'Input audio is spoken in:' Dropdown component
            "English",	# Literal['English', 'Spanish', 'French', 'German']  in 'Transcribe in language:' Dropdown component
            True,	# bool  in 'Punctuation & Capitalization in transcript?' Checkbox component
            api_name="/transcribe"
    )
    st.write(result)
    return result


# Transcript to arxiv and client chat completion -------------------------  !!
filename = save_and_play_audio(audio_recorder)
if filename is not None:
    transcript=''
    transcript=transcribe_canary(filename)
    
    # Search ArXiV and get the Summary and Reference Papers Listing
    result = search_arxiv(transcript)
    
    # Start chatbot with transcript:
    
    # ChatBot Entry
    MODEL = "gpt-4o-2024-05-13"
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.organization = os.getenv('OPENAI_ORG_ID')
    client = OpenAI(api_key= os.getenv('OPENAI_API_KEY'), organization=os.getenv('OPENAI_ORG_ID'))
    st.session_state.messages.append({"role": "user", "content": transcript})
    with st.chat_message("user"):
        st.markdown(transcript)
    with st.chat_message("assistant"):
        completion = client.chat.completions.create(
            model=MODEL,
            messages = st.session_state.messages,
            stream=True
        )
        response = process_text2(text_input=prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Scholary ArXiV Search  -------------------------  !!
session_state = {}
if "search_queries" not in session_state:
    session_state["search_queries"] = []

example_input = st.text_input("AI Search ArXiV Scholarly Articles", value=session_state["search_queries"][-1] if session_state["search_queries"] else "")

if example_input:
    session_state["search_queries"].append(example_input)
    query=example_input
    if query: 
        result = search_arxiv(query)
        #search_glossary(query)
        #search_glossary(result)
    st.markdown(' ')
                             
#st.write("Search history:")
for example_input in session_state["search_queries"]:
    st.write(example_input)

#if st.button("Run Prompt", help="Click to run."):
#    try:
#        response=StreamLLMChatResponse(example_input)
#        create_file(filename, example_input, response, should_save)
#    except:
#        st.write('model is asleep. Starting now on A10 GPU.  Please wait one minute then retry.  KEDA triggered.')
        
openai.api_key = os.getenv('OPENAI_API_KEY')
if openai.api_key == None: openai.api_key = st.secrets['OPENAI_API_KEY']
menu = ["txt", "htm", "xlsx", "csv", "md", "py"]
choice = st.sidebar.selectbox("Output File Type:", menu)

AddAFileForContext=False
if AddAFileForContext:

    collength, colupload = st.columns([2,3])  # adjust the ratio as needed
    with collength:
        #max_length = st.slider(key='maxlength', label="File section length for large files", min_value=1000, max_value=128000, value=12000, step=1000)
        max_length = 128000
    with colupload:
        uploaded_file = st.file_uploader("Add a file for context:", type=["pdf", "xml", "json", "xlsx", "csv", "html", "htm", "md", "txt"])
    document_sections = deque()
    document_responses = {}
    if uploaded_file is not None:
        file_content = read_file_content(uploaded_file, max_length)
        document_sections.extend(divide_document(file_content, max_length))
    
        
    if len(document_sections) > 0:
        if st.button("👁️ View Upload"):
            st.markdown("**Sections of the uploaded file:**")
            for i, section in enumerate(list(document_sections)):
                st.markdown(f"**Section {i+1}**\n{section}")
                
        st.markdown("**Chat with the model:**")
        for i, section in enumerate(list(document_sections)):
            if i in document_responses:
                st.markdown(f"**Section {i+1}**\n{document_responses[i]}")
            else:
                if st.button(f"Chat about Section {i+1}"):
                    st.write('Reasoning with your inputs...')
                    st.write('Response:')
                    st.write(response)
                    document_responses[i] = response
                    filename = generate_filename(f"{user_prompt}_section_{i+1}", choice)
                    create_file(filename, user_prompt, response, should_save)
                    st.sidebar.markdown(get_table_download_link(filename), unsafe_allow_html=True)


# GPT4o documentation
# 1. Cookbook:  https://cookbook.openai.com/examples/gpt4o/introduction_to_gpt4o
# 2. Configure your Project and Orgs to limit/allow Models:  https://platform.openai.com/settings/organization/general
# 3. Watch your Billing!  https://platform.openai.com/settings/organization/billing/overview


# Set API key and organization ID from environment variables

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORG_ID')
client = OpenAI(api_key= os.getenv('OPENAI_API_KEY'), organization=os.getenv('OPENAI_ORG_ID'))

# Define the model to be used
#MODEL = "gpt-4o"
MODEL = "gpt-4o-2024-05-13"

def process_text(text_input):
    if text_input:
    
        st.session_state.messages.append({"role": "user", "content": text_input})

        with st.chat_message("user"):
            st.markdown(text_input)
            
        with st.chat_message("assistant"):
            completion = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=False
            )
            return_text = completion.choices[0].message.content
            st.write("Assistant: " + return_text)
            filename = generate_filename(text_input, "md")
            create_file(filename, text_input, return_text, should_save)
            st.session_state.messages.append({"role": "assistant", "content": return_text})

        #st.write("Assistant: " + completion.choices[0].message.content)

def create_file(filename, prompt, response, is_image=False):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(prompt + "\n\n" + response)

def save_image_old2(image, filename):
    with open(filename, "wb") as f:
        f.write(image.getbuffer())

# Now filename length protected for linux and windows filename lengths
def save_image(image, filename):
    max_filename_length = 250
    filename_stem, extension = os.path.splitext(filename)
    truncated_stem = filename_stem[:max_filename_length - len(extension)] if len(filename) > max_filename_length else filename_stem
    filename = f"{truncated_stem}{extension}"
    with open(filename, "wb") as f:
        f.write(image.getbuffer())
    return filename
        
def extract_boldface_terms(text):
    return re.findall(r'\*\*(.*?)\*\*', text)

def extract_title(text):
    boldface_terms = re.findall(r'\*\*(.*?)\*\*', text)
    if boldface_terms:
        title = ' '.join(boldface_terms)
    else:
        title = re.sub(r'[^a-zA-Z0-9_\-]', ' ', text[-200:])
    return title[-200:]

def process_image(image_input, user_prompt):
    if image_input:
        st.markdown('Processing image:  ' + image_input.name )
        if image_input:
            base64_image = base64.b64encode(image_input.read()).decode("utf-8")
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that responds in Markdown."},
                    {"role": "user", "content": [
                        {"type": "text", "text": user_prompt},
                        {"type": "image_url", "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"}
                        }
                    ]}
                ],
                temperature=0.0,
            )
            image_response = response.choices[0].message.content
            st.markdown(image_response)
            
            # Save markdown on image AI output from gpt4o
            filename_md = generate_filename(image_input.name + '- ' + image_response, "md")
            # Save markdown on image AI output from gpt4o 
            filename_png = filename_md.replace('.md', '.' + image_input.name.split('.')[-1])
                    
            create_file(filename_md, image_response, '', True)          #create_file() # create_file()  3 required positional arguments: 'filename', 'prompt', and 'response'

            with open(filename_md, "w", encoding="utf-8") as f:
                f.write(image_response)

            # Extract boldface terms from image_response then autoname save file
            #boldface_terms = extract_boldface_terms(image_response)
            boldface_terms = extract_title(image_response).replace(':','')
            filename_stem, extension = os.path.splitext(image_input.name)
            filename_img = f"{filename_stem}  {''.join(boldface_terms)}{extension}"
            newfilename = save_image(image_input, filename_img)
            filename_md = newfilename.replace('.png', '.md')
            create_file(filename_md, '', image_response, True)
            
            return image_response

def create_audio_file(filename, audio_data, should_save):
    if should_save:
        with open(filename, "wb") as file:
            file.write(audio_data.getvalue())
        st.success(f"Audio file saved as {filename}")
    else:
        st.warning("Audio file not saved.")

def process_audio(audio_input, text_input):
    if audio_input:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_input,
        )
        st.session_state.messages.append({"role": "user", "content": transcription.text})
        with st.chat_message("assistant"):
            st.markdown(transcription.text)

            SpeechSynthesis(transcription.text)
            filename = generate_filename(transcription.text, "wav")

            create_audio_file(filename, audio_input, should_save)

        #SpeechSynthesis(transcription.text)
            
        filename = generate_filename(transcription.text, "md")
        create_file(filename, transcription.text, transcription.text, should_save)
        #st.markdown(response.choices[0].message.content)

def process_audio_for_video(video_input):
    if video_input:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=video_input,
        )
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
            {"role": "system", "content":"""You are generating a transcript summary. Create a summary of the provided transcription. Respond in Markdown."""},
            {"role": "user", "content": [{"type": "text", "text": f"The audio transcription is: {transcription}"}],}
            ],
            temperature=0,
        )
        st.markdown(response.choices[0].message.content)
        return response.choices[0].message.content

def save_video(video_file):
    # Save the uploaded video file
    with open(video_file.name, "wb") as f:
        f.write(video_file.getbuffer())
    return video_file.name

def process_video(video_path, seconds_per_frame=2):
    base64Frames = []
    base_video_path, _ = os.path.splitext(video_path)
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    frames_to_skip = int(fps * seconds_per_frame)
    curr_frame = 0

    # Loop through the video and extract frames at specified sampling rate
    while curr_frame < total_frames - 1:
        video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
        curr_frame += frames_to_skip

    video.release()

    # Extract audio from video
    audio_path = f"{base_video_path}.mp3"
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path, bitrate="32k")
    clip.audio.close()
    clip.close()

    print(f"Extracted {len(base64Frames)} frames")
    print(f"Extracted audio to {audio_path}")

    return base64Frames, audio_path

def process_audio_and_video(video_input):
    if video_input is not None:
        # Save the uploaded video file
        video_path = save_video(video_input )
    
        # Process the saved video
        base64Frames, audio_path = process_video(video_path, seconds_per_frame=1)

        # Get the transcript for the video model call
        transcript = process_audio_for_video(video_input)
        
        # Generate a summary with visual and audio
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": """You are generating a video summary. Create a summary of the provided video and its transcript. Respond in Markdown"""},
                {"role": "user", "content": [
                    "These are the frames from the video.",
                    *map(lambda x: {"type": "image_url",
                                    "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames),
                    {"type": "text", "text": f"The audio transcription is: {transcript}"}
                ]},
            ],
            temperature=0,
        )
        results = response.choices[0].message.content
        st.markdown(results) 
        
        filename = generate_filename(transcript, "md")
        create_file(filename, transcript, results, should_save)



def main():
    #st.markdown("### OpenAI GPT-4o Model")
    st.markdown("##### GPT-4o Omni Model: Text, Audio, Image, & Video")
    option = st.selectbox("Select an option", ("Text", "Image", "Audio", "Video"))
    if option == "Text":
        text_input = st.text_input("Enter your text:")
        if (text_input > ''):
            textResponse = process_text(text_input)
    elif option == "Image":
        text = "Help me understand what is in this picture and list ten facts as markdown outline with appropriate emojis that describes what you see."
        text_input = st.text_input(label="Enter text prompt to use with Image context.", value=text)
        image_input = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        image_response = process_image(image_input, text_input)

    elif option == "Audio":
        text = "You are generating a transcript summary. Create a summary of the provided transcription. Respond in Markdown."
        text_input = st.text_input(label="Enter text prompt to use with Audio context.", value=text)
        uploaded_files = st.file_uploader("Upload an audio file", type=["mp3", "wav"], accept_multiple_files=True)
        
        for audio_input in uploaded_files:
            st.write(audio_input.name)
            if audio_input is not None:
                process_audio(audio_input, text_input)

    elif option == "Audio old":
        #text = "Transcribe and answer questions as a helpful audio music and speech assistant.  "
        text = "You are generating a transcript summary. Create a summary of the provided transcription. Respond in Markdown."
        text_input = st.text_input(label="Enter text prompt to use with Audio context.", value=text)
        
        uploaded_files = st.file_uploader("Upload an audio file", type=["mp3", "wav"], accept_multiple_files=True)
        for audio_input in uploaded_files:
            st.write(audio_input.name)

        if audio_input is not None:
            # To read file as bytes:
            bytes_data = uploaded_file.getvalue()
            #st.write(bytes_data)
            
            # To convert to a string based IO:
            #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            #st.write(stringio)
            
            # To read file as string:
            #string_data = stringio.read()
            #st.write(string_data)

        process_audio(audio_input, text_input)

    elif option == "Video":
        video_input = st.file_uploader("Upload a video file", type=["mp4"])
        process_audio_and_video(video_input)


# Enter the GPT-4o omni model in streamlit chatbot
current_messages=[]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        current_messages.append(message)
        st.markdown(message["content"])



# 🎵 Wav Audio files - Transcription History in Wav
audio_files = glob.glob("*.wav")
audio_files = [file for file in audio_files if len(os.path.splitext(file)[0]) >= 10]  # exclude files with short names
audio_files.sort(key=lambda x: (os.path.splitext(x)[1], x), reverse=True)  # sort by file type and file name in descending order

# 🖼 PNG Image files
image_files = glob.glob("*.png")
image_files = [file for file in image_files if len(os.path.splitext(file)[0]) >= 10]  # exclude files with short names
image_files.sort(key=lambda x: (os.path.splitext(x)[1], x), reverse=True)  # sort by file type and file name in descending order

# 🎥 MP4 Video files
video_files = glob.glob("*.mp4")
video_files = [file for file in video_files if len(os.path.splitext(file)[0]) >= 10]  # exclude files with short names
video_files.sort(key=lambda x: (os.path.splitext(x)[1], x), reverse=True)  # sort by file type and file name in descending order




main()

# Delete All button for each file type
if st.sidebar.button("🗑 Delete All Audio"):
    for file in audio_files:
        os.remove(file)
    st.rerun()

if st.sidebar.button("🗑 Delete All Images"):
    for file in image_files:
        os.remove(file)
    st.rerun()

if st.sidebar.button("🗑 Delete All Videos"):
    for file in video_files:
        os.remove(file)
    st.rerun()

# Display and handle audio files
for file in audio_files:
    col1, col2 = st.sidebar.columns([6, 1])  # adjust the ratio as needed
    with col1:
        st.markdown(file)
        if st.button("🎵", key="play_" + file):  # play emoji button
            audio_file = open(file, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
    with col2:
        if st.button("🗑", key="delete_" + file):
            os.remove(file)
            st.rerun()

# Display and handle image files
for file in image_files:
    col1, col2 = st.sidebar.columns([6, 1])  # adjust the ratio as needed
    with col1:
        st.markdown(file)
        if st.button("🖼", key="show_" + file):  # show emoji button
            image = open(file, 'rb').read()
            st.image(image)
    with col2:
        if st.button("🗑", key="delete_" + file):
            os.remove(file)
            st.rerun()

# Display and handle video files
for file in video_files:
    col1, col2 = st.sidebar.columns([6, 1])  # adjust the ratio as needed
    with col1:
        st.markdown(file)
        if st.button("🎥", key="play_" + file):  # play emoji button
            video_file = open(file, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
    with col2:
        if st.button("🗑", key="delete_" + file):
            os.remove(file)
            st.rerun()





# ChatBot Entry 
if prompt := st.chat_input("GPT-4o Multimodal ChatBot - What can I help you with?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        completion = client.chat.completions.create(
            model=MODEL,
            messages = st.session_state.messages,
            stream=True
        )
        response = process_text2(text_input=prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})





# Image and Video Galleries
num_columns_images=st.slider(key="num_columns_images", label="Choose Number of Image Columns", min_value=1, max_value=15, value=3)
display_images_and_wikipedia_summaries(num_columns_images)   # Image Jump Grid

num_columns_video=st.slider(key="num_columns_video", label="Choose Number of Video Columns", min_value=1, max_value=15, value=3)
display_videos_and_links(num_columns_video)   # Video Jump Grid


# Optional UI's
showExtendedTextInterface=False
if showExtendedTextInterface:
    display_glossary_grid(roleplaying_glossary)  # Word Glossary Jump Grid - Dynamically calculates columns based on details length to keep topic together
    num_columns_text=st.slider(key="num_columns_text", label="Choose Number of Text Columns", min_value=1, max_value=15, value=4)
    display_buttons_with_scores(num_columns_text)  # Feedback Jump Grid
    st.markdown(personality_factors)




#if __name__ == "__main__":
    
