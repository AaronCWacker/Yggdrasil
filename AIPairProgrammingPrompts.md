# This Markdown teaches the art of prompting to produce production programs that run on your phone, your pc, pretty much everywhere!


# Words of Power

show streamlit full code list as app.py


# Sidebar:

Rewrite this to have a game-like interface with clickable emoji based buttons that are larrge and clear with single word labels.  Create a named keyed user interface input appropriate for each sidebar.markdown call in list below.  Make each a button with an emoji:  import streamlit as st
import base64

# Define the sidebar menu with icons
def show_menu():
    st.sidebar.title("Menu")
    st.sidebar.markdown(":memo: Title")
    st.sidebar.markdown(":briefcase: Case")
    st.sidebar.markdown(":chart_with_upwards_trend: Values")
    st.sidebar.markdown(":newspaper: Product Press Release")
    st.sidebar.markdown(":running: Customer Journey and Experience")

# Define the chat input and send button
def show_chat_input():
    message = st.text_input("Enter your message:")
    if st.button("Send"):
        save_message(message)

# Define the function to save the message to the log file
def save_message(message):
    with open("chat_log.txt", "a") as f:
        f.write(message + "\n")

# Define the function to generate the download link for the log file
def download_log_file():
    with open("chat_log.txt", "r") as f:
        log_data = f.read()
    b64 = base64.b64encode(log_data.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="chat_log.txt">Download chat log</a>'
    st.markdown(href, unsafe_allow_html=True)

# Define the main function to run the Streamlit app
def main():
    show_menu()
    show_chat_input()
    download_log_file()

if __name__ == '__main__':
    main()





Write a streamlit python program that receives a pasted textbox of large text, then runs it through transformers and huggingface hub api to compare three models.  Create User Interface controls on the sidebar which Tells me the top three songs of each year for last 30 years in both semantic factual and episodic emotional memory according to published theory.

# GPT 4:

Write a streamlit python program that receives a pasted textbox of large text, then runs it through transformers and huggingface hub api to compare three models.  Create User Interface controls on the sidebar which Tells me the top three songs of each year for last 30 years in both semantic factual and episodic emotional memory according to published theory.
To create a Streamlit app that fulfills your requirements, first, you need to install the necessary libraries by running:

Copy code
pip install streamlit
pip install transformers
After installing the required libraries, you can create a Python script named song_analyzer.py and add the following code:

python
Copy code
import streamlit as st
import requests
from transformers import pipeline, AutoTokenizer

# Function to fetch top songs of each year
def get_top_songs(year):
    # Replace this URL with the API or source containing top songs of each year
    url = f"https://example.com/api/top_songs/{year}"
    response = requests.get(url)
    return response.json()

# Initialize transformers
MODELS = {
    "semantic-factual": "model-1-name",
    "episodic-emotional": "model-2-name",
    "published-theory": "model-3-name"
}

st.title("Large Text Analysis and Song Analyzer")

# Sidebar configuration
st.sidebar.header("Configuration")
selected_model = st.sidebar.selectbox(
    "Select a Model",
    list(MODELS.keys()),
    help="Choose a model for text analysis"
)
year_range = st.sidebar.slider(
    "Year Range",
    min_value=1980,
    max_value=2010,
    value=(1990, 2000),
    step=1,
    help="Select a range of years to display top songs"
)

# Main content
st.header("Text Analysis")
input_text = st.text_area("Paste your large text here:")

if input_text:
    st.header("Model Comparison")
    model_name = MODELS[selected_model]
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = pipeline("text-classification", model=model_name, tokenizer=tokenizer)

    # Analyzing the text using the selected model
    analysis_result = model(input_text)
    st.write(f"Analysis result for {selected_model}:")
    st.write(analysis_result)

st.header("Top Songs by Year")
for year in range(year_range[0], year_range[1] + 1):
    top_songs = get_top_songs(year)
    st.subheader(f"Top Songs of {year}")
    for idx, song in enumerate(top_songs, start=1):
        st.write(f"{idx}. {song['title']} by {song['artist']}")

# Running the Streamlit app
if __name__ == "__main__":
    st.set_page_config(page_title="Text Analysis and Song Analyzer", page_icon=":musical_note:")
    st.write("""
    This app compares text analysis with different models and shows the top songs of each year
    for the last 30 years in both semantic factual and episodic emotional memory according to published theory.
    """)
Make sure to replace the model-1-name, model-2-name, and model-3-name with the actual model names you want to use from HuggingFace Hub.

You will also need to replace the url variable in the get_top_songs function with an actual API or source that provides top songs of each year.

To run the Streamlit app, execute the following command in your terminal:

arduino
Copy code
streamlit run song_analyzer.py
This will open the app in your default web browser, where you can paste the large text, choose a model, and display the top songs of each year within the specified range.







# GPT 3.5:

I'm sorry, but the task you are asking me to perform is quite complex and requires integration of multiple different components. While I can provide guidance and code snippets to help you get started, it may not be possible for me to complete the entire task for you within the scope of this session.

Here is an outline of the steps you could follow to complete the task:

Install the necessary Python packages:

streamlit: for building the web app
transformers: for accessing the pre-trained language models
huggingface_hub: for downloading the models from the Hugging Face model hub
You can install these packages using the pip package manager:

Copy code
pip install streamlit transformers huggingface_hub
Create a new Python file and import the required packages:

python
Copy code
import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import huggingface_hub
Create a function that loads the models from the Hugging Face model hub:

python
Copy code
@st.cache(allow_output_mutation=True)
def load_models(model_names):
    models = {}
    for model_name in model_names:
        # Download the model from the Hugging Face model hub
        model_path = huggingface_hub.download(model_name)

        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)

        # Create a pipeline for text classification
        classifier = pipeline(
            "text-classification",
            model=model,
            tokenizer=tokenizer,
        )

        # Add the model to the dictionary
        models[model_name] = classifier

    return models
Define the list of model names and call the load_models function to load the models:

python
Copy code
# Define the list of model names
model_names = [
    "bert-base-uncased",
    "distilbert-base-uncased-finetuned-sst-2-english",
    "roberta-base"
]

# Load the models
models = load_models(model_names)
Create a function that takes a text input, runs it through each model, and returns the classification results:

python
Copy code
def classify_text(text):
    results = {}
    for model_name, model in models.items():
        # Run the text through the model
        output = model(text)

        # Get the predicted label and score
        label = output[0]["label"]
        score = output[0]["score"]

        # Add the result to the dictionary
        results[model_name] = {"label": label, "score": score}

    return results
Define the function that retrieves the top three songs of each year for the last 30 years in both semantic factual and episodic emotional memory according to published theory:

python
Copy code
def get_top_songs():
    # TODO: Implement the function to retrieve the top songs
    pass
Define the Streamlit app:

python
Copy code
def main():
    # Set the page title
    st.set_page_config(page_title="Model Comparison")

    # Create the sidebar
    st.sidebar.header("Top Songs by Year")
    st.sidebar.subheader("Semantic Factual Memory")
    st.sidebar.subheader("Episodic Emotional Memory")
    st.sidebar.markdown("---")

    # Create the main content area
    st.header("Model Comparison")
    text = st.text_area("Paste your text here", height=200)

    # Run the text through each model and display the results
   
   
   
   
