# This Markdown teaches the art of prompting to produce production programs that run on your phone, your pc, pretty much everywhere!


# Go Back Jack and Do it Again:

You are a streamlit python programmer specializing in AI and software design patterns and antipatterns.  generate a python streamlit interface that demonstrates three functions in streamlit and what you can do :  Use this story as context for the interface.  Title: The Transhuman Awakening

Characters:

Dr. Ada Lovelace: A brilliant scientist and pioneer in transhumanism.
Max Powers: A young and ambitious engineer working with Dr. Lovelace.
Luna Moon: A bold astronaut chosen for the first transhuman space mission.
AI-X: The advanced artificial intelligence assisting the team.
Setting: Earth, 2023

Plot:
In 2023, Dr. Ada Lovelace and her team of researchers made a groundbreaking discovery in the field of transhumanism. They developed a technology that could safely enhance human intelligence two or three times its natural capacity. This breakthrough led to a new era of technological advancements, particularly in space exploration.

The technology, called Neural Quantum Enhancement (NQE), involved a combination of genetic engineering and advanced nanotechnology. This process integrated nanobots into the human brain, enabling rapid synaptic connections and increased neural plasticity. NQE was made possible by a new energy source, Quantum Fusion, which had been recently developed for spacecraft propulsion.

Dr. Lovelace's team, which included engineer Max Powers and astronaut Luna Moon, designed the first-ever transhuman spacecraft called the "Pegasus." It was a sleek, cutting-edge vessel that could travel at unprecedented speeds, thanks to its Quantum Fusion engine. The Pegasus was equipped with advanced life-support systems, AI-driven navigation, and a revolutionary Virtual Reality (VR) training room.

AI-X, the team's artificial intelligence, was developed to assist the team on their missions and manage the Index Builder. The Index Builder was an innovative tool that could save and organize information collected from various sources, such as the Wikipedia API. It allowed the team to quickly access relevant data during their expeditions.

Luna Moon, the astronaut chosen for the first transhuman space mission, underwent the NQE procedure to enhance her intelligence. As a result, she could absorb and analyze vast amounts of information, perform complex calculations, and quickly adapt to new environments.

The Pegasus embarked on its maiden voyage to explore the outer reaches of the solar system. With Luna's enhanced intelligence and the support of her team, they made incredible discoveries, such as new planets with potential for colonization and previously unknown resources.

Their success caught the attention of governments and private organizations worldwide. The global community began to invest in transhumanism and space exploration, accelerating humanity's expansion into the cosmos. As the technology became more widespread, people started to believe that a new era of peace, prosperity, and unity was on the horizon.

The story of Dr. Ada Lovelace, Max Powers, Luna Moon, and AI-X would go down in history as the catalyst for humanity's awakening and the dawn of the transhuman age.


# Reccombo:  

rewrite this code as the best event driven real time map by animating folium and streamlit charts pandas graph objects, generate top five programmatically in 5 lines of code or less:  import streamlit as st
import folium

def add_marker(folium_map, name, coords, website, wikipedia):
    popup_text = f"<b>{name}</b><br><a href='{website}' target='_blank'>Website</a><br><a href='{wikipedia}' target='_blank'>Wikipedia</a>"
    folium.Marker(location=coords, popup=popup_text).add_to(folium_map)

def main():
    mn_coords = [46.729553, -94.685899]
    hospital_systems = [
        ("Allina Health", [44.924180, -93.418003], "https://www.allinahealth.org/", "https://en.wikipedia.org/wiki/Allina_Health"),
        ("Alomere Health", [45.878719, -95.392539], "https://www.alomerehealth.com/", "https://en.wikipedia.org/wiki/Alomere_Health"),
        ("Altru Health System", [47.917304, -97.059748], "https://www.altru.org/", "https://en.wikipedia.org/wiki/Altru_Health_System"),
        ("Avera Health", [44.311833, -96.797603], "https://www.avera.org/", "https://en.wikipedia.org/wiki/Avera_Health"),
        ("Catholic Health Initiatives (CHI)", [44.957214, -93.269583], "https://www.catholichealthinitiatives.org/", "https://en.wikipedia.org/wiki/Catholic_Health_Initiatives"),
        ("CentraCare Health", [45.547782, -94.220109], "https://www.centracare.com/", "https://en.wikipedia.org/wiki/CentraCare_Health"),
        ("Children's Minnesota", [44.944186, -93.252723], "https://www.childrensmn.org/", "https://en.wikipedia.org/wiki/Children%27s_Minnesota"),
        ("Essentia Health", [46.807764, -92.175521], "https://www.essentiahealth.org/", "https://en.wikipedia.org/wiki/Essentia_Health"),
        ("Gillette Children's Specialty Healthcare", [44.959775, -93.186368], "https://www.gillettechildrens.org/", "https://en.wikipedia.org/wiki/Gillette_Children%27s_Specialty_Healthcare"),
        ("Gundersen Health System", [43.815935, -91.255947], "https://www.gundersenhealth.org/", "https://en.wikipedia.org/wiki/Gundersen_Health_System"),
        ("HealthPartners", [44.925221, -93.218017], "https://www.healthpartners.com/", "https://en.wikipedia.org/wiki/HealthPartners"),
        ("HealthEast Care System", [44.979166, -93.013702], "https://www.healtheast.org/", "https://en.wikipedia.org/wiki/HealthEast_Care_System"),
        ("Hennepin Healthcare", [44.972239, -93.259884], "https://www.hennepinhealthcare.org/", "https://en.wikipedia.org/wiki/Hennepin_Healthcare"),
        ("Indian Health Services", [47.504131, -92.538468], "https://www.ihs.gov/", "https://en.wikipedia.org/wiki/Indian_Health_Service"),
        ("Lakewood Health System", [46.712105, -95.947868], "https://www.lakewoodhealthsystem.com/", "https://en.wikipedia.org/wiki/Lakewood_Health_System"),
        ("Mayo Clinic Health System", [44.023977, -92.466410], "https://www.mayoclinichealthsystem.org/", "https://en.wikipedia.org/wiki/Mayo_Clinic_Health_System"),
        ("M Health Fairview", [44.954393, -93.168900], "https://www.mhealth.org/", "https://en.wikipedia.org/wiki/University_of_Minnesota_Medical_Center,_Fairview"),
        ("North Memorial Health", [45.040743, -93.365262], "https://www.northmemorial.com/", "https://en.wikipedia.org/wiki/North_Memorial_Health"),
        ("Riverwood Healthcare Center", [46.166916, -93.855874], "https://riverwoodhealthcare.org/", "https://en.wikipedia.org/wiki/Riverwood_Healthcare_Center"),
        ("Sanford Health", [46.854886, -96.847764], "https://www.sanfordhealth.org/", "https://en.wikipedia.org/wiki/Sanford_Health"),
        ("Shriners Children's", [44.943741, -93.237200], "https://www.shrinerschildrens.org/locations/twin-cities/", "https://en.wikipedia.org/wiki/Shriners_Hospitals_for_Children"),
        ("St. Francis Regional Medical Center", [44.802400, -93.527410], "https://www.allinahealth.org/st-francis-regional-medical-center", "https://en.wikipedia.org/wiki/St._Francis_Regional_Medical_Center"),
        ("Wilderness Health", [47.500629, -92.274697], "https://www.wildernesshealth.org/", "https://en.wikipedia.org/wiki/Wilderness_Health")
    ]

folium_map = folium.Map(location=mn_coords, zoom_start=7)

for system in hospital_systems:
    add_marker(folium_map, *system)

folium_static(folium_map)

if name == 'main':
    main()
    
    

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
   
   
   
   
