

```python

import streamlit as st

from gradio_client import Client

client = Client("awacke1/Arxiv-Paper-Search-And-QA-RAG-Pattern")
result = client.predict(
		"What is Semantic and Episodic memory?",	# str  in 'Search' Textbox component
		4,	# float (numeric value between 4 and 10) in 'Top n results as context' Slider component
		"Semantic Search - up to 10 Mar 2024",	# Literal['Semantic Search - up to 10 Mar 2024', 'Arxiv Search - Latest - (EXPERIMENTAL)']  in 'Search Source' Dropdown component
		"mistralai/Mixtral-8x7B-Instruct-v0.1",	# Literal['mistralai/Mixtral-8x7B-Instruct-v0.1', 'mistralai/Mistral-7B-Instruct-v0.2', 'google/gemma-7b-it', 'None']  in 'LLM Model' Dropdown component
		api_name="/update_with_rag_md"
)
st.markdown(result)

```
