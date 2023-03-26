

# Top Ten Live Examples:

1. ![image](https://user-images.githubusercontent.com/30595158/227757162-129e4bd9-6f7e-48ec-9904-d3c8b4601767.png)
https://huggingface.co/spaces/awacke1/Webcam-Object-Recognition-Yolo-n-Coco
2. Memory: https://huggingface.co/spaces/awacke1/Twitter-Sentiment-Live-Realtime   |   ![image](https://user-images.githubusercontent.com/30595158/227757196-a11b0b2c-75e7-4212-8573-050c3a21f1b5.png)

3. https://huggingface.co/spaces/awacke1/2-LiveASR 
4. What is consistency 1-10, repeatedly, speed and loss rates
one two three four five six seventhree four five six seven eight nine ten one two three four five six seven eight nine ten
Still not so good
5. SimPhysics: https://huggingface.co/spaces/awacke1/1-SimPhysics
6. RTLiveDashBoard: https://huggingface.co/spaces/awacke1/StreamlitTimerTest
7. 


When things go wrong - AI cant follow you,
pivot and get it to, learning language nuances between 3.5 to 4 and see what output shapes change:
continue

graphql
Copy code
    # Handle dataset search
    query = st.text_input("Search for datasets:")
    if query:
        datasets = search_datasets(query)
        show_datasets(datasets)
if name == 'main':
main()

sql
Copy code

The `search_datasets` function sends a request to Hugging Face Hub with the search query and returns the top 3 matching datasets. The `show_datasets` function displays detailed information about each matching dataset. In the `main` function, we handle the dataset search when no menu button is clicked. The search query is obtained from the user input and passed to the `search_datasets` function. If there are matching datasets, they are displayed using the `show_datasets` function.



Aaron Wacker
modify this program with examples:  Tune to make it fast and show four different views of the charts at a time and ask user to upvote thumbs up emoji or downvote thumbs down emoji and record is saved and shown clearly as the users human feedback which is precious!!  import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# top-level filters
job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["job"] == job_filter]

# near real-time / live feed simulation
for seconds in range(200):

    df["age_new"] = df["age"] * np.random.choice(range(1, 5))
    df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_age = np.mean(df["age_new"])

    count_married = int(
        df[(df["marital"] == "married")]["marital"].count()
        + np.random.choice(range(1, 30))
    )

    balance = np.mean(df["balance_new"])

    with placeholder.container():

        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Age ⏳",
            value=round(avg_age),
            delta=round(avg_age) - 10,
        )
        
        kpi2.metric(
            label="Married Count 💍",
            value=int(count_married),
            delta=-10 + count_married,
        )
        
        kpi3.metric(
            label="A/C Balance ＄",
            value=f"$ {round(balance,2)} ",
            delta=-round(balance / count_married) * 100,
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="age_new", x="marital"
            )
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="age_new")
            st.write(fig2)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
        
        
