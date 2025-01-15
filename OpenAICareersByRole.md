
# Position and Demand Analysis for OpenAI - Select ML Roles.


```markdown

Share


You said:
For the roles below please help me write a single streamlit markdown python app.py and requirements.txt to perform a demo of each using three python libraries per position to simulate the visualization of that process and demonstrate and document appropriate library usage :    1) Roles > $500k (💰💰💰💰💰)
🤖💼 Engineering Manager, Distributed Systems ($360K–$530K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Large-scale distributed computing & HPC performance
Coordination of concurrency frameworks (Kubernetes, etc.)
Python & Golang for infra automation
System reliability & SRE best practices
🤖⚙️ HW/SW Co-Design Engineer (Positions #33 & #35) ($360K–$530K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

GPU accelerator architecture & CUDA kernel optimization
Low-level HPC code (C++/Triton) & parallel programming
Cross-layer performance tuning (hardware + software)
Data-center scale HPC or ML deployment
🤖 Machine Learning Engineer, Applied AI ($310K–$550K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Transformer-based LLM development & fine-tuning
Building ML-driven products (Python, PyTorch)
Performance optimization for large-scale inference
End-to-end MLOps & DevOps
🤖 Machine Learning Engineer, Integrity ($310K–$550K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Abuse detection & ML-based risk scoring
NLP pipelines (PyTorch/Transformers)
Large-scale data ingestion & labeling
Automated moderation & anomaly detection
🤖 Machine Learning Engineer, Retrieval & Search ($310K–$550K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Vector databases & semantic search (FAISS, etc.)
Large-scale retrieval optimization (RAG, etc.)
Python-based data pipelines for query handling
LLM-based ranking & retrieval modeling
🤖💼 Platform ML Engineering Manager, Model Graph ($440K–$530K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Managing large ML architecture at scale (transformers)
Distributed training frameworks (PyTorch, etc.)
Python/C++ HPC code for model parallelism
Cross-functional leadership for platform roadmaps
🤖💼 Platform ML Engineering Manager, Training ($440K–$530K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Overseeing massive-scale model training ops
HPC provisioning & GPU cluster orchestration
ML pipeline efficiency & dev enablement
Cross-team collaboration & project leadership
🤖⚙️ Principal Engineer, GPU Platform ($385K–$550K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

GPU kernel design & HPC concurrency
Performance modeling for large GPU fleets
Low-level driver optimizations (CUDA, RDMA, etc.)
Containerized HPC infrastructure (K8s + GPU orchestration)
🤖 Research Engineer, Data Processing (Foundations) ($360K–$530K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Building massive training sets for LLMs
Data pipeline tooling (Spark, Airflow)
Scalable data cleaning & dedup strategies
Performance-aware code in Python & C++
🤖 Research Engineer, Pre-training Architecture ($360K–$530K) → >$500k 💰💰💰💰💰
Key Skills & Tech:

Transformer modeling (GPT-like) & novel arch prototyping
HPC training pipeline & multi-GPU scheduling
Python + low-level matrix ops / custom CUDA kernels
Foundational large-scale data ingestion & curation

ChatGPT

Thought about high-level engineering roles for 49 seconds
Below is an example Streamlit application (app.py) that demonstrates each of the listed roles (all offering “>$500k” compensation) with a brief visualization or code snippet using three Python libraries per role to simulate relevant processes. Each role section includes short usage examples and commentary. A corresponding requirements.txt is also provided.

app.py
python
Copy
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import torch
import time

# Additional libraries referenced in code snippets for demonstration:
import concurrent.futures   # For HPC concurrency demonstration
import numba               # For GPU kernel optimization
import spacy               # For NLP pipeline demonstration
import faiss               # For vector search demonstration
import networkx as nx      # For graph-based model pipeline
# (In real HPC or distributed training scenarios, you'd also see frameworks such as
#  Horovod, Ray, PyTorch Distributed, Dask, Spark, etc. We reference them conceptually.)

st.set_page_config(page_title=">$500k Roles Demonstration", layout="centered")

# Define roles and brief descriptions:
roles_info = {
    "Engineering Manager, Distributed Systems": {
        "salary": ">$500k 💰💰💰💰💰",
        "tech_stack": [
            "concurrent.futures (Python concurrency)",
            "Kubernetes concepts (mentioned conceptually)",
            "NumPy or Dask (for HPC scale-out)"
        ],
        "description": """
        This role focuses on large-scale distributed computing,
        concurrency frameworks (Kubernetes, etc.), Python & Golang for infra automation,
        and system reliability / SRE best practices.
        """,
        "demo": """
```python
# Simple concurrency example with concurrent.futures
import concurrent.futures

def heavy_computation(x):
    # Emulate HPC job
    return x*x

data = list(range(10))
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = list(executor.map(heavy_computation, data))
print("Computed squares in parallel:", results)
css
Copy
    """,
    "chart_demo_title": "Distributed System Simulation",
    "chart_demo_data": pd.DataFrame({
        'Tasks': ['Task 1','Task 2','Task 3','Task 4','Task 5'],
        'CompletionTime (s)': [3, 5, 2, 6, 4]
    })
},

"HW/SW Co-Design Engineer (GPU Accelerator)": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "Numba (GPU-targeted Python)",
        "C++/Triton (mentioned conceptually)",
        "Parallel programming optimizations"
    ],
    "description": """
    Key responsibilities include GPU accelerator architecture & CUDA kernel optimization,
    low-level HPC code (C++/Triton) & parallel programming, and cross-layer performance tuning
    (hardware + software).
    """,
    "demo": """
python
Copy
# Simple GPU kernel example with numba
import numba
import numpy as np

@numba.cuda.jit
def vector_add(a, b, c):
    idx = numba.cuda.grid(1)
    if idx < a.size:
        c[idx] = a[idx] + b[idx]

# Using Numba to accelerate on a CUDA-capable GPU
N = 10
A = np.arange(N, dtype=np.float32)
B = np.ones(N, dtype=np.float32)
C = np.zeros(N, dtype=np.float32)

dA = numba.cuda.to_device(A)
dB = numba.cuda.to_device(B)
dC = numba.cuda.to_device(C)

threads_per_block = 32
blocks_per_grid = (N + (threads_per_block - 1)) // threads_per_block

vector_add[blocks_per_grid, threads_per_block](dA, dB, dC)
C = dC.copy_to_host()
print("Vector Add on GPU:", C)
rust
Copy
    """,
    "chart_demo_title": "GPU Parallel Performance",
    "chart_demo_data": pd.DataFrame({
        'BatchSize': [32, 64, 128, 256],
        'Throughput (GFLOPS)': [50, 90, 160, 300]
    })
},

"Machine Learning Engineer, Applied AI": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "PyTorch for model building",
        "Hugging Face Transformers for LLM",
        "scikit-learn for data preprocessing"
    ],
    "description": """
    This role involves Transformer-based LLM development & fine-tuning,
    building ML-driven products in Python/PyTorch, optimizing performance for large-scale
    inference, and handling end-to-end MLOps & DevOps.
    """,
    "demo": """
python
Copy
# Mini demonstration with PyTorch
import torch
from torch import nn

model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)
x = torch.randn(1, 10)
out = model(x)
print("Simple forward pass output:", out)
python
Copy
    """,
    "chart_demo_title": "Model Inference Performance",
    "chart_demo_data": pd.DataFrame({
        'BatchSize': [1, 16, 64, 128],
        'InferenceTime (ms)': [2.1, 3.5, 8.8, 16.7]
    })
},

"Machine Learning Engineer, Integrity": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "spaCy (NLP pipelines)",
        "PyTorch/Transformers (deep NLP)",
        "scikit-learn (anomaly detection)"
    ],
    "description": """
    Specializes in abuse detection & ML-based risk scoring, NLP pipelines,
    large-scale data ingestion & labeling, and automated moderation & anomaly detection.
    """,
    "demo": """
python
Copy
# Basic text classification approach (spaCy or Hugging Face)
import spacy

nlp = spacy.load("en_core_web_sm")  # example small model
doc = nlp("This is a suspicious message containing potential policy violations.")
for ent in doc.ents:
    print(ent.text, ent.label_)
css
Copy
    """,
    "chart_demo_title": "Integrity Anomaly Scores",
    "chart_demo_data": pd.DataFrame({
        'Sample': ['Msg1','Msg2','Msg3','Msg4'],
        'AnomalyScore': [0.1, 0.7, 0.3, 0.9]
    })
},

"Machine Learning Engineer, Retrieval & Search": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "FAISS (vector similarity search)",
        "Sentence Transformers",
        "scikit-learn (data prep & transformations)"
    ],
    "description": """
    Responsible for vector databases & semantic search (FAISS, etc.),
    large-scale retrieval optimization (RAG), Python data pipelines for query handling,
    and LLM-based ranking & retrieval modeling.
    """,
    "demo": """
python
Copy
# Example: Building an index with FAISS
import faiss
import numpy as np

d = 4  # dimension
index = faiss.IndexFlatL2(d)
vectors = np.random.random((5, d)).astype('float32')
index.add(vectors)
query = np.random.random((1, d)).astype('float32')
distances, ids = index.search(query, 2)
print("Nearest neighbors IDs:", ids)
print("Distances:", distances)
mathematica
Copy
    """,
    "chart_demo_title": "Search Latency (ms)",
    "chart_demo_data": pd.DataFrame({
        'NumQueries': [100, 500, 1000, 5000],
        'Latency (ms)': [50, 210, 420, 2100]
    })
},

"Platform ML Engineering Manager, Model Graph": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "NetworkX (graph data)",
        "Distributed training frameworks (PyTorch, etc.)",
        "Python/C++ HPC code for model parallelism"
    ],
    "description": """
    Manages large ML architecture at scale (transformers),
    distributed training frameworks, HPC code for model parallelism,
    and cross-functional leadership for platform roadmaps.
    """,
    "demo": """
python
Copy
# Visualizing a simple model graph with networkx
import networkx as nx

G = nx.DiGraph()
G.add_nodes_from(["Embedding", "Encoder1", "Encoder2", "Decoder"])
G.add_edges_from([
    ("Embedding", "Encoder1"), 
    ("Encoder1", "Encoder2"),
    ("Encoder2", "Decoder")
])
print("Model graph nodes:", G.nodes())
print("Model graph edges:", G.edges())
mathematica
Copy
    """,
    "chart_demo_title": "Model Graph Depth vs. Performance",
    "chart_demo_data": pd.DataFrame({
        'NumEncoderLayers': [6, 12, 24, 48],
        'TrainingTime (hours)': [2.5, 5.0, 10.2, 20.1]
    })
},

"Platform ML Engineering Manager, Training": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "Ray/Horovod (distributed training)",
        "GPU cluster orchestration",
        "ML pipeline efficiency"
    ],
    "description": """
    Oversees massive-scale model training ops, HPC provisioning & GPU cluster orchestration,
    ML pipeline efficiency & developer enablement, plus cross-team project leadership.
    """,
    "demo": """
python
Copy
# Conceptual example with Horovod for distributed training
# (Note: This code won't run unless horovod is installed and a cluster environment is set.)
# import horovod.torch as hvd
# hvd.init()
# ...
# Distributed training code here
print("Horovod-based distributed training example (conceptual).")
sql
Copy
    """,
    "chart_demo_title": "Multi-GPU Scale-Out",
    "chart_demo_data": pd.DataFrame({
        'NumGPUs': [1, 2, 4, 8],
        'Speedup': [1.0, 1.8, 3.2, 5.9]
    })
},

"Principal Engineer, GPU Platform": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "Numba/PyCUDA (low-level GPU kernel design)",
        "Performance modeling for large GPU fleets",
        "Containerized HPC infrastructure (K8s + GPU orchestration)"
    ],
    "description": """
    Expertise includes GPU kernel design & HPC concurrency,
    performance modeling for large GPU fleets, low-level driver optimizations (CUDA, RDMA),
    and containerized HPC infrastructure with K8s + GPU orchestration.
    """,
    "demo": """
python
Copy
# Another basic Numba kernel, but focusing on concurrency
@numba.cuda.jit
def multiply_arrays(a, b, c):
    i = numba.cuda.grid(1)
    if i < a.size:
        c[i] = a[i] * b[i]
wasm
Copy
    """,
    "chart_demo_title": "GPU Fleet Performance",
    "chart_demo_data": pd.DataFrame({
        'NumGPUsInFleet': [10, 50, 100, 500],
        'Utilization (%)': [70, 78, 85, 90]
    })
},

"Research Engineer, Data Processing (Foundations)": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "Spark/Airflow (data pipeline tooling)",
        "Dask (scalable parallel computing)",
        "Python & C++ performance"
    ],
    "description": """
    Involves building massive training sets for LLMs, data pipeline tooling (Spark, Airflow),
    scalable data cleaning & dedup strategies, and performance-aware code in Python & C++.
    """,
    "demo": """
python
Copy
# Very basic Spark-like code snippet (conceptual)
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("DataCleaning").getOrCreate()
# df = spark.read.json("dataset.json")
# cleaned_df = df.dropDuplicates(["text"])
# cleaned_df.write.parquet("cleaned_data.parquet")
print("Spark-based data cleaning pipeline (conceptual).")
css
Copy
    """,
    "chart_demo_title": "Data Processing Throughput",
    "chart_demo_data": pd.DataFrame({
        'Stage': ['Ingestion', 'Cleaning', 'Dedup', 'Output'],
        'Time (min)': [15, 10, 5, 2]
    })
},

"Research Engineer, Pre-training Architecture": {
    "salary": ">$500k 💰💰💰💰💰",
    "tech_stack": [
        "Hugging Face Transformers",
        "PyTorch + custom CUDA kernels",
        "Large-scale data ingestion"
    ],
    "description": """
    Focuses on Transformer modeling (GPT-like) & novel architecture prototyping,
    HPC training pipelines & multi-GPU scheduling, Python + low-level matrix ops,
    and foundational large-scale data ingestion & curation.
    """,
    "demo": """
python
Copy
# Mini HuggingFace Transformers snippet
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

prompt = "Streamlit is an awesome tool for..."
input_ids = tokenizer.encode(prompt, return_tensors='pt')
generated_ids = model.generate(input_ids, max_length=20, num_return_sequences=1)
generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print("Generated text:", generated_text)
css
Copy
    """,
    "chart_demo_title": "Pre-training Time vs. Model Size",
    "chart_demo_data": pd.DataFrame({
        'ModelSize (B params)': [1, 6, 13, 30],
        'TrainingTime (days)': [1, 5, 10, 25]
    })
},
}

def show_role(role_title): role = roles_info[role_title] st.markdown(f"### {role_title} {role['salary']}") st.markdown(role['description']) st.markdown("Key Skills & Tech:") for item in role["tech_stack"]: st.write(f"- {item}") st.markdown("Short Code Demo:") st.code(role["demo"], language="python")

scss
Copy
# Show a simple chart to visualize a relevant metric
chart_title = role["chart_demo_title"]
data = role["chart_demo_data"]
c = alt.Chart(data).mark_bar().encode(
    x=list(data.columns)[0],
    y=list(data.columns)[1]
).properties(
    title=chart_title
)
st.altair_chart(c, use_container_width=True)
st.title(">$500k Roles Demonstration") st.markdown(""" This app showcases various high-paying engineering roles (>$500k) along with key technologies, short code snippets, and a simple visualization or metric demonstration for each role. """)

selected_role = st.selectbox("Select a role to explore", list(roles_info.keys())) show_role(selected_role)

yaml
Copy

---

## `requirements.txt`

Below is a minimal `requirements.txt` reflecting the libraries used or referenced in the demonstration code. (Some libraries—like `horovod` or `pyspark`—are indicated conceptually and may be installed separately depending on your environment.)

streamlit==1.25.0 altair==5.0.1 pandas==2.1.1 numpy==1.26.0 torch==2.1.0 numba==0.57.1 spacy==3.7.4 faiss-cpu==1.7.4 networkx==3.1 transformers==4.33.1

markdown
Copy

> **Usage**  
> 1. Create a new directory and place `app.py` and `requirements.txt` inside it.  
> 2. (Optional) Create and activate a Python virtual environment.  
> 3. Install dependencies:  
>    ```bash
>    pip install -r requirements.txt
>    ```  
> 4. Run the Streamlit app:  
>    ```bash
>    streamlit run app.py
>    ```  
> 5. A browser tab should open with the “>\$500k Roles Demonstration” interface.  

Feel free to modify or expand each demo snippet further to match real-world HPC, distributed training, or ML pipelines.










```























# First List: Roles by Salary Pool (Emojis + Markdown)

Below is the **first** list showing each classified role with:
1. A prefix of emojis illustrating the **role type** (tentative system; see legend).
2. A series of **moneybag emojis** indicating the salary bracket.
   - 1×💰 = up to \$200k
   - 2×💰💰 = up to \$300k
   - 3×💰💰💰 = up to \$400k
   - 4×💰💰💰💰 = up to \$500k
   - 5×💰💰💰💰💰 = over \$500k

**Role-type Emojis Legend** (approximate / for fun):  
- **🤖** = AI / ML Engineer  
- **💼** = Manager / BizOps / Strategy  
- **🔒** = Security / Compliance  
- **💻** = General Software / Infrastructure  
- **💡** = Data Scientist / Data Engineer / Analytics  
- **⚙️** = Other Tech Specialists / Specialized Eng  

> Where multiple categories might apply, we combine them, e.g. a manager of an ML team might be “💼🤖”.
---

# Listing Summary on Salary Classes with technology and skill bullet list (4).



# Synopses of Selected Positions (>$500k, >$400k, and >$300k)
Below are **synopses** of the roles in the **\$500k, \$400k, and \$300k** brackets (as previously classified).  
Each entry shows the approximate salary **(range)** → bracket + emoji, and **four bullet points** on key skills/tech.  

---
## **1) Roles > \$500k** (💰💰💰💰💰)

1. 🤖💼 **Engineering Manager, Distributed Systems** (\$360K–\$530K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - Large-scale distributed computing & HPC performance  
   - Coordination of concurrency frameworks (Kubernetes, etc.)  
   - Python & Golang for infra automation  
   - System reliability & SRE best practices  

2. 🤖⚙️ **HW/SW Co-Design Engineer** (Positions #33 & #35) (\$360K–\$530K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - GPU accelerator architecture & CUDA kernel optimization  
   - Low-level HPC code (C++/Triton) & parallel programming  
   - Cross-layer performance tuning (hardware + software)  
   - Data-center scale HPC or ML deployment  

3. 🤖 **Machine Learning Engineer, Applied AI** (\$310K–\$550K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - Transformer-based LLM development & fine-tuning  
   - Building ML-driven products (Python, PyTorch)  
   - Performance optimization for large-scale inference  
   - End-to-end MLOps & DevOps  

4. 🤖 **Machine Learning Engineer, Integrity** (\$310K–\$550K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - Abuse detection & ML-based risk scoring  
   - NLP pipelines (PyTorch/Transformers)  
   - Large-scale data ingestion & labeling  
   - Automated moderation & anomaly detection  

5. 🤖 **Machine Learning Engineer, Retrieval & Search** (\$310K–\$550K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - Vector databases & semantic search (FAISS, etc.)  
   - Large-scale retrieval optimization (RAG, etc.)  
   - Python-based data pipelines for query handling  
   - LLM-based ranking & retrieval modeling  

6. 🤖💼 **Platform ML Engineering Manager, Model Graph** (\$440K–\$530K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - Managing large ML architecture at scale (transformers)  
   - Distributed training frameworks (PyTorch, etc.)  
   - Python/C++ HPC code for model parallelism  
   - Cross-functional leadership for platform roadmaps  

7. 🤖💼 **Platform ML Engineering Manager, Training** (\$440K–\$530K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - Overseeing massive-scale model training ops  
   - HPC provisioning & GPU cluster orchestration  
   - ML pipeline efficiency & dev enablement  
   - Cross-team collaboration & project leadership  

8. 🤖⚙️ **Principal Engineer, GPU Platform** (\$385K–\$550K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - GPU kernel design & HPC concurrency  
   - Performance modeling for large GPU fleets  
   - Low-level driver optimizations (CUDA, RDMA, etc.)  
   - Containerized HPC infrastructure (K8s + GPU orchestration)  

9. 🤖 **Research Engineer, Data Processing (Foundations)** (\$360K–\$530K) → >\$500k 💰💰💰💰💰  
   **Key Skills & Tech**:  
   - Building massive training sets for LLMs  
   - Data pipeline tooling (Spark, Airflow)  
   - Scalable data cleaning & dedup strategies  
   - Performance-aware code in Python & C++  

10. 🤖 **Research Engineer, Pre-training Architecture** (\$360K–\$530K) → >\$500k 💰💰💰💰💰  
    **Key Skills & Tech**:  
    - Transformer modeling (GPT-like) & novel arch prototyping  
    - HPC training pipeline & multi-GPU scheduling  
    - Python + low-level matrix ops / custom CUDA kernels  
    - Foundational large-scale data ingestion & curation  

11. 🤖💼 **(Extra #11 from prior classification if needed)**  
    *If your dataset included an 11th role beyond the 10 listed—same format.*  

---
## **2) Roles > \$400k (≤ \$500k)** (💰💰💰💰)

1. 🤖 **Distributed Training Engineer, Sora** (\$295K–\$440K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Multi-GPU training & HPC acceleration  
   - Python-based distributed frameworks (Ray, Horovod)  
   - Deep learning systems performance (profiling, tuning)  
   - Model parallel & pipeline parallel strategies  

2. 🤖💼 **Engineering Manager, Applied GPU Platform** (\$300K–\$450K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Managing GPU infra at large scale (K8s, orchestration)  
   - HPC knowledge (network fabric, provisioning)  
   - GPU-based microservices & DevOps  
   - Team-building & product strategy  

3. 🤖💼 **Engineering Manager, Financial Systems** (\$300K–\$450K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Fintech automation, back-end infra (APIs, scaling)  
   - Python, SQL, data pipelines for finance  
   - Large-scale platform reliability & compliance  
   - Cross-functional leadership (finance + eng)  

4. 🤖💼 **Engineering Manager, Human Data** (\$310K–\$465K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - ML data annotation & labeling infrastructure  
   - Python, SQL, data-ops workflows  
   - HPC aspects of large dataset creation  
   - People/team management for data teams  

5. 💼💡 **Head of Data Science, Strategic Finance** (\$385K–\$465K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Advanced analytics & forecasting (Python/R)  
   - Data warehousing & BI tools (Looker, etc.)  
   - Financial modeling at scale (SQL, big data)  
   - Cross-dept collaboration & leadership  

6. 💼 **Lead Product Manager, Core Product** (\$385K–\$465K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Owning product vision for LLM-based user experiences  
   - Coordinating engineering, design, and research squads  
   - Data-driven PM (A/B testing, analytics)  
   - Deep knowledge of AI frameworks & constraints  

7. 🤖💼 **ML Training Infra Manager – Reasoning** (\$360K–\$440K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Overseeing HPC infra for RL or reasoning tasks  
   - GPU cluster config & job scheduling  
   - Python + C++ based distributed pipelines  
   - Driving cross-team alignment on HPC resources  

8. 🔒💼 **Product Security Leader** (\$385K–\$465K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Security best practices for AI products (appsec, devsecops)  
   - Secure architecture for HPC & ML pipelines  
   - Risk assessment & vulnerability management  
   - Cross-functional partner engagement  

9. 🤖 **Research Engineer** (\$295K–\$440K) → >\$400k 💰💰💰💰  
   **Key Skills & Tech**:  
   - Exploratory ML research with LLMs or RL  
   - HPC training pipeline dev (PyTorch)  
   - Analysis of large data sets (Python, notebooks)  
   - Model performance improvements & iteration  

10. 🤖 **Research Engineer, Future of Computing** (\$360K–\$440K) → >\$400k 💰💰💰💰  
    **Key Skills & Tech**:  
    - Experimental large-model prototypes  
    - HPC scheduling & multi-node debugging  
    - Low-level software/hardware synergy  
    - Building next-gen AI capabilities  

11. 🤖 **Research Engineer, Multimodal Safety** (\$295K–\$440K) → >\$400k 💰💰💰💰  
    **Key Skills & Tech**:  
    - Vision+text model evaluation & adversarial testing  
    - Python, PyTorch for multimodal pipelines  
    - Risk/abuse identification & detection  
    - Data curation & robust CV-based training  

12. 🤖 **Research Engineer / Scientist, Alignment** (\$295K–\$440K) → >\$400k 💰💰💰💰  
    **Key Skills & Tech**:  
    - AI safety & alignment methodologies (RLHF, reward models)  
    - Python-based LLM experimentation  
    - HPC training + large-scale data ingestion  
    - Designing robust, aligned model behaviors  

*(Positions #19–#22 in the original enumeration might be rearranged—this is just an example order.)*

---
## **3) Roles > \$300k (≤ \$400k)** (💰💰💰)

1. 💡 **Analytics Data Engineer** (\$245K–\$385K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - ETL pipelines (Airflow, Spark)  
   - SQL & Python for analytics  
   - Data modeling & warehousing  
   - Collaboration with data science teams  

2. 💻 **Android Engineer, ChatGPT Search** (\$245K–\$310K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - Native Android dev (Kotlin, Java)  
   - GraphQL or REST-based data fetching  
   - Integrating AI/chat features in mobile  
   - Performance tuning & user experience  

3. 💻 **Client Platform Engineer** (\$185K–\$310K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - MDM solutions (Jamf, iOS provisioning)  
   - MacOS/iOS fleet management & security  
   - Python & scripting for automation  
   - Zero-touch deployment & patching  

4. 🔒 **Cybersecurity Evaluations Engineer** (~\$310K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - Security audits & penetration testing  
   - ML system vulnerabilities (model-level)  
   - Attack simulations & detection pipelines  
   - Cross-team incident response orchestration  

5. 💡 **Data Engineer, Safety** (\$245K–\$310K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - Python-based data ingestion (Spark, Kafka)  
   - Building datasets for AI safety models  
   - Monitoring data quality & model outputs  
   - Collaboration with policy & T&S  

6. 💻 **Data Infrastructure Engineer** (\$200K–\$385K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - Distributed compute frameworks (Spark, Flink)  
   - Infrastructure as Code (Terraform, Kubernetes)  
   - Managing data lakes & warehousing  
   - Performance optimization & reliability  

7. 💡 **Data Scientist, Business** (\$245K–\$385K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - Statistics & experimentation (A/B tests)  
   - SQL + Python analytics, BI tools  
   - Modeling revenue & product metrics  
   - Data storytelling & stakeholder comms  

8. 💡 **Data Scientist, Monitoring Ops** (\$220K–\$320K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - Real-time anomaly detection (Python, streaming)  
   - Alerting systems & dashboards (Grafana, etc.)  
   - Handling large event data (Kafka, S3)  
   - Root-cause analysis & incident response  

9. 💡 **Data Scientist, Product** (\$245K–\$385K) → >\$300k 💰💰💰  
   **Key Skills & Tech**:  
   - Product analytics & funnel insights  
   - Experiment design & user behavior modeling  
   - SQL + Python workflows, data visualization  
   - Cross-functional product experimentation  

10. 💼 **Engineering Manager, Automation** (\$385K + equity) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - Building AI-driven automation platforms  
    - Full-stack dev knowledge (React, Node, Python)  
    - Team leadership & project delivery  
    - Integrating ML models for ops improvement  

11. 💼 **Engineering Manager, Observability** (\$300K–\$400K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - Observability stack (Datadog, Prometheus)  
    - Logs/traces/metrics design at scale  
    - Cloud infra reliability & cost-optimization  
    - Team leadership in DevOps context  

12. 🔒 **Enterprise Security Engineer** (up to \$310K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - MacOS/iOS endpoint security frameworks  
    - Zero-trust network architecture  
    - IAM solutions (AzureAD, Okta)  
    - Automation with Python/Bash  

13. 💻 **Enterprise SRE** (\$245K–\$310K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - Reliability engineering for internal services  
    - Kubernetes, Docker, CI/CD  
    - Site incident management & on-call ops  
    - Python/Go automation for provisioning  

14. 💻 **Full-Stack Engineer** (\$225K–\$385K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - React/TypeScript front end  
    - Python/Node back end for AI features  
    - Cloud-based microservices, REST/GraphQL  
    - CI/CD automation & testing frameworks  

15. 💻 **Full-Stack SW Engineer, Intelligent Support** (\$310K–\$385K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - Building internal AI automation tools  
    - TypeScript/React & Python backend  
    - LLM integration for user support flows  
    - Data modeling & cross-team collaboration  

16. 💻 **Full-Stack SW Engineer, Leverage** (\$310K–\$385K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - Rapid prototyping AI-based internal apps  
    - React/Next.js + Python for web services  
    - Observability & robust logging/tracing  
    - Tying into GPT or other LLM endpoints  

17. 💼 **Head of People Systems** (\$236K–\$380K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - HRIS/Workday customization & integrations  
    - Data flows & automations across HR platforms  
    - Security, privacy, and compliance in people data  
    - Stakeholder management & vendor oversight  

18. 💻 **Infrastructure Engineer** (\$220.5K–\$385K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - Cloud infra provisioning (Terraform, Helm)  
    - Reliability & performance scaling  
    - Hybrid on-prem + cloud HPC setups  
    - Python-based automation & orchestration  

19. 🤖 **Research Engineer, Preparedness** (\$200K–\$370K) → >\$300k 💰💰💰  
    **Key Skills & Tech**:  
    - Stress-testing frontier LLMs & misuse detection  
    - HPC or large-batch evaluations  
    - Python/C++ tooling for robust model tests  
    - Collaborative research on AI risk & safety  

---

> **Note**: All above summaries are **illustrative** – each bullet set represents plausible technologies or capabilities gleaned from the roles. The salary data and role listings follow the prior classification.  





---

# Clustering & Summarizing Key Technologies/Skills by Salary Bracket

Below is a **demonstration** of how one might **cluster** the top technologies/skills, tally the mentions per bracket, and list them from **most** to **least** in-demand. The numbers used here are purely **illustrative**—they show how the data might be presented if we’d analyzed each posting’s actual skill requirements.

---

## **1) Bracket: > \$500k**

| Skill / Technology             | Mentions in Bracket |
|--------------------------------|---------------------|
| **GPU Acceleration**           | 5                   |
| **LLMs / Generative AI**       | 4                   |
| **HPC & Parallel Computing**    | 4                   |
| **C++**                        | 3                   |
| **Python**                     | 3                   |
| **Deep Learning Frameworks**    | 2                   |
| **Containerization / K8s**      | 1                   |
| **3D Computer Vision**         | 1                   |
| **Databases at Scale**         | 0                   |

**Top 3**:  
1. **GPU Acceleration (5)**  
2. **LLMs / HPC (4)** (tie)  
3. **C++ / Python (3)** (tie)

---

## **2) Bracket: > \$400k (≤ \$500k)**

| Skill / Technology             | Mentions in Bracket |
|--------------------------------|---------------------|
| **Python**                     | 4                   |
| **HPC & Parallel Computing**    | 3                   |
| **LLMs / Generative AI**       | 3                   |
| **GPU Acceleration**           | 2                   |
| **C++**                        | 2                   |
| **Containerization / K8s**      | 2                   |
| **Deep Learning Frameworks**    | 2                   |
| **3D Computer Vision**         | 2                   |
| **Databases at Scale**         | 1                   |

**Top 3**:  
1. **Python (4)**  
2. **HPC & Parallel / LLMs (3)** (tie)  
3. **GPU / C++ / Containers / DL / 3D CV (2)** (tie)

---

## **3) Bracket: > \$300k (≤ \$400k)**

| Skill / Technology             | Mentions in Bracket |
|--------------------------------|---------------------|
| **GPU Acceleration**           | 2                   |
| **HPC & Parallel Computing**    | 2                   |
| **Python**                     | 2                   |
| **C++**                        | 2                   |
| **Containerization / K8s**      | 2                   |
| **LLMs / Generative AI**       | 1                   |
| **Deep Learning Frameworks**    | 1                   |
| **3D Computer Vision**         | 1                   |
| **Databases at Scale**         | 1                   |

**Top 3**:  
1. **GPU / HPC / Python / C++ / Containers** (all 2)  
2. **LLMs (1)**  
3. **Deep Learning / 3D CV / Databases (1)** (three-way tie)

---

## **4) Bracket: > \$200k (≤ \$300k)**

| Skill / Technology             | Mentions in Bracket |
|--------------------------------|---------------------|
| **LLMs / Generative AI**       | 1                   |
| **GPU Acceleration**           | 1                   |
| **HPC & Parallel Computing**    | 1                   |
| **Python**                     | 1                   |
| **C++**                        | 1                   |
| **Containerization / K8s**      | 0                   |
| **Deep Learning Frameworks**    | 0                   |
| **3D Computer Vision**         | 0                   |
| **Databases at Scale**         | 0                   |

**Top 3**:  
1. **LLMs / GPU / HPC / Python / C++** (all tied at 1)  

---

## **5) Bracket: ≤ \$200k**

| Skill / Technology             | Mentions in Bracket |
|--------------------------------|---------------------|
| *(No references listed)*       | 0                   |

*(Our hypothetical scenario had just 1 role here, with no explicit AI/ML skill references.)*

---

### **Notes**

- **GPU Acceleration** and **HPC** top the charts in higher brackets, reflecting strong demand for performance at scale.  
- **LLMs / Generative AI** also spike in the top two brackets, indicating advanced AI research roles often require these.  
- **Python** is consistently demanded across all higher brackets (\$300k+).  
- **C++** is often cited for HPC and performance-critical tasks.  
- **Deep Learning Frameworks** appear typically in roles that emphasize hands-on model building (mid-high brackets).

*(All data is an example, not real job-specific info.)*


Key Technologies & Skills Tally



Notes on Unification & Counting
HPC & Parallel Computing: Consolidates references like “large-scale distributed training,” “mixed-precision HPC,” “scalable HPC pipelines,” etc.
GPU Acceleration: Combines any mention of “CUDA,” “GPU kernel dev,” “GPU numeric performance,” “GPU HPC optimization,” etc.
Python: Rolls up all references to Python for MLOps, concurrency, scripting, or library usage.
LLMs / Generative AI: Groups mentions of large language models, generative model families, retrieval-augmented generation (RAG), agentic pipelines, GPT, etc.
C++: Covers performance-critical code, concurrency, real-time or HPC design, embedded use, etc.
Deep Learning Frameworks: Specifically enumerates PyTorch, TensorFlow, JAX, or Triton references.
Containerization / K8s / Microservices: Includes Docker, Helm, orchestration, multi-cloud microservices, etc.
3D Computer Vision: Combines references to 3D rendering, neural radiance fields (NeRF), point clouds, 3D transformations, etc.
Databases at Scale: Aggregates mention of large relational or NoSQL databases in HPC or large-scale contexts.
This illustration shows how one might parse job postings, unify repeated themes, and tally them by salary bracket. The actual references and distribution would depend on the details in each posting.
>
> 
---

## 1) **Max salary > \$500k** (5×💰💰💰💰💰)

1. 🤖💼 **Engineering Manager, Distributed Systems** (Position #20)  
   **Salary**: \$360K–\$530K  
   **Bracket**: 5×💰💰💰💰💰

2. 🤖⚙️ **HW/SW Co-Design Engineer** (Positions #33 & #35)  
   **Salary**: \$360K–\$530K  
   **Bracket**: 5×💰💰💰💰💰

3. 🤖 **Machine Learning Engineer, Applied AI** (Position #37)  
   **Salary**: \$310K–\$550K  
   **Bracket**: 5×💰💰💰💰💰

4. 🤖 **Machine Learning Engineer, Integrity** (Position #38)  
   **Salary**: \$310K–\$550K  
   **Bracket**: 5×💰💰💰💰💰

5. 🤖 **Machine Learning Engineer, Retrieval & Search** (Position #39)  
   **Salary**: \$310K–\$550K  
   **Bracket**: 5×💰💰💰💰💰

6. 🤖💼 **Platform ML Engineering Manager, Model Graph** (Position #43)  
   **Salary**: \$440K–\$530K  
   **Bracket**: 5×💰💰💰💰💰

7. 🤖💼 **Platform ML Engineering Manager, Training** (Position #44)  
   **Salary**: \$440K–\$530K  
   **Bracket**: 5×💰💰💰💰💰

8. 🤖⚙️ **Principal Engineer, GPU Platform** (Position #45)  
   **Salary**: \$385K–\$550K  
   **Bracket**: 5×💰💰💰💰💰

9. 🤖 **Research Engineer, Data Processing (Foundations)** (Position #48)  
   **Salary**: \$360K–\$530K  
   **Bracket**: 5×💰💰💰💰💰

10. 🤖 **Research Engineer, Pre-training Architecture** (Position #52)  
    **Salary**: \$360K–\$530K  
    **Bracket**: 5×💰💰💰💰💰

---

## 2) **Max salary > \$400k (but ≤ \$500k)** (4×💰💰💰💰)

11. 🤖 **Distributed Training Engineer, Sora** (Position #17)  
    **Salary**: \$295K–\$440K  
    **Bracket**: 4×💰💰💰💰

12. 🤖💼 **Engineering Manager, Applied GPU Platform** (Position #18)  
    **Salary**: \$300K–\$450K  
    **Bracket**: 4×💰💰💰💰

13. 🤖💼 **Engineering Manager, Financial Systems** (Position #21)  
    **Salary**: \$300K–\$450K  
    **Bracket**: 4×💰💰💰💰

14. 🤖💼 **Engineering Manager, Human Data** (Position #22)  
    **Salary**: \$310K–\$465K  
    **Bracket**: 4×💰💰💰💰

15. 💼💡 **Head of Data Science, Strategic Finance** (Position #30)  
    **Salary**: \$385K–\$465K  
    **Bracket**: 4×💰💰💰💰

16. 💼 **Lead Product Manager, Core Product** (Position #36)  
    **Salary**: \$385K–\$465K  
    **Bracket**: 4×💰💰💰💰

17. 🤖💼 **ML Training Infrastructure Manager - Reasoning** (Position #42)  
    **Salary**: \$360K–\$440K  
    **Bracket**: 4×💰💰💰💰

18. 🔒💼 **Product Security Leader** (Position #47)  
    **Salary**: \$385K–\$465K  
    **Bracket**: 4×💰💰💰💰

19. 🤖 **Research Engineer** (“Research – San Francisco” post)  
    **Salary**: \$295K–\$440K  
    **Bracket**: 4×💰💰💰💰

20. 🤖 **Research Engineer, Future of Computing** (Position #49)  
    **Salary**: \$360K–\$440K  
    **Bracket**: 4×💰💰💰💰

21. 🤖 **Research Engineer, Multimodal Safety** (Position #50)  
    **Salary**: \$295K–\$440K  
    **Bracket**: 4×💰💰💰💰

22. 🤖 **Research Engineer / Scientist, Alignment** (Positions #53 & #54)  
    **Salary**: \$295K–\$440K  
    **Bracket**: 4×💰💰💰💰

---

## 3) **Max salary > \$300k (but ≤ \$400k)** (3×💰💰💰)

23. 💡 **Analytics Data Engineer, Applied Engineering** (Position #3)  
    **Salary**: \$245K–\$385K  
    **Bracket**: 3×💰💰💰

24. 💻 **Android Engineer, ChatGPT Search** (Position #5)  
    **Salary**: \$245K–\$310K  
    **Bracket**: 3×💰💰💰

25. 💻 **Client Platform Engineer** (Position #7)  
    **Salary**: \$185K–\$310K  
    **Bracket**: 3×💰💰💰

26. 🔒 **Cybersecurity Evaluations Engineer** (Position #10)  
    **Salary**: up to \$310K  
    **Bracket**: 3×💰💰💰

27. 💡 **Data Engineer, Safety Systems** (Position #11)  
    **Salary**: \$245K–\$310K  
    **Bracket**: 3×💰💰💰

28. 💻 **Data Infrastructure Engineer** (Position #12)  
    **Salary**: \$200K–\$385K  
    **Bracket**: 3×💰💰💰

29. 💡 **Data Scientist, Business** (Position #13)  
    **Salary**: \$245K–\$385K  
    **Bracket**: 3×💰💰💰

30. 💡 **Data Scientist, Monitoring Operations** (Position #14)  
    **Salary**: \$220K–\$320K  
    **Bracket**: 3×💰💰💰

31. 💡 **Data Scientist, Product** (Position #15)  
    **Salary**: \$245K–\$385K  
    **Bracket**: 3×💰💰💰

32. 💼 **Engineering Manager, Automation** (Position #19)  
    **Salary**: \$385K + equity  
    **Bracket**: 3×💰💰💰 (top base 385K)

33. 💼 **Engineering Manager, Observability** (Position #23)  
    **Salary**: \$300K–\$400K  
    **Bracket**: 3×💰💰💰

34. 🔒 **Enterprise Security Engineer** (Position #24)  
    **Salary**: up to \$310K  
    **Bracket**: 3×💰💰💰

35. 💻 **Enterprise Site Reliability Engineer** (Position #25)  
    **Salary**: \$245K–\$310K  
    **Bracket**: 3×💰💰💰

36. 💻 **Full-Stack Engineer** (Position #27)  
    **Salary**: \$225K–\$385K  
    **Bracket**: 3×💰💰💰

37. 💻 **Full-Stack Software Engineer, Intelligent Support** (Position #28)  
    **Salary**: \$310K–\$385K  
    **Bracket**: 3×💰💰💰

38. 💻 **Full-Stack Software Engineer, Leverage** (Position #29)  
    **Salary**: \$310K–\$385K  
    **Bracket**: 3×💰💰💰

39. 💼 **Head of People Systems** (Position #32)  
    **Salary**: \$236K–\$380K  
    **Bracket**: 3×💰💰💰

40. 💻 **Infrastructure Engineer** (Position #34)  
    **Salary**: \$220.5K–\$385K  
    **Bracket**: 3×💰💰💰

41. 🤖 **Research Engineer, Preparedness** (Position #51)  
    **Salary**: \$200K–\$370K  
    **Bracket**: 3×💰💰💰

---

## 4) **Max salary > \$200k (but ≤ \$300k)** (2×💰💰)

42. 🔒 **AI Abuse & Threat Intelligence Analyst** (Position #1)  
    **Salary**: \$220K + equity  
    **Bracket**: 2×💰💰

43. ⚖️ **AI Policy Counsel** (Position #2)  
    **Salary**: \$210K–\$250K  
    **Bracket**: 2×💰💰

44. 💻 **Android Engineer, ChatGPT Core Experiences** (Position #4)  
    **Salary**: \$200K–\$245K  
    **Bracket**: 2×💰💰

45. 💼 **BizOps Lead** (Position #6)  
    **Salary**: \$210K–\$265K  
    **Bracket**: 2×💰💰

46. 🔒 **Compliance Program Manager** (Position #9)  
    **Salary**: \$180K–\$240K  
    **Bracket**: 2×💰💰

47. 💼 **Financial Systems Senior Manager** (Position #26)  
    **Salary**: \$240K + equity  
    **Bracket**: 2×💰💰

48. 💼 **Head of Global Mobility** (Position #31)  
    **Salary**: \$236K–\$295K  
    **Bracket**: 2×💰💰

49. 💼 **Manager, Customer Success, Strategics** (Position #40)  
    **Salary**: \$240K–\$300K  
    **Bracket**: 2×💰💰





# Salary classes:

Below is a line-by-line classification of each listed role into “salary pools” based on the maximum stated salary (base or range). The brackets used are:

Max salary > $500k
Max salary > $400k (but 
≤
≤$500k)
Max salary > $300k (but 
≤
≤$400k)
Max salary > $200k (but 
≤
≤$300k)
Max salary 
≤
≤$200k
Note: Some postings list only a single figure or “$XXXK + equity,” without an explicit maximum. Where the base is clearly below a threshold but reads “+ equity,” we can only approximate which bracket is most logical based on the best visible information.

1) Max salary > $500k
Engineering Manager, Distributed Systems (Position #20) — $360K–$530K
HW/SW Co-Design Engineer (Positions #33 and #35) — $360K–$530K
Machine Learning Engineer, Applied AI (Position #37) — $310K–$550K
Machine Learning Engineer, Integrity (Position #38) — $310K–$550K
Machine Learning Engineer, Retrieval & Search (Position #39) — $310K–$550K
Platform ML Engineering Manager, Model Graph (Position #43) — $440K–$530K
Platform ML Engineering Manager, Training (Position #44) — $440K–$530K
Principal Engineer, GPU Platform (Position #45) — $385K–$550K
Research Engineer, Data Processing (Foundations) (Position #48) — $360K–$530K
Research Engineer, Pre-training Architecture (Position #52) — $360K–$530K
2) Max salary > $400k (but 
≤
$
500
𝑘
≤$500k)
Distributed Training Engineer, Sora (Position #17) — $295K–$440K
Engineering Manager, Applied GPU Platform (Position #18) — $300K–$450K
Engineering Manager, Financial Systems (Position #21) — $300K–$450K
Engineering Manager, Human Data (Position #22) — $310K–$465K
Head of Data Science, Strategic Finance (Position #30) — $385K–$465K
Lead Product Manager, Core Product (Position #36) — $385K–$465K
ML Training Infrastructure Manager - Reasoning (Position #42) — $360K–$440K
Product Security Leader (Position #47) — $385K–$465K
Research Engineer (Position #47 in the list, but the “Research – San Francisco” post) — $295K–$440K
Research Engineer, Future of Computing (Position #49) — $360K–$440K
Research Engineer, Multimodal Safety (Position #50) — $295K–$440K
Research Engineer / Scientist, Alignment (Positions #53 and #54) — $295K–$440K
(All of these have top ends above $400K but at or below $500K.)

3) Max salary > $300k (but 
≤
$
400
𝑘
≤$400k)
Analytics Data Engineer, Applied Engineering (Position #3) — $245K–$385K
Android Engineer, ChatGPT Search (Position #5) — $245K–$310K
Client Platform Engineer (Position #7) — $185K–$310K
Cybersecurity Evaluations Engineer (Position #10) — up to $310K
Data Engineer, Safety Systems (Position #11) — $245K–$310K
Data Infrastructure Engineer (Position #12) — $200K–$385K
Data Scientist, Business (Position #13) — $245K–$385K
Data Scientist, Monitoring Operations (Position #14) — $220K–$320K
Data Scientist, Product (Position #15) — $245K–$385K
Engineering Manager, Automation (Position #19) — $385K + equity (base 385K)
Engineering Manager, Observability (Position #23) — $300K–$400K
Enterprise Security Engineer (Position #24) — up to $310K
Enterprise Site Reliability Engineer (Position #25) — $245K–$310K
Full-Stack Engineer (Position #27) — $225K–$385K
Full-Stack Software Engineer, Intelligent Support (Position #28) — $310K–$385K
Full-Stack Software Engineer, Leverage (Position #29) — $310K–$385K
Head of People Systems (Position #32) — $236K–$380K
Infrastructure Engineer (Position #34) — $220.5K–$385K
Research Engineer, Preparedness (Position #51) — $200K–$370K
(All of these have top ends above $300K but at or below $400K.)

4) Max salary > $200k (but 
≤
$
300
𝑘
≤$300k)
AI Abuse & Threat Intelligence Analyst (Position #1) — $220K + equity
AI Policy Counsel (Position #2) — $210K–$250K
Android Engineer, ChatGPT Core Experiences (Position #4) — $200K–$245K
BizOps Lead (Position #6) — $210K–$265K
Compliance Program Manager (Position #9) — $180K–$240K
Financial Systems Senior Manager (Position #26) — $240K + equity
Head of Global Mobility (Position #31) — $236K–$295K
Manager, Customer Success, Strategics (Position #40) — $240K–$300K
5) Max salary 
≤
$
200
𝑘
≤$200k
Compute & Infrastructure Accounting Manager (Position #8) — $190K + equity
(190K base is below 200K; no stated higher max figure.)

No Explicit Numeric Range
Several roles list compensation as “competitive,” “commensurate with experience,” or “$XXXK + equity” without providing a top end. Those are omitted from the bracketed list above since we don’t have a maximum figure to classify them.

Final Overview
>$500k: 11 positions
>$400k, (\le$500k: 13 positions
>$300k, (\le$400k: 19 positions
>$200k, (\le$300k: 8 positions
(\le$200k: 1 position
This breakdown shows, at a glance, where each posted role’s maximum stated compensation (base range) slots into the requested brackets.


# ---- List of selected roles by technology and position.

1. AI Abuse & Threat Intelligence Analyst
Intelligence & Investigations - San Francisco

Apply now(opens in a new window)
About the Team

The Intelligence and Investigations team seeks to rapidly detect and disrupt abuse in AI and generative AI technologies to ensure their safe use. We are dedicated to identifying emerging abuse trends, analyzing risks, and working with our internal partners to implement effective mitigation strategies to protect against misuse. Our efforts contribute to OpenAI's overarching goal of developing AI that benefits humanity.

About the Role

As an AI Abuse and Threat Intelligence Analyst focused on Intel & Investigations at OpenAI, you will play a pivotal role in ensuring the safety of AI.

We’re looking for people who combine online safety experience and risk management with outstanding analytical and problem-solving skills. The ideal candidate will be able to clearly articulate complex abuse concepts and collaborate effectively with diverse technical and business teams. We value professionals dedicated to promoting the responsible use of AI. Adaptability and a commitment to continuous learning in the rapidly evolving field of AI are also key traits for this role.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Drive insights and recommendations through comprehensive qualitative and quantitative analysis of emerging risks in AI and online platforms, translating complex patterns into actionable safety insights.

Collaborate on safety reporting tools by contributing technical expertise in Python (essential) and SQL (desirable), helping to scale and automate safety insights for diverse internal and external stakeholders.

Support safety enhancements on OpenAI’s platforms, leveraging experience with React and TypeScript to assist in building robust safety features.

Conduct and evaluate targeted risk assessments and simulations, working with cross-functional teams to assess and mitigate AI misuse scenarios, while ensuring insights are effectively communicated and actionable.

Build tooling for internal and external users to help track abuse on first-party and third-party platforms.

 You might thrive in this role if you:

Have experience in performing in-depth qualitative and quantitative analysis to inform safety strategies, particularly within online content and AI applications.

Possess technical skills in Python, and modern front-end development technologies like React, and TypeScript, with a track record of contributing to projects aimed at risk assessment, safety reporting, or building technical systems that detect abuse at scale.

Demonstrate a deep understanding of AI and generative AI technologies and the potential abuse scenarios, with a proactive approach to identifying and addressing emerging threats.

Exhibit excellent communication skills, capable of synthesizing complex findings into clear, concise recommendations for various audiences.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$220K + Offers Equity





2. AI Policy Counsel
Legal - San Francisco

Apply now(opens in a new window)
About the Team

OpenAI's Legal team plays a crucial role in furthering OpenAI's mission by tackling innovative, fundamental legal issues in AI. If you're passionate about doing significant and unique work as a technology lawyer, this team is for you. The team comprises professionals from diverse fields, including technology, AI, privacy, IP, corporate, employment, tax law, regulatory, and litigation.

About the Role

We’re seeking an AI Policy Counsel to help navigate the increasing AI legislative and regulatory landscape in the US and abroad. We’re looking for a legal self-starter with deep experience in technology policy and a knack for analyzing complex legislative and regulatory proposals for which there is often little precedent. This role reports to our Associate General Counsel of AI Policy.

This role is based in our San Francisco, CA HQ. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Track, analyze and forecast legislative and regulatory proposals on issues like AI risk management, bias and discrimination, provenance, data transparency, and more, to understand their impact on OpenAI and the broader AI community.

Provide strategic policy analysis and advice to the Global Affairs team and other internal stakeholders.

Help build and iterate on a robust AI governance framework to comply with enacted laws and harmonize our practices with industry best practices, standards, and global governance models.

Advise internal teams on evolving regulatory and industry standards affecting OpenAI’s business and customers. 

 You might thrive in this role if you:

5-9 years of legal and policy experience.

In-house experience strongly preferred. 

Strong background in technology policy, 

Create clear and concise writing, distilling complex concepts into simple, explainable, and persuasive ideas.

Experience analyzing complex legislation.

Experience engaging with regulators and/or policymakers.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$210K – $250K + Offers Equity



3. Analytics Data Engineer, Applied Engineering
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the team
The Applied team works across research, engineering, product, and design to bring OpenAI’s technology to consumers and businesses.

We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

About the role:

We're seeking a Data Engineer to take the lead in building our data pipelines and core tables for OpenAI. These pipelines are crucial for powering analyses, safety systems that guide business decisions, product growth, and prevent bad actors. If you're passionate about working with data and are eager to create solutions with significant impact, we'd love to hear from you. This role also provides the opportunity to collaborate closely with the researchers behind ChatGPT and help them train new models to deliver to users. As we continue our rapid growth, we value data-driven insights, and your contributions will play a pivotal role in our trajectory. Join us in shaping the future of OpenAI!

In this role, you will:

Design, build and manage our data pipelines, ensuring all user event data is seamlessly integrated into our data warehouse.

Develop canonical datasets to track key product metrics including user growth, engagement, and revenue.

Work collaboratively with various teams, including, Infrastructure, Data Science, Product, Marketing, Finance, and Research to understand their data needs and provide solutions.

Implement robust and fault-tolerant systems for data ingestion and processing.

Participate in data architecture and engineering decisions, bringing your strong experience and knowledge to bear.

Ensure the security, integrity, and compliance of data according to industry and company standards.

You might thrive in this role if you:

Have 3+ years of experience as a data engineer and 8+ years of any software engineering experience(including data engineering).

Proficiency in at least one programming language commonly used within Data Engineering, such as Python, Scala, or Java.

Experience with distributed processing technologies and frameworks, such as Hadoop, Flink and distributed storage systems (e.g., HDFS, S3).

Expertise with any of ETL schedulers such as Airflow, Dagster, Prefect or similar frameworks.

Solid understanding of Spark and ability to write, debug and optimize Spark code. 

This role is exclusively based in our San Francisco HQ. We offer relocation assistance to new employees.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$245K – $385K + Offers Equity



4. Android Engineer, ChatGPT Core Experiences
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

The ChatGPT Core Experiences team supports the OpenAI mission by innovating and evolving the Core UX design, technical architecture, and essential features of the Web, iOS, and Android ChatGPT client experiences. We focus on horizontal improvements that strategically empower vertical product development across our organization, enabling the launch of industry-leading feature capabilities.

About the Role
We are looking for a senior Android engineer to lead the development of new features and client foundational/architectural improvements across the ChatGPT Android client. In this role, you will:

Build and ship new features that push the boundaries of research and product innovation, bringing delightful and impactful AI experiences to Android users.

Plan and implement foundational client architecture improvements, focusing on optimizing performance, reliability, and scalability for the Android platform.

Drive client-side GraphQL migrations, collaborating with backend teams to adopt and integrate GraphQL, improving data fetching efficiency and developer productivity.

Optimize Android platform infrastructure to support development, testing, and deployment of these product and architectural improvements.

Work closely with research, product, design, and data science teams to ensure alignment and success in shipping innovative AI-driven features for Android.

How We Work
Our team prioritizes quality by focusing on latency, performance, reliability, and user delight. We take an impact-driven approach, focusing on the highest-ROI efforts that unlock velocity and leverage for vertical product teams. We emphasize developer enablement through improved tooling, infrastructure, and testing processes to ensure smooth and efficient product development.

We value a pragmatic approach, ensuring that we neither overbuild nor underbuild, always striking the right balance to deliver impactful solutions. We act as the glue that connects teams across the ChatGPT organization, ensuring cross-functional collaboration and cohesion for all client applications.

In this role, you will:

Build and ship new experiences that push the boundaries of research and product innovation to create a useful, delightful AI assistant in every user’s pocket

Plan and deploy mobile platform infrastructure necessary to build, test, and deploy these product experiences.

Execute on projects by working closely with research, product, design, data science and other members of product teams to land impact on product goals

Create a diverse and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group-think.

You might thrive in this role if you:

Have a strong track record of building impactful Android features and delivering high-quality mobile applications.

Have experience migrating to or using GraphQL for efficient data fetching, and collaborating with backend teams to drive this adoption.

Enjoy solving complex architectural challenges to optimize performance, scalability, and developer productivity on Android.

Value developer enablement, making it easier for other teams to deploy, test, and scale their work within the Android ecosystem.

Are comfortable navigating ambiguity and rapidly changing requirements, and enjoy working cross-functionally to ship meaningful AI-powered experiences.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$200K – $245K + Offers Equity



5. Android Engineer, ChatGPT Search
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

The ChatGPT Search team bridges research, engineering, product, and design to bring OpenAI's technology to the world.

We seek to learn from deployment and broadly distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. We aim to make our innovative tools globally accessible, transcending geographic, economic, or platform barriers. Our commitment is to facilitate the use of AI to enhance lives, fostered by rigorous insights into how people use our products.

About the Role

We seek an experienced Android engineer to craft intuitive, impactful experiences that solve meaningful user problems and bring the magic of our latest research to life. If you’re driven by user experience, love to ship, and sweat the details, this role is for you.

In this role, you will:

Build and ship new experiences that push the boundaries of research and product innovation to create a useful, delightful AI assistant in every user’s pocket

Plan and deploy mobile platform infrastructure necessary to build, test, and deploy these product experiences.

Execute on projects by working closely with research, product, design, data science and other members of product teams to land impact on product goals

Create a diverse and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group-think.

You might thrive in this role if you:

Have a proven track record of delivering impactful Android features.

Have a voracious and intrinsic desire to learn and fill in missing skills. An equally strong talent for sharing that information clearly and concisely with others

Are comfortable with ambiguity and rapidly changing conditions. You view changes as an opportunity to add structure and order when necessary

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$245K – $310K + Offers Equity



6. Bizops Lead
Business Operations - San Francisco

Apply now(opens in a new window)
About the Team
Business Operations drives some of OpenAI's most impactful initiatives and addresses mission-critical challenges that shape our research, product development, and go-to-market strategies, partnerships, and overall mission and company success. This small and high-performing team excels at bringing structure to ambiguity, crafting strategic direction, aligning stakeholders, and driving operational execution. Team members are highly analytical (able to break down complex business challenges using first-principles thinking), operational (able to work through obstacles and get things done), and collaborative (able to earn the trust of cross-functional stakeholders to make progress). They serve as trusted partners to leaders across the organization to ensure we achieve our most ambitious goals.

About the Role
We are hiring a Business Operations Lead to join our dynamic, high-impact team. In this role, you will provide strategic and operational capacity to leaders across the company to manage the direction and performance of the business, and also help launch and scale new initiatives. You will work on a project-by-project basis versus directly mapping to a business line.

You’ll develop a deep understanding of our technology and business at both macro and micro levels to shape strategic direction and drive tactical execution. This includes prioritizing key initiatives, identifying growth drivers, uncovering opportunities to accelerate success, and working with teammates to make them happen. Leveraging these insights, you’ll help ensure we are building the best models, products, and strategies, while proactively tackling challenges to achieve our goals.

Success in this role requires a combination of strategic vision, sharp analytical skills, executive-level communication, and hands-on problem-solving abilities. You'll need to foster collaboration across the organization, gain alignment from stakeholders, design comprehensive solutions, and drive results.

This role is based in our San Francisco HQ. We operate on a hybrid work model with three days in the office per week and offer relocation assistance. 

In this role, you will:
Collaborate closely with senior leaders to shape the strategic direction and performance of key business areas, ensuring alignment with OpenAI’s overarching objectives and long-term vision.

Identify growth opportunities in collaboration with product, go-to-market, and partnerships teams.

Partner with research, product, go-to-market, partnerships and other functions to launch new initiatives – helping think through strategic implications and executing on any operational components. 

Deep dive into the critical drivers of the business, enhancing operational understanding and identifying opportunities for optimization and innovation.

Develop and optimize monetization strategies, including pricing and packaging, to position our offerings competitively in the market and drive sustainable growth.

Support monthly business reviews by developing clear, data-driven narratives on performance, and presenting actionable insights and recommendations to senior leadership to inform decision-making and strategic planning.

You might thrive in this role if you:
Have 8+ years of experience in business operations, strategy, venture capital, private equity, or consulting, with at least 2 years operating within a company. We will also consider high-trajectory candidates with fewer years of experience but at top companies with a clear track record of excellence.

Have experience taking end-to-end ownership of large, ambiguous problems, and breaking them down into clear, actionable plans. 

Have direct experience engaging with executives and senior leaders to influence and drive strategic decisions.

Excel under pressure, bringing a high motor and exceptional adaptability and flexibility in a fast-paced, dynamic environment.

Are highly analytical – sophisticated in your understanding and approach to analyses; ability to ask and answer the most important questions, and present results clearly to leaders to influence decision making 

Are comfortable operating at all altitudes – discussing strategy and vision with executives, and troubleshooting operations with individual contributors.  

Have excellent communication and cross-functional collaboration skills. 

Are passionate about technology and artificial intelligence, and interested in its impact on business and society.

Nice to haves:
Technical background with a computer science degree or work in engineering/product 

Hands-on data experience with SQL and visualization tools (e.g., Tableau, Mode). 

Experience working in AI.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$210K – $265K + Offers Equity



7. Client Platform Engineer
IT - San Francisco

Apply now(opens in a new window)
About the Team

OpenAI’s IT organization supports the mission of deploying artificial general intelligence (AGI) for the benefit of all. Our team is committed to providing seamless technological support and solutions to ensure that all OpenAI employees are well-equipped and connected. This enables them to contribute effectively towards our AI research, corporate operations and product initiatives. 

About the Role

As a Client Platform Engineer at OpenAI, you will play a pivotal role in maintaining and shaping the overall experience of our employee endpoints, specifically focusing on our Mac laptop and corporate iPhone fleet. Your responsibilities will include ensuring that these endpoints are optimally set up for a variety of use cases, including advanced security configurations, seamless software deployments, and efficient troubleshooting processes. This role requires a proactive approach to monitor and address the needs of our diverse team, contributing to the development of scalable solutions that enhance the effectiveness of our endpoint program. By keeping our systems reliable and responsive, you will directly impact the agility and efficiency of our work at OpenAI. 

 This is a hybrid role and will require 3 days a week in our San Francisco office.

In this role, you will:

Manage our MDM and adjacent systems

Develop and implement robust patch policies and create custom application installers

Customize and streamline the deployment of endpoints tailored to diverse user stories

Collaborate closely with our enterprise security team to ensure all devices comply with the latest security standards and company policies

Lead initiatives to move towards a collaborative endpoint management program through the use of source control

You may be a fit for this role if you have:

Deep technical mastery of MacOS and iOS environments, with substantial experience managing these systems at scale within a hyper-growth company. You should be adept at handling rapid changes in infrastructure and user needs.

Advanced scripting skills in Python and Bash, with proven ability to automate processes, develop tools, and integrate systems that significantly improve operational efficiency and user experiences.

 Extensive experience with MDM solutions, particularly Jamf Pro, ensuring comprehensive management, security, and compliance of MacOS and iOS devices.

Expertise in deploying and managing large fleets of Macs and iOS devices, with a strong understanding of network configurations, security protocols, and troubleshooting practices in large-scale environments.

 Demonstrated capability in source control tools and practices, contributing to a collaborative endpoint management program that aligns with modern DevOps and agile methodologies.

 Experience in implementing zero-touch setup processes for endpoints, streamlining device deployment, and maintenance without compromising security or user productivity.

Proficiency in creating robust patch policies and custom application installers that meet the stringent requirements of a fast-paced, security-conscious organization.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$185K – $310K + Offers Equity



8. Compute & Infrastructure Accounting Manager
Finance - San Francisco

Apply now(opens in a new window)
About the Team

OpenAI Finance is responsible for ensuring the organization is set up for success in pursuit of its mission. The Compute & Infrastructure team shares financial insights and partners with internal and external business stakeholders to manage all aspects of cloud computing and platform infrastructure costs. This team ensures operational scalability, commits to financial accuracy, and empowers informed decision-making.

About the Role

We’re looking for an experienced accounting manager with a strong foundation in technical accounting to join our team. You will have deep subject matter expertise in technical accounting (ASC 842), strong analytical skills, and attention to detail. In this role, you will be a key player in driving the financial success of the organization by ensuring timely and accurate financial reporting for a critical part of OpenAI’s business. 

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Own end-to-end financial accounting and reporting for compute & infrastructure costs to support a timely month-end close.

Drive improvements in the quality of numbers by working cross-functionally with internal and external stakeholders to improve the reliability of data.

Maintain lease accounting schedules and record adjustments for lease modifications when appropriate.

Be the resident expert on ASC 842 and manage all hardware lease schedules and monthly accounting.

Build scalable processes and systems to support the scale-up of the organization.

Partner with other members of the accounting team to draft technical accounting memos related to platform infrastructure costs.

Be the primary liaison with external auditors for compute & platform infrastructure costs.

You might thrive in this role if you have: 

6+ years of progressive experience in accounting, audit or advisory services; operational experience in technology companies is strongly preferred. 

Mastery of technical accounting concepts related to leases (ASC 842). 

Best-in-class attention to detail and unwavering commitment to accuracy in an ever-changing business environment. 

Exemplary interpersonal skills as demonstrated by the ability to partner with internal and external stakeholders in various parts of the world on complex topics. 

Operational experience with monthly close and following a transaction start to finish.

Deep understanding of artificial intelligence development and platform infrastructure investments as key inputs to its success.

A passion for technology and artificial intelligence. 

CPA or CA strongly preferred.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$190K + Offers Equity




9. Compliance Program Manager
Security - San Francisco

Apply now(opens in a new window)
About the Team

Governance, Risk, and Compliance (GRC) is at the foundation of OpenAI’s mission to ensure that artificial general intelligence benefits all of humanity.  The GRC team provides security assurances and builds compliance for OpenAI’s technology, people, and products. We are technical in what we build but are operational in how we do our work, and are committed to supporting all products and research at OpenAI. Our team tenets include: prioritizing for impact; enabling sales, product, and research; preparing for future transformative technologies; and engaging a robust security and compliance culture.    

About the Role

As a Compliance Program Manager, you will be responsible for driving compliance operations optimizations forward and owning their outcomes. This will include building process implementations, creating documentation, and direct ownership of external audits for our organization. You will need to be an enthusiastic self-starter, diplomatic, reliable, optimization oriented, and capable of managing interpersonal dynamics well in high-pressure situations. You will be a part of a team of talented individuals who are just as passionate about supporting one another as they are about OpenAI’s mission. In this role you will do more than just manage audits end to end; you will help support and drive the business through building repeatable and scalable GRC processes across the organization, while consistently driving to reduce risks. 

We are looking for people who enjoy operating in a high accountability, high expectation environment where the goal is always to produce the best solution. Honesty, openness to new ideas, and willingness to accept and respond to feedback are critical. This position requires a combination of operations, project management, process optimization, and interpersonal skills with a focus on execution.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Drive audits and GRC initiatives across OpenAI. 

Enable OpenAI’s business by prioritizing where to mitigate risks and build processes that reduce friction and enable the teams and/or projects you support to use their resources most effectively.

Partner with internal teams to scope projects and initiatives that move our key objectives forward. 

Automate away administrative burdens so you and the team can focus on the next most pressing / challenging operational priorities.

Leverage the collective knowledge of the team: learn and develop expertise to cover gaps, bolster important efforts and projects, internalize feedback, and take charge of your personal growth.

Build and improve the operational workflows for Compliance & Security across OpenAI. 

You might thrive in this role if you have:

Experience and expertise in at least one area GRC, security, or security-adjacent fields.

A robust understanding of security and privacy compliance and regulatory standards.

Excellent program management skills, with a track record of having delivered on complex initiatives in a fast-moving environment.

Experience leading third-party compliance audits.

Strong written communication and customer service skills with an ability to engage across all levels of internal and external leadership.

Ability to empathize and collaborate with colleagues, independently manage and run projects, and prioritize efforts for risk reduction.

Ability to learn new skills and technologies to deliver the most effective solutions, and break down technical work into pieces that you both understand and can re-articulate to others.

Strong attention to detail, including maintaining accurate records and diligently following through on open requests.

Experience operationalizing workflows to increase responsiveness with an eye toward continuous compliance and continuous process improvement. 

Experience developing and navigating technical and compliance documentation and contract language.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$180K – $240K + Offers Equity



10. Cybersecurity Evaluations Engineer
Safety Systems - San Francisco

Apply now(opens in a new window)
About the Team

The Safety Systems team is responsible for various safety work to ensure our best models can be safely deployed to the real world to benefit the society and is at the forefront of OpenAI's mission to build and deploy safe AGI, driving our commitment to AI safety and fostering a culture of trust and transparency.

Frontier AI models have the potential to benefit all of humanity, but also pose increasingly severe risks. To ensure that AI promotes positive change, the Preparedness team helps us prepare for the development of increasingly capable frontier AI models. This team is tasked with identifying, tracking, and preparing for catastrophic risks related to frontier AI models.

Specifically, the mission of the Preparedness team is to:

Closely monitor and predict the evolving capabilities of frontier AI systems, with an eye towards misuse risks whose impact could be catastrophic (not necessarily existential) to our society; and

Ensure we have concrete procedures, infrastructure and partnerships to mitigate these risks and, more broadly, to safely handle the development of powerful AI systems.

Our team will tightly connect capability assessment, evaluations, and internal red teaming for frontier models, as well as overall coordination on AGI preparedness. The team’s core goal is to ensure that we have the infrastructure needed for the safety of highly-capable AI systems—from the models we develop in the near future to those with AGI-level capabilities. 

About the Role

As OpenAI continues to grow, we are looking for experienced, problem-solving engineers to ensure our systems scale. Our success depends on our ability to quickly iterate on products while also ensuring that they are performant and reliable. You will work in a deeply iterative, collaborative, fast-paced environment to bring our technology to millions of users around the world, and ensure it’s delivered with safety and reliability in mind. Successful candidates will play a crucial role in ensuring the reliability, scalability, and performance of our systems as we continue to expand. As a reliability expert, you will be at the forefront of maintaining and enhancing the stability, scalability, and performance of our rapidly evolving infrastructure. You will work closely with cross-functional teams, including software engineers, product managers, and data scientists, to build and maintain resilient systems that can handle our growing user base and workload.

In this role, you will:

Work on scaling our infrastructure to support a wide variety of evaluations, supporting systems and automation.

Collaborate with development teams to make our systems more reliable (owning Production Readiness Reviews)

Implement and manage monitoring systems to proactively identify issues and anomalies in our production environment.

Develop and maintain service level objectives (SLOs) and service level indicators (SLIs) to measure and ensure system reliability.

Implement fault-tolerant and resilient design patterns to minimize service disruptions.

Build and maintain automation tools to streamline repetitive tasks and improve system reliability.

Partner with engineers and researchers at OpenAI to help bring frontier research capabilities to the world.

Participate in an on-call rotation to respond to critical incidents and ensure 24/7 system availability.

You might thrive in this role if you:

Enjoy seeking out and addressing bottlenecks and areas for performance improvement in our systems.

Utilize Infrastructure as Code (IaC) principles to automate infrastructure provisioning and configuration management.

Are experienced in collaborating with cross-functional teams to ensure that reliability and scalability are considered in the design and development of new features and services.

Have a track record of accelerating engineering reliability by empowering your fellow engineers with excellent tooling and systems.

Help create a diverse, equitable, and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group think.

Have a humble attitude, an eagerness to help your colleagues, and a desire to do whatever it takes to make the team succeed.

Own problems end-to-end, and are willing to pick up whatever knowledge you're missing to get the job done.

Qualifications:

Bachelor's degree in Computer Science, Information Technology, or a related field (or equivalent work experience).

Have at least 7+ years of professional software engineering experience.

Proven experience as an reliability engineer or a similar role in a fast-paced, rapidly scaling company.

Strong proficiency in cloud infrastructure.

Proficiency in programming/scripting languages.

Experience with containerization technologies and container orchestration platforms like Kubernetes.

Knowledge of IaC tools such as Terraform or CloudFormation.

Excellent problem-solving and troubleshooting skills.

Strong communication and collaboration skills.

Experience with observability tools such as DataDog, Prometheus, Grafana, Splunk and ELK stack.

Experience with microservices architecture and service mesh technologies.

Knowledge of security best practices in cloud environments.

This role is exclusively based in our San Francisco HQ. We offer relocation assistance to new employees.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K + Offers Equity



11. Data Engineer, Safety Systems
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the team
The ChatGPT team works across research, engineering, product, and design to bring OpenAI’s technology to consumers and businesses.

We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

About the role:

We're looking for our first Data Engineer to help drive our product analytics and growth. If you love working with data, and creating solutions that drive critical business decisions and product development, you might be a great fit. ChatGPT is one of the fastest growing products in Silicon Valley history, and we hope to further accelerate our growth with data-derived insights.

In this role, you will:

Design, build and manage our data pipelines, ensuring all user event data is seamlessly integrated into our data warehouse.

Develop canonical datasets to track key product metrics including user growth, engagement, and revenue.

Work collaboratively with various teams, including, Infrastructure, Data Science, Product, Marketing, Finance, and Research to understand their data needs and provide solutions.

Implement robust and fault-tolerant systems for data ingestion and processing.

Participate in data architecture and engineering decisions, bringing your strong experience and knowledge to bear.

Ensure the security, integrity, and compliance of data according to industry and company standards.

You might thrive in this role if you:

Have 3+ years of experience as a data engineer and 8+ years of any software engineering experience(including data engineering).

Proficiency in at least one programming language commonly used within Data Engineering, such as Python, Scala, or Java.

Experience with distributed processing technologies and frameworks, such as Hadoop, Flink and distributed storage systems (e.g., HDFS, S3).

Expertise with any of ETL schedulers such as Airflow, Dagster, Prefect or similar frameworks.

Solid understanding of Spark and ability to write, debug and optimize Spark code. 

This role is exclusively based in our San Francisco HQ. We offer relocation assistance to new employees.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$245K – $310K + Offers Equity



12. Data Infrastructure Engineer
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

You’ll join the team that’s behind OpenAI’s data infrastructure that powers critical engineering, product, alignment teams that are core to the work we do at OpenAI. The systems we support include our data warehouse, batch compute infrastructure, streaming infrastructure, data orchestration system, data lake, vector databases, critical integrations, and more. 

About the Role

The Applied Data Platform team designs, builds, and operates the foundational data infrastructure that enables products and teams at OpenAI.

You are comfortable with work such as scaling Kubernetes services, OLAP systems, debugging Kafka consumer lag, diagnosing distributed kv store failures, designing a system to retrieve image vectors with low latency. 

You are well versed with infrastructure tooling such as Terraform, worked with Kubernetes, and have the SRE skill sets. 

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Design, build, and maintain data infrastructure systems such as distributed compute, data orchestration, distributed storage, streaming infrastructure while ensuring scalability, reliability, and security 

Ensure our data platform can scale reliably to the next several orders of magnitude

Accelerate company productivity by empowering your fellow engineers & teammates with excellent data tooling and systems, providing a best in case experience

Bring new features and capabilities to the world by partnering with product engineers, trust & safety and other teams to build the technical foundations

Like all other teams, we are responsible for the reliability of the systems we build. This includes an on-call rotation to respond to critical incidents as needed 

You might thrive in this role if you: 

Have 4+ years in data infrastructure engineering OR

Have 4+ years in infrastructure engineering with a strong interest in data

Take pride in building and operating scalable, reliable, secure systems

Are comfortable with ambiguity and rapid change

Have a voracious and intrinsic desire to learn and fill in missing skills—and an equally strong talent for sharing learnings clearly and concisely with others

Some of the technologies you’ll be working with include Apache Spark, Clickhouse, Python, Terraform, Kafka, Azure EventHub, Vector DBs.

 

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$200K – $385K + Offers Equity




13. Data Scientist, Business
Growth - San Francisco and New York City

Apply now(opens in a new window)
About the Role

As a member of our Business Data Scientist team, you will help build a data-driven culture around insight generation, decision making, and strategy at OpenAI. You should expect to work on a wide range of projects like defining north-star metrics, designing tests, estimating the incrementality of marketing and sales, and establishing source-of-truth dashboards that our business teams can use to answer their own questions. Most importantly, you should expect to be a core member of the Business teams, helping to bring our technology to a wide range of customers and supporting our self-serve and sales-led motions.

This role is based in San Francisco, CA or New York, NY. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Embed with the GTM, User Ops, Marketing, and Partnerships organization as a trusted partner, uncovering new ways to improve the business and drive growth

Manage cross-functional data science projects about revenue, marketing, pricing, usage, and other topics core to the business. 

Establish a data-driven culture by driving the definition, tracking, and operationalizing of metrics

Become an expert in OAI’s data and systems. Through partnership with Data Eng, Finance and other business teams, you should be able to self-serve all the underlying data for our business and derive insights from them.

Develop and socialize dashboards, reports, and other ways of enabling the team and company to answer product data questions in a self-serve way

Partner with other data scientists across the company to share knowledge and continually synthesizing learnings across the organization

 You might thrive in this role if you have:

At least 10+ years of experience in Data Science roles within dynamic, outcome-driven organizations.

Expertise in statistics and causal inference, applied in both experimentation and observational causal inference studies.

Proficiency in quantitative programming languages, such as Python and R.

Expertise in SQL, with extensive experience extracting large datasets and designing ETL workflows.

Experience using business intelligence tools, such as Mode, Tableau, and Looker.

Strategic and impact-driven mindset, capable of translating complex business problems into actionable frameworks.

Ability to build relationships with diverse stakeholders and cultivate strong partnerships.

Strong communication skills, including the ability to bridge technical and non-technical stakeholders and collaborate across various functions to ensure business impact.

Ability to craft clear data stories using decks, memos, and dashboards to drive decision-making at every level.

Best-in-class attention to detail and unwavering commitment to accuracy.

Proven track record in solving problems within Finance, Marketing, Partnerships, Sales, Support, or other GTM areas.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$245K – $385K + Offers Equity


14. Data Scientist, Monitoring Operations
Intelligence & Investigations - San Francisco and London, UK

Apply now(opens in a new window)
About the Team

OpenAI’s mission is to ensure that general-purpose artificial intelligence benefits all of humanity. We believe that achieving our goal requires real world deployment and iteratively updating based on what we learn. 

The Intelligence and Investigations team supports this by identifying and investigating misuses of our products – especially new types of abuse. This enables our partner teams to develop data-backed product policies and build scaled safety mitigations. Precisely understanding abuse allows us to safely enable users to build useful things with our products. 

About the Role

As a Data Scientist on the Monitoring Operations team, you will be responsible for building systems to proactively identify abuse on OpenAI’s products. This includes ensuring we have robust monitoring in place for new products, and can sustain monitoring for existing products.  You will also respond to critical escalations, especially those that are not caught by our existing safety systems. This will require expert understanding of our products and data, and involves working cross-functionally with product, policy, and engineering teams. 

This role can either be based in our San Francisco or London office and includes participation in an on-call rotation that will involve resolving urgent escalations outside of normal work hours. Some investigations may involve sensitive content, including sexual, violent, or otherwise-disturbing material. 

In this role, you will:

Scope and implement monitoring requirements for new product launches. This involves working with Product and Policy teams to understand key risks, and working with Engineering teams to ensure we have sufficient data and tooling. 

Improve processes to sustain monitoring operations for existing products. This includes developing approaches to automate monitoring subtasks.  

You might thrive in this role if you:

Have at least 4 years of experience doing technical analysis, especially in SQL and Python. 

Have experience in trust and safety and/or have worked closely with policy, enforcement, and engineering teams

Have experience with basic data engineering, such as building core tables or writing data pipelines (not expected to build infrastructure or write production code)

Have experience scaling and automating processes, especially with language models

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$220K – $320K + Offers Equity


15. Data Scientist, Product
Data Science - San Francisco

Apply now(opens in a new window)
About the Team

Our Applied team brings OpenAI technologies to consumers and businesses around the world. We collaborate across research, engineering, design and business functions to turn cutting-edge AI advancements into impactful real-world applications. Our team has been behind notable product launches (ChatGPT, API, Sora), creating tools that help developers write code, enable businesses to operate more efficiently, and empower individuals to learn and create. As AI capabilities rapidly evolve, we focus on ensuring that our products are safe, accessible, and beneficial to all. 

About the Role

As a Data Scientist on the Applied Product team, you will contribute to a data-driven product development culture for consumer and enterprise products at OpenAI. This is critical as our products reach millions of users and businesses worldwide. We are focused on aligning both research and product development to drive measurable impact for these individuals and organizations alike.

You should expect to define our north-star metrics, design A/B tests, and establish source-of-truth dashboards that the entire company can use to answer their own product questions. Most importantly, you should expect to be a core member of the product development team. 

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Embed with the product development team as a trusted partner, uncovering new ways to improve the product and drive growth

Define and interpret A/B tests that help answer critical questions about the impact of model and UX changes to our product 

Establish a data-driven product development culture by defining, tracking, and operationalizing feature-, product-, and company-level metrics

Develop and socialize dashboards, reports, and other ways of enabling the team and company to answer product data questions in a self-serve way

You might thrive in this role if you have:

5+ years experience in a quantitative role navigating highly ambiguous environments, ideally as an early data scientist or product analyst at a hyper-growth product company or research org

Proposed, designed, and run rigorous experiments with clear insights and product recommendations utilizing SQL and Python

Defined, implemented, and operationalized new feature and product-level metrics from scratch

Excellent communication skills with demonstrated ability to communicate with product managers, engineers, and executives alike

Strategic insights beyond the paradigm of statistical significance testing

You could be an especially great fit if you have:

Strong programming background, with ability to run simulations and prototype variants

Experience validating quantitative insights with qualitative methods (e.g. surveys, UXR)

Demonstrated prior experience in NLP, large language models, or generative AI

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$245K – $385K + Offers Equity



16. Developer Advocate, Developer Experience
Go To Market - London, UK

Apply now(opens in a new window)
About the Team

The Developer Experience team is a new group at OpenAI with a singular focus: making developers successful. Our mission is to empower every developer and startup on the planet to build on the OpenAI platform, providing them with the most delightful developer experience to seamlessly integrate AI into their apps and products. We are dedicated to ensuring that developers have the tools, resources, and support they need to unlock the full potential of AI in their projects.

The Developer Experience team partners very closely with the product and engineering teams building the OpenAI API, all GTM functions, as well as research and leadership. Across all product lines, we ensure that these powerful tools are used responsibly. This is a key part of OpenAI’s path towards safely deploying broadly beneficial Artificial General Intelligence (AGI). Safety is more important to us than unfettered growth. We are also committed to fostering an inclusive and diverse developer community, ensuring that our technologies are accessible and beneficial to all.

About the Role

We are looking for a highly skilled and passionate Developer Advocate to join our Developer Experience team. As a Developer Advocate, you will play a crucial role in engaging with our developer community and advocating for developers’ needs within OpenAI.

You will be using and advocating for new models and capabilities, such as GPT-4 Turbo, Vision, Whisper, TTS, and more, by building high-quality sample apps and demos, creating compelling technical content, shaping our documentation, as well as building developer tools for developers to build on top of the OpenAI API — everyone from hobbyist developers to Fortune 500 companies. You will also collaborate closely with the research and API teams as we bring the latest cutting-edge models to our platform.

This role is based in London, UK. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

As a Developer Advocate, you will:

Create and curate high-quality technical content, such as tutorials, blog posts, videos, and code samples, to educate and inspire developers.

Engage with the developer community, building strong relationships and fostering a vibrant ecosystem around OpenAI’s technologies.

Be a tireless champion for developers and their needs, gathering and organizing their feedback to inform our product roadmap.

Build relationships with key developers and help nurture a community of developers on our platform, representing OpenAI at developer events and online forums, serving as a knowledgeable and approachable ambassador for our platform.

Collaborate closely with product, engineering, and marketing teams to drive adoption and success of OpenAI’s APIs and developer tools.

Contribute to the development and enhancement of all OpenAI's developer surfaces to provide a seamless experience for developers.

We’re looking for a blend of:

Strong full-stack engineering background, with experience building with AI and LLMs.

Proven track record of engaging with developers to help them find success with API-based products, and building developer communities.

Deep user empathy and an understanding of what’s required for a product experience to be great and an appreciation that the details matter.

Creativity and passion for exploring new ways to connect with and empower developers.

Pride in crafting delightful developer tools and high-quality demos and sample projects.

A history of creating documentation, how-to content, and code that help developers find success with technical products.

An ability to write high-quality code, documentation, how-to content that help developers find success with technical products.

Ownership of problems end-to-end, and are willing to pick up whatever knowledge you’re missing to get the job done.

Team player with a collaborative mindset, able to work effectively across different teams and disciplines.

Ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines.

Experience with or a strong interest in AI ethics and safety, aligning with OpenAI's commitment to responsible AI development.

Compensation, Benefits and Perks

This is a position with OpenAI UK Ltd., which controls the hiring and management of this position. Total compensation includes competitive salary, generous equity and benefits.

Private medical insurance covering 100% of premiums for employees and their dependents

Pension plan with 4% employer contribution

52 weeks maternity leave and 20 weeks parental leave

Unlimited time off

Annual learning & development stipend ($1,500 USD equivalent per year)

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.




17. Distributed Training Engineer, Sora
Sora - San Francisco

Apply now(opens in a new window)
About the Team

The Sora team is working on making video a key capability of OpenAI’s foundation models. We are a hybrid research and product team that seeks to understand and expand the capabilities of our video models, while ensuring their reliability and safety. We accomplish this both through directly studying and experimenting with the models, as well as deploying them into the real-world to distribute their benefits widely.

 

About the Role

As a Distributed Systems/ML engineer, you will work on improving the training throughput for our internal training framework and enable researchers to experiment with new ideas. This requires good engineering (for example designing, implementing, and optimizing state-of-the-art AI models), writing bug-free machine learning code (surprisingly difficult!), and acquiring deep knowledge of the performance of supercomputers. We’re looking for people who love optimizing performance, understanding distributed systems, and who cannot stand having bugs in their code. 

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Collaborate with researchers to enable them to develop systems-efficient video models and architectures

Apply the latest techniques to our internal training framework to achieve impressive hardware efficiency for our training runs

Profile and optimize our training framework

You might thrive in this role if you:

Have experience working with multi-modal ML pipelines

Love diving deep into systems implementations and understanding their fundamentals in order to improve their performance and maintainability

Have strong software engineering skills and are proficient in Python.

Have experience understanding and optimizing training kernels

Are passionate about understanding stable training dynamics

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$295K – $440K + Offers Equity



18. Engineering Manager, Applied GPU Platform
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

Our team runs the GPU fleet that serves the models backing ChatGPT and the API. We build automation to provision and manage one of the largest cutting edge GPU inference fleets in the world, exposing it as a singular platform for other OpenAI teams to seamlessly run production applied AI workloads. 

We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

About the Role

We are looking for an experienced engineering manager to help lead our GPU platform team. You’ll help build and scale one of the largest inference fleets in the world. You will also collaborate closely with product and infrastructure teams to help ship reliable products quickly. 

In this role, you will:

Manage and build a diverse team of high performing infrastructure engineers

Guide the roadmap for automation for a fleet that can grow an order of magnitude in size or more

Build a world-class, secure compute fleet that serves users at scale

Set technical direction on evolving our compute and abstractions to support a growing business

Collaborate closely with a broad set of stakeholders, including product engineering, inference, security, research and finance

Work with external partners to unlock bleeding edge compute and making it available as a turnkey resource for scheduling workloads

Coach and nurture engineers to accelerate their growth and learning

You might thrive in this role if you:

Have 10+ years of experience in infrastructure software engineering, including 5+ years of experience in engineering management

Have prior experience building out high performance computing infrastructure teams at scale

Have worked with provisioning bare metal server data centers that interconnect across a WAN

Have experience building hybrid-cloud platforms

Care deeply about diversity, equity, and inclusion, and have a track record of building inclusive teams

Own problems end-to-end, and are willing to pick up whatever knowledge you're missing to get the job done. You will be expected to be able to be hands-on to help the team debug issues or manage systems from time to time as needed.

Have the ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$300K – $450K + Offers Equity




19. Engineering Manager, Automation
User Operations - San Francisco

Apply now(opens in a new window)
About the Team

The Support Automation team at OpenAI scales the organization by applying cutting-edge AI models to real-world challenges, automating and enhancing work across the organization. From customer operations to engineering, we develop an ecosystem of automation products that empower our colleagues and drive impact. We're passionate about crafting products that serve those around us, blending rapid prototyping with a focus on long-term quality and reliability. By creating reusable solutions, we create patterns that can be applied across diverse domains within OpenAI.

TLDR: this team leverages OpenAI technology to improve OpenAI, and you’ll have the opportunity to leverage the full extent of our tech (both public and pre-released) to accomplish this mission.

About the Role

We’re seeking our first Engineering Manager, Support Automation who’s excited about leading a team to create intuitive, impactful, and innovative user experiences. This role is ideal for someone who thrives in a hands-on, dynamic environment, driving both the team’s vision and technical execution. You will be the founding leader of this organization, and therefore will have the opportunity to shape the craft of this team in one of the most innovative companies in the world. You'll mentor a talented team of engineers, oversee project planning, and ensure delivery of high-quality interfaces that push the limits of what's possible with AI. If you’re passionate about blending leadership with deep technical expertise, this role could be a great fit.

In this role, you will:

Lead, mentor, and develop a team of engineers to build impactful products with a focus on performance, scalability, and delight.

Oversee the end-to-end product lifecycle from ideation and rapid prototyping through to production-ready deployment.

Collaborate closely with product, design, and cross-functional partners to align on vision, priorities, and execution.

Facilitate technical planning, code reviews, and ensure high-quality code and UI standards across projects.

Balance the needs of rapid iteration with the implementation of sustainable, maintainable solutions.

You might thrive in this role if you:

Have 7+ years of engineering experience, with at least 5 years in a people management role within a tech or product-focused organization.

Are highly proficient in modern front-end technologies like TypeScript, React, and related web standards, and are skilled in using design tools such as Figma.

Enjoy the challenge of transforming conceptual ideas into production-ready products, with a deep appreciation for design and user experience.

Bring a startup mindset, excelling in fast-paced environments where priorities and objectives can shift. You will be hands on AND leading - the details will matter

Are passionate about applying AI to solve real-world problems and creating interfaces that delight users.

Excel in fostering a culture of collaboration, ownership, and continuous improvement.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$385K + Offers Equity




20. Engineering Manager, Distributed Systems
Platform - San Francisco

Apply now(opens in a new window)
About the Team

The Platform Runtime team builds the low level framework components to power our ML training systems.  We work on building robust, scalable, high performance components to support our distributed training workloads.  Our priorities are to maximize the productivity of our researchers and our hardware, with the goal of accelerating progress towards AGI.  

About the Role

In this role, you will be directly managing our teams responsible for our distributed systems, specifically to deliver powerful APIs orchestrating thousands of computers moving/persisting vast amounts of data. This requires both providing easy to use, introspectible systems that can promote a fast debugging/development cycle, while also enabling that experience to scale to our newest supercomputers maintaining stability and performance throughout.

We’re looking for people who love optimizing an end to end system, understanding high performance I/O to maximize local performance and distributed across our compute resources. We want someone excited by the rapid pace of responding to the dynamic and evolving needs of our training systems architectures. Our team uses Python and Rust, and we are looking for someone who is excited to work in this stack and learn it if they're not familiar.

You will build teams in a deeply iterative, collaborative, fast-paced environment to bring our technology to millions of users around the world, and ensure it’s delivered with safety and reliability in mind.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

You might thrive in this role if you:

Have 5+ years of management experience, including previous experience managing managers

Have been responsible for building large scale systems to distribute workloads and industry-changing scale.

Are a seasoned technical leader, excited to do hand-on technical work but equally excited to lead technical teams to peak performance.

Help create a diverse, equitable, and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group think.

Have a humble attitude, an eagerness to help your colleagues, and a desire to do whatever it takes to make the team succeed.

Are experienced in collaborating with cross-functional teams to ensure that reliability and scalability are considered in the design and development of new features and services.

Own problems end-to-end, and are willing to pick up whatever knowledge you're missing to get the job done.

Have excellent communication skills. Expressing ideas clearly and listening carefully are among the most important requirements for success in this role.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$360K – $530K + Offers Equity



21. Engineering Manager, Financial Systems
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

The Applied team at OpenAI safely brings cutting-edge technology to the world. We have released groundbreaking products such as ChatGPT, Plugins, DALL·E, and APIs for GPT-4, GPT-3, embeddings, and fine-tuning. Our team also manages large-scale inference infrastructure. With much more on the horizon, our impact continues to grow.

Our customers create fast-growing businesses using our APIs, enabling product features previously unimaginable. ChatGPT exemplifies the current scope of possibilities. We prioritize the responsible use of our powerful tools, valuing safe deployment over unchecked expansion.

Within Applied Engineering, the Financial Engineering team ensures that our diverse products are monetized effectively to accommodate customers' varying needs and scales. Collaborating closely with the GTM and Finance teams, we strive to tailor our billing stack to our evolving internal requirements. We seek an experienced engineer to architect and refine our billing systems, enhancing their functionality to meet the demands of our increasingly complex and expansive product offerings.

In This Role, You Will:

Lead and Mentor: Oversee and grow a team of financial engineers, fostering a collaborative and innovative team culture.

Integrate Cross-Functionally: Collaborate closely with Product, Data, Finance, GTM, and other engineering teams, integrating billing tools into product and infrastructure workflows.

Strategic Direction: Set strategic priorities, staying updated with the latest trends and best practices.

Drive Operational Excellence: Scale infrastructure and processes to meet the demands of fast-growing products, balancing operational costs with performance.

You Might Thrive in This Role If You:

Care deeply about diversity, equity, and inclusion, and have a track record of building inclusive teams

Have a strong track record of coaching engineers to achieve their peak potential

Have Extensive Engineering Experience in software engineering, ideally with a background in payments, billing, or financial systems.

Enjoy Cross-Functional Collaboration: Are skilled at engaging with partners outside engineering, including finance, product, and operations teams.

Are a Strategic Thinker and Problem-Solver: Have a proven ability to set and execute a strategic vision, especially in dynamic environments with competing priorities.

Are Customer-Centric: Take pride in crafting scalable solutions that meet customer needs, with a focus on delivering an exceptional user experience.

Embrace Continuous Learning: Stay curious and proactive in acquiring new skills and sharing knowledge across the team.

Have a variety of experiences with highly available, distributed, online systems and have experience-driven insights into their pitfalls and tradeoffs

Join us to shape the next generation of financial systems, enabling OpenAI’s products to scale responsibly and securely.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees. 

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$300K – $450K + Offers Equity



22. Engineering Manager, Human Data
Human Data - San Francisco

Apply now(opens in a new window)
About the Team

OpenAI's Human Data Team creates custom data solutions driving groundbreaking research. Our work enhances and evaluates our flagship models and product like ChatGPT, GPT-4o, and Sora and contributes to safety initiatives through collaboration with our Preparedness and Safety Systems teams.

We work with AI trainers to gather specialized data for training and evaluating our models across modalities such as video, audio, text, and tool actions. Our goal is to develop scalable methods and tools and platforms to generate and evaluate high quality data from both synthetic sources and human experts in various fields, including mathematics, sciences, creative writing, programming, art, and safety. We leverage OpenAI models to improve and streamline our data collection and quality processes.

We're looking for a tech lead manager to build teams in a deeply iterative, collaborative, fast-paced environment to bring our technology to millions of users around the world, and ensure it’s delivered with safety and reliability in mind.

About the Role

In this role you might:

Directly manage ICs / TLs on Human Data, a core part of the Research organization. You will collaborate with product managers, researchers, and the rest of our engineering team to create new data and tooling around emerging research capabilities and unsolved customer needs.

Build and grow high performing teams in a deeply iterative, collaborative, fast-paced environment to bring our technology to millions of users around the world, and ensure it’s delivered with safety and reliability in mind.

Be responsible for the team that will architect, build, and design our tooling, infra, products, and evals that power our data collection and management platform, including collecting important training signals from products like ChatGPT, Dall-E, Sora, along with the key interfaces used by our AI human labelers.

Iterate rapidly to improve user and developer experience both for our internal team as well as partner research teams while advancing scalability, performance, observability, and security.

Understand training and eval data needs from across all of OpenAI and research opportunities to improve our platform, and help develop our technical roadmap and prioritization.

Help drive the high leverage projects for our team and ensure our team engagement is high and team, technical, and organizational blockers are resolved and milestones are delivered.

Ensure that our overall data collection platform is secure, scalable, highly available, and maximally useful.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

 

You might thrive in this role if you:

Hold a Ph.D., M.S., or B.S. or other degree in computer science, AI, machine learning, or a related field.

Have experience being a hands-on individual contributor, while simultaneously managing a high performing team.

Are comfortable rolling up your sleeves to write code and be a major contributor to a project.

Have experience hiring, coaching, and inspiring senior engineers or other TLs.

Are willing to both own important problems end-to-end, but also have good delegation skills and are willing to pick up whatever knowledge you're missing to get the job done.

Are strongly motivated by OpenAI’s mission of building safe, universally beneficial AGI and are aligned with OpenAI’s charter

Stay goal-oriented instead of method-oriented, and are not afraid of tedious but high-value work when needed.

Are a team player who enjoys collaborative work environments.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K – $465K + Offers Equity



23. Engineering Manager, Observability
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Role
As the Engineering Manager for Observability, you will build and lead a team responsible for the full observability stack, ensuring visibility, monitoring, logging, and alerting are all operating seamlessly at scale. Your team will help product teams observe, monitor, and troubleshoot their services, ensuring that our technology scales to meet the needs of our users without sacrificing performance or increasing operational costs.

You’ll work closely with product teams to ensure that observability practices are deeply integrated into development workflows. Additionally, you'll evaluate our existing observability stack, propose improvements, and lead the implementation of cost-effective and scalable solutions. Your technical depth, strong cross-functional collaboration skills, and leadership experience will guide us as we scale our infrastructure in the cloud.

In this role, you will:
Lead and grow a team of observability engineers, fostering a culture of collaboration and innovation.

Lead a team in building the observability stack, including monitoring, logging, and tracing, ensuring scalability and cost-efficiency.

Work closely with product and infrastructure teams to integrate observability tools into their development workflows.

Scale the observability infrastructure to meet the demands of fast-growing products while managing operational costs.

Ensure system reliability by identifying and addressing performance bottlenecks.

Set the strategic direction for observability tools, processes, and infrastructure, with a focus on scalability and delightful UX.

Stay updated with the latest trends in observability and cloud-native technologies, continuously seeking out improvements.

Build and maintain strong cross-functional relationships, ensuring that all product teams have visibility into their systems and services.

You might thrive in this role if you:
Have experience building and operating an observability stack from scratch, ideally in a cloud-based environment.

Are comfortable working in a fast-moving startup environment and can adapt to the pace of rapid growth.

Have technical expertise in observability tools and technologies (e.g., DataDog, Prometheus, Grafana, ELK stack).

Have a deep understanding of cloud platforms (e.g., AWS, GCP, Azure) and their role in observability.

Understand the challenges of building scalable observability backends and appreciate the importance of creating a user-friendly interface.

Have a strong track record of building and maintaining scalable systems in a cloud-based environment.

Are skilled in collaborating with cross-functional teams and have experience working with various product teams as customers.

Have a humble, coachable attitude and are eager to learn and grow as a leader.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$300K – $400K + Offers Equity



24. Enterprise Security Engineer
IT - San Francisco

Apply now(opens in a new window)
About the Team

Within the OpenAI Security organization, our IT team works to ensure our diverse team of researchers, engineers, and staff have the tools they need to work comfortably, securely, and with minimal interruptions. As an Enterprise Security Engineer, you will work in a highly technical and employee-focused environment.

Our IT team is a small and nimble team, where you’ll have the opportunity to dive into a wide breadth of areas and build from the ground up. We’re well supported and well resourced, and have a mandate to deliver a world-class enterprise security program to our teams.

About the Role

As an Enterprise Security Engineer, you will be responsible for implementing and managing the security of OpenAI's internal information systems’ infrastructure and processes. You will work closely with our IT and Security teams to develop security capabilities, enforce security policies, and monitor internal systems for security threats.

In this role, you will:

Develop and implement security measures to protect our company's information assets against unauthorized access, disclosure, or misuse.

Monitor internal and external systems for security threats and respond to alerts.

Contribute to and enforce our company's IT and Security policies and procedures.

Work closely with our IT department to harden our infrastructure using best practices in AzureAD, GSuite, Github, and other SaaS tooling.

Advise our employees on best practices for maintaining the security of their endpoints, and office AV and network infrastructure.

Devise novel sharing controls and associated monitoring to protect company data, including  intelligent groups management, Data Loss Prevention (DLP) and other security controls as appropriate.

Employ forward-thinking models like “secure by default” and “zero trust” to create sustainably secure environments for knowledge workers and developers.

Identify and remediate vulnerabilities in our internal systems, adhering to best practices for data security.

Use our own AI-driven models to develop systems for improved security detection and response, data classification, and other security-related tasks.

Educate employees on the importance of data security, and advise them on best practices for maintaining a secure environment.

Contribute to OpenAI's endpoint and cloud security roadmaps by staying up to date with the latest security threats, and making recommendations for improving our security posture.

You might thrive in this role if you have: 

Experience in protecting and managing macOS fleets.

Experience deploying and managing endpoint security solutions (e.g. management frameworks, EDR tools).

Experience with public cloud service providers (e.g. Amazon AWS, Microsoft Azure).

Experience with identity and access management frameworks and protocols, including SAML, OAUTH, and SCIM.

Experience with e-mail security protocols (e.g. SPF, DKIM, DMARC) and controls.

Intermediate or advanced proficiency with a scripting language (e.g. Python, Bash, or similar).

Knowledge of modern adversary tactics, techniques, and procedures.

Ability to empathize and collaborate with colleagues, independently manage and run projects, and prioritize efforts for risk reduction.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K + Offers Equity



25. Enterprise Site Reliability Engineer
IT - San Francisco

Apply now(opens in a new window)
About the Team

OpenAI’s IT organization supports the mission of deploying artificial general intelligence (AGI) for the benefit of all. Our team is committed to providing seamless technological support and solutions to ensure that all OpenAI employees are well-equipped and connected. This enables them to contribute effectively towards our AI research, corporate operations and product initiatives. 

About the Role

As an Enterprise Site Reliability Engineer, you are tasked with enhancing our Enterprise IT services through the use of OpenAI's models, automation, and development of internal tools. This includes automating internal identity and access management systems, designing applications and dashboards for internal users, and optimizing workflows. In addition, the role involves creating and managing intelligent Slack bots and integrations.

In this role, you will:

Architect scalable systems and deliver full lifecycle application development, including requirement gathering, planning, building, deploying, and maintaining software solutions.

Manage AzureAD IAM, SAML, OAUTH, and SCIM systems.

Handle identity and permissions on major cloud providers (Azure, AWS, GCP).

Design and implement role-based access control (RBAC) systems.

Mitigate common security vulnerabilities in Identity and Access Management.

Use Python for scripting and infrastructure automation tools such as Ansible, Chef, Puppet, and Terraform.

Utilize OpenAI's LLMs for internal application development and workflow optimization.

Create and manage Slack bots and integrations.

Manage multiple projects simultaneously, ensuring attention to detail and effective task prioritization.

You may thrive in this role if you have:

Proven application development skills with experience in reliable system

Experience with building Web APIs and services using Python (including async), Flask or FastAPI.

In-depth knowledge of AzureAD IAM, SAML, OAUTH, and SCIM.

Advanced scripting skills in Python and familiarity with infrastructure automation tools.

Understanding of identity and permissions on major cloud providers (Azure, AWS, GCP).

Experience with role-based access control (RBAC) systems design and implementation.

Understanding of common security vulnerabilities in Identity and Access Management and strategies to mitigate them.

Proven ability to manage projects effectively, pay close attention to detail, and prioritize tasks.

Excellent communication skills and ability to engage effectively with both technical and non-technical stakeholders.

Experience with developing and managing Slack bots and integrations.

 This is a hybrid role and will require 3 days a week in our San Francisco office.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$245K – $310K + Offers Equity



26. Financial Systems Senior Manager
Finance - San Francisco

Apply now(opens in a new window)
About the Team

The Finance Business Systems team’s mission is to design, implement, and maintain robust, future-proof systems that empower the business to grow seamlessly. We focus on driving process efficiencies through strategic system integrations, building automated workflows, and continuously expanding scalable automation initiatives. By enabling seamless data flow, reliable reporting, and strong compliance, we ensure our systems evolve alongside OpenAI’s growth, supporting smarter decisions and sustainable operations at scale.

About the Role

As a Financial Systems Senior Manager, you will play a vital role in managing and optimizing the financial systems that support our rapidly expanding finance organization. Reporting to the Head of Finance Business Systems, you will be responsible for overseeing the day-to-day operations of financial platforms, driving system enhancements, and ensuring the successful execution of finance-related projects and programs.

We’re looking for people who possess a strong mix of technical expertise, project management skills, and a deep understanding of finance processes. 

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Manage financial systems (Netsuite, ZIP, Metronome, Stripe) to ensure high availability, functionality, and performance.

Identify enhancement opportunities and drive the integration of financial systems to streamline workflows, improve data flow and accuracies, and enhance overall operational efficiency. 

Plan, manage, and execute finance-related projects and programs, ensuring timely delivery and alignment with business objectives.

Partner closely with the Strategic Finance team to implement a financial planning system that supports the corporate planning process

Partner with the Head of Finance Business Systems to design and deploy agentic workflows and bots leveraging OpenAI’s technologies to improve productivity and decision-making within the finance organization.

Ensure adherence to technology management best practices and strengthen internal controls by identifying and mitigating risks associated with systems.

Provide expert guidance and support for systems-related inquiries to internal stakeholders across Controllership, Procure-to-Pay, Revenue and Billing Operations, and other finance teams.

Create and maintain system documentation, in addition to developing reporting dashboards to provide actionable insights into system performance and project progress.

Manage offshore teams, ensuring alignment with organizational goals and high performance.

Mentor and coach team members to foster their professional growth, and contribute to a positive team culture.

 You might thrive in this role if you have: 

8+ years of progressive experience managing financial systems and projects, ideally in hypergrowth environments.

Strong technical expertise in financial platforms (e.g., Netsuite, ZIP, Metronome, Stripe) and iPaaS solutions.

Strong implementation experience in financial planning systems like Hyperion, Adaptive, or Anaplan (required).

Exceptional project management skills, with a track record of delivering complex projects on time and within scope.

Deep experience with system integrations, automations, and workflow optimizations.

Familiarity with compliance standards and best practices in technology management.

Excellent communication and collaboration skills, with the ability to effectively influence cross-functional partners.

Knowledge of AI technologies and their application in workflow automation.

Bachelor’s degree in a related field; advanced degree or relevant certifications (e.g., PMP, CPA, or similar) preferred.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$240K + Offers Equity




27. Full-Stack Engineer
Applied AI - San Francisco and Remote - Washington, DC

Apply now(opens in a new window)
About the Team

Join the engineering teams that bring OpenAI’s ideas safely to the world!!

The Applied Engineering team works across research, engineering, product, and design to bring OpenAI’s technology to consumers and businesses. We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

About the Role

We’re seeking a Full-Stack Engineer who can work across the entire software stack. You’ll join a nimble team where you’ll help drive deployment of OpenAI’s technology into new environments and infrastructure to enable the critical missions in the public sector. This role engages cross-functionally with internal product, security, and compliance teams to build required functionality and ensure we’re delivering a scalable, reliable platform. You’ll interface directly with customers to build the features they need most. 

This role is based in Washington D.C. and San Francisco, CA. Occasional travel to customer sites is required for this role.

In this role, you will:

Own the development of new customer-facing ChatGPT and OpenAI API features end-to-end, both on-premises and in the cloud, for our public sector customers.

Partner and directly embed with teams across the business, including engineering, security, and compliance, to enable our products to work within the unique constraints of new environments.

Talk to users to understand their problems and design solutions to address them

Work with the research team to get relevant feedback and iterate on their latest models

Collaborate with a cross-functional team of engineers, researchers, product managers, designers, and operations folks to create cutting-edge products

Optimize applications for speed and scale

You might thrive in this role if you:

Hold an active US security clearance

5+ years of relevant engineering experience at tech and product-driven companies

Proficiency with JavaScript, React, and other web technologies

Proficiency with some backend language (we use Python)

Some experience with underlying infrastructure primitives like Kubernetes and Terraform

Interest in AI/ML (direct experience not required)

Ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines

An interest in enabling public sector use cases with unique requirements

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$225K – $385K + Offers Equity



28. Full-Stack Software Engineer, Intelligent Support Engineering
User Operations - San Francisco

Apply now(opens in a new window)
About the Team
The Intelligent Support Engineering team is scaling OpenAI with OpenAI. We apply our latest models, technologies, and products (some external, some still in the lab) to real-world problems in order to assist with or automate work across the User Operations organization. We share what we learn back to the broader product and research teams, and we look to scale our solutions to new problem spaces within OpenAI. We love building products for folks sitting right next to us, and we take the time to add the touches that delight. Our goal is to prototype fast, then build for reliable long-term impact. We're constantly looking for the similarities and patterns in different types of work, and focus on building simple, generic patterns that we can apply across many domains.

The work of this team is intended to be the best example of leveraging OpenAI technologies. Our intent is to build systems to the point where the world can see the leverage that is possible with well designed AI-based implementations. We do this by working through internal use cases focused on Customers (specifically knowledge systems, automation systems, and automated agent systems) to prove impact, then we scale.

About the Role

We’re looking for a Full Stack Engineer who’s passionate about blending production-ready platform architecture with new tech and new paradigms. You’ll push the boundaries of OpenAI’s newest technologies to enable interactions and automations that are not only functional, but delightful. We value proactive, customer-centric engineers who can get the foundational details right (data models, architecture, security) in service of enabling great products.
In this role, you will:

Own the end-to-end development lifecycle for new platform capabilities and integrations with other systems

Collaborate closely with engineers, data scientists, information systems architects, and internal customers to understand their problems and implement effective solutions

Work with product and research team to share relevant feedback and iterate on applying their latest models

Your background might look something like:

4+ years of professional engineering experience (excluding internships) in relevant roles at tech and product-driven companies

Former founder, or early engineer at a startup who has built a product from scratch is a plus

Proficiency with JavaScript, React, and other web technologies

Proficiency with a backend language (we use Python)

Some experience with relational databases like Postgres/MySQL

Interest in AI/ML (direct experience not required)

Proven ability to thrive in fast-growing, product-driven companies by effectively navigating loosely defined tasks and managing competing priorities or deadlines.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K – $385K + Offers Equity


29. Full Stack Software Engineer, Leverage Engineering
Leverage Engineering - San Francisco and New York City

Apply now(opens in a new window)
About the Team

The Leverage team is scaling OpenAI with OpenAI. We apply our latest models to real-world problems in order to assist with or automate work across the company—then share what we learn back to the broader product and research teams. We’ve built an ecosystem of automation products that’s applied everywhere from customer operations to workplace to engineering.

We love building products for folks sitting right next to us, and we take the time to add the little big touches that delight. Our goal is to prototype fast, then build for reliable long-term impact. We're constantly looking for the similarities and patterns in different types of work, and focus on building simple, generic patterns that we can apply across many domains.


About the Role

We’re looking for an engineer who’s passionate about blending production-ready platform architecture with new tech and new paradigms. You’ll push the boundaries of OpenAI’s newest technologies to enable interactions and automations that are not only functional, but delightful. We value proactive, product-minded engineers who can see the big picture while staying on top of the little details that define great products.


 In this role, you will:

Own the full product development lifecycle for new platform capabilities and product experiences end-to-end

Collaborate closely with internal customers to understand their problems and implement effective solutions

Work with the research team to share relevant feedback and iterate on applying their latest models


You might thrive in this role if you:

4+ years of professional engineering experience (excluding internships) in relevant roles at tech and product-driven companies

Former founder, or early engineer at a startup who has built a product from scratch is a plus

Proficiency with JavaScript, React, and other web technologies

Proficiency with a backend language (we use Python)

Some experience with relational databases like Postgres/MySQL

Interest in AI/ML (direct experience not required)

Proven ability to thrive in fast-growing, product-driven companies by effectively navigating loosely defined tasks and managing competing priorities or deadlines.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K – $385K + Offers Equity




30. Head of Data Science, Strategic Finance
Strategic Finance - San Francisco

Apply now(opens in a new window)
About the Team

The Strategic Finance team is responsible for shaping the company’s financial strategy and plays a critical role in capital allocation decisions to align financial goals with broader business and mission objectives.

The Strategic Finance Data Science function has four core priorities: (1) accurately and credibly forecast our key business and financial metrics; (2) ensure attainment of key targets; (3) support complex modeling and analyses for business decision-making; and (4) scale recurring work and analysis through automation and dashboarding.

About the Role

The Head of Data Science, Strategic Finance will partner closely with the rest of the Strategic Finance team as well as the Product and GTM Data Science organizations to execute on core business priorities. You will report to the VP of Strategic Finance and work closely with finance leadership to drive data driven decision-making, improve data fluency of those around you, and move the needle on financial outcomes. This is a managerial role. 

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Develop accurate forecasts for product usage and revenue, compute consumption and their underlying drivers, allowing for real-time tracking of key metrics performance and trajectory.

Become an expert in OAI’s data and systems, through partnership with Data Engineering, Finance, and other Data Science teams.

Design and deliver dashboards for key metrics that impact financial performance.

Lead metrics reviews with Strategic Finance and finance leadership to interpret trends from aforementioned dashboards and surface actionable insights.

Drive automation of standardized reporting, analysis, and processes across our various revenue segments and compute spend.

Build and mentor a high-performing team.

Support critical business decisions with ad hoc analysis as needed.

You might thrive in this role if you have:

A MS/PhD in a quantitative discipline (Math, Statistics, Operations Research, Economics, Engineering, or CS).

12+ years of experience in a Data Science role at a dynamic and outcome-driven organization.

Proficiency in critical analytical tools including SQL.

Extensive experience building production-ready models for time series applications.

Built adjustable and explainable forecast models for multiple planning cycles.

Experience conducting open-ended research projects on new forecasting methodologies.

Exemplary ability to distill complex financial information into actionable insights for leadership.

Excellent communication skills and “storytelling” ability when presenting data insights.

The ability to thrive in a dynamic environment. That means being flexible and willing to jump in and do whatever it takes to be successful.

Knowledge of Python.

Prior management experience.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$385K – $465K + Offers Equity



31. Head of Global Mobility
People - San Francisco and Remote - US

Apply now(opens in a new window)
About the Team

OpenAI’s People team aims to hire, engage, and retain world-class talent who will safely build and deploy universally beneficial Artificial General Intelligence (AGI). The HR team is an important subset of the People team and supports a complex, growing employee group of scientists, engineers, and business professionals. The team contains expertise across compliance, employee relations, immigration, compensation and benefits, learning and development, People programs, employee communications, and more.

About the Role

We are expanding our People Compliance team, nested within our People Operations group, and seeking a strategic and experienced leader for our global mobility and immigration programs. This role will oversee global immigration, relocation, and tax compliance initiatives, and will support our recruiting, retention, and growth strategies by developing efficient, compliant, cost-effective, and scalable policies aligned with company objectives.

Your Key Responsibilities include:

Lead the design and strategic implementation of comprehensive global mobility programs and policies, including complex relocations, international transfers, and assignments, to help drive business growth and enhance the overall employee experience.

Serve as a trusted advisor to recruiters, managers, and employees, providing expert guidance on mobility policies, relocation packages, and comprehensive transition support.    

Collaborate closely with senior leadership in finance, legal, and tax teams to ensure seamless payroll and tax compliance.

Develop and maintain robust vendor management practices to optimize global mobility processes and ensure effective partnerships with external vendors.

Spearhead the evolution of the company's global immigration strategy, collaborating with the team to execute initiatives that ensure robust compliance with all applicable regulations and laws and alignment with broader business objectives.  

Proactively monitor and anticipate changes in global immigration policies, implementing strategic updates to company practices to mitigate risks and maintain compliance.

We’re looking for someone with:

10+ years of experience in global mobility, immigration, and tax compliance, with at least 3 years in a managerial or leadership role.

Proven experience managing mobility, immigration programs, with a strong focus on effectively overseeing vendor relationships to ensure service quality, compliance, and excellent employee experience.

In-depth knowledge of global immigration laws, relocation processes, and international tax compliance.

Strong project management and organizational skills.

Excellent communication, consultation, and stakeholder management abilities.

Ability to work in a fast-paced, dynamic environment and manage multiple priorities.

High attention to detail and commitment to compliance.

Location and Workplace

This role is based either in our Mission Bay, San Francisco, CA office or remotely in the US if outside of an office location.

Our offices use a hybrid work model: three days in the office per week with optional work from home on Thursdays and Fridays. We offer relocation assistance to new employees.

Our open-plan offices have height-adjustable desks, conference rooms, phone booths, well-stocked kitchens full of snacks and drinks, three in-house prepared meals daily, a private outdoor space for working in the sun or socializing, nap rooms, private bike storage, and more.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$236K – $295K + Offers Equity • Multiple Ranges

Apply now



33. Head of People Systems
People - San Francisco and Remote - US

Apply now(opens in a new window)
About the Team
OpenAI’s People team aims to hire, engage, and retain world-class talent who will ensure that artificial general intelligence benefits all of humanity. The People Ops team supports a complex, growing employee group of scientists, engineers, and business professionals.

About the Role

We’re looking for an experienced and technical leader for our People Systems team to ensure we have the right technology strategy in place to enable the initiatives and programs driven by the People Team and cross-functional partners. As part of the People Operations leadership team, you’ll work alongside the leaders of Recruiting Ops, Employee Support, and Compliance teams.

You’ll be responsible for important goals:

Conduct an Assessment: Evaluate our current People Systems and technology landscape to identify strengths, weaknesses, opportunities, and threats. This includes assessing system performance, user experience, compliance, audit readiness, and data privacy practices to inform your strategic decisions in support of the People Team's initiatives.

Create the Strategy: Develop a comprehensive technology strategy for People Systems that supports business requirements and aligns with our innovative culture. Your strategy should incorporate a deep understanding of our internal products and their potential to enhance People Team solutions, processes, and the overall employee experience, with a focus on compliance and data security. It will be critical to be able to lead within a matrix of owning the technology solutions, and partnering to ensure the overall technology ecosystem is sound, as well as setting the foundation for People analytics. 

Drive the Roadmap: Establish and communicate a clear roadmap for People Systems that outlines key initiatives, timelines, and milestones. You will ensure that this roadmap is aligned with the strategic priorities of the People Team and cross-functional partners such as IT, Finance, and Legal, especially around data integrity and consistent data governance. 

Lead the Team: Lead and mentor the People Systems team, fostering a culture of innovation and continuous improvement. You will be responsible for building a strong, high-performing team that can execute on the strategy and adapt to the evolving needs of the business and the People Team.

Champion our Mission: As a key promoter of OpenAI's mission to advance AI for the benefit of humanity, you will lead efforts to integrate this mission into our People Systems. Advocate for leveraging our own products within People Systems to test and refine solutions, aligning technology initiatives with strategic goals and ensuring robust data privacy practices.

We’re looking for a blend of this experience:

HR Systems Experience: 10-15+ years of experience in HR systems (experience, across multiple HR disciplines, including working within a shared services environment a strong plus) 

Extensive Experience with Workday and Technical Proficiency:

Deep understanding of Workday's configuration, business processes, reporting capabilities, and data management

Proven track record of implementing and managing Workday HCM modules.

Workday certification(s) in relevant modules or areas of expertise, including HCM, Security, Compensation, Benefits or Absence

Strong technical skills in system integrations and security best practices.

Leadership and Team Management:

5-10 years of demonstrated experience leading and mentoring a technical team in a People Systems or HR context.

Proven success in building and scaling People Systems in a high-growth, global organization

Ability to manage cross-functional teams and collaborate effectively with IT, Finance, and Legal.

Strategic Planning and Execution:

Experience in developing and executing technology strategies that align with organizational goals and HR initiatives.

Ability to create and communicate a technology roadmap for People Systems.

Experience managing vendors ensuring alignment with organizational goals and technology strategy, and partnering with Procurement to negotiate contracts, manage performance, and collaborate to optimize service delivery.

Communication, Problem Solving, and Stakeholder Management:

Excellent communication skills with the ability to translate technical concepts for non-technical stakeholders.

Focus on developing and implementing change management strategies to ensure adoption

Strong problem-solving abilities with a focus on continuous improvement and leveraging new technologies.

Ability to work closely with HR leadership and other senior stakeholders to understand and address their needs.

Location and Workplace

This role is based either in our Mission Bay, San Francisco, CA office or remotely in the US if outside of an office location.

Our offices use a hybrid work model: three days in the office per week with optional work from home on Thursdays and Fridays. We offer relocation assistance to new employees.

Our open-plan offices have height-adjustable desks, conference rooms, phone booths, well-stocked kitchens full of snacks and drinks, three in-house prepared meals daily, a private outdoor space for working in the sun or socializing, nap rooms, private bike storage, and more.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$236K – $380K + Offers Equity • Multiple Ranges



34. HW/SW Co-Design Engineer
Platform - San Francisco

Apply now(opens in a new window)
About the Team

Our mission at OpenAI is to discover and enact the path to safe, beneficial AGI. To do this, we believe that many technical breakthroughs are needed in generative modeling, reinforcement learning, large scale optimization, active learning, among other topics.

The Research Platform team builds robust and scalable software to support our research efforts. It also offers core development services for mission critical goals and applications. 

We’re forming a new team to work with our partners on hardware optimization and co-design, and are looking for founding engineers. This team will be responsible for working with partners to optimize their hardware for our workloads, identifying promising new deep learning accelerators, and bringing those hardware platforms to production.

About the Role

As an Engineer on our Hardware Team, you will co-design future hardware from different vendors for programmability and performance. You will work with our kernel, compiler and machine learning engineers to understand their needs related to ML techniques, algorithms, numerical approximations, programming expressivity, and compiler optimizations. You will evangelize these constraints with various vendors to develop future hardware architectures amenable for efficient training and inference. If you are excited about maximizing HBM bandwidth, optimizing for low arithmetic intensity, expressive SIMD ISA, low-precision formats, optimizing for memory hierarchies, simulating workloads at various resolutions of the hardware and evangelizing these ideas with hardware engineers, this is the perfect opportunity!

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Co-design future hardware for programmability and performance with our hardware vendors

Assist hardware vendors in developing optimal kernels and add support for it in our compiler

Develop performance estimates for critical kernels for different hardware configurations 

Work with machine learning engineers, kernel engineers and compiler developers to understand their vision and needs from high performance accelerators

Manage communication and coordination with internal and external partners

Influence the roadmap of hardware partners to optimize them for OpenAI’s workloads.

Evaluate potential partners’ accelerators and platforms.

Build simulations and performance models to progressively improve decision making fidelity.

As the scope of the role and team grows, understand and influence roadmaps for hardware partners for our datacenter networks, racks, and buildings.

You might thrive in this role if you:

4+ years of industry experience, including experience harnessing compute at scale or building semiconductors.

Strong experience in software/hardware co-design

Deep understanding of GPU and/or other AI accelerators

Experience with CUDA or a related accelerator programming language

Experience driving Machine Learning accuracy with low precision formats

Experience aligning future hardware with a well established HPC infrastructure

Are familiar with the fundamentals of deep learning computing and chip microarchitecture.

Able to actively collaborate with ML engineers, kernel writers and compiler developers

These attributes are nice to have:

PhD in Computer Science and Engineering with a specialization in Computer Architecture, Parallel Computing. Compilers or other Systems

Strong coding skills in C/C++ and Python

Strong understanding of LLMs and challenges related to their training and inference 

Benefits and Perks

Medical, dental, and vision insurance for you and your family

Mental health and wellness support

401(k) plan with 4% matching

Unlimited time off and 18+ company holidays per year

Paid parental leave (20 weeks) and family-planning support

Annual learning & development stipend ($1,500 per year)

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$360K – $530K



35. Infrastructure Engineer
Applied AI - Remote - Washington, DC and San Francisco

Apply now(opens in a new window)
About the Team

Join the engineering teams that bring OpenAI’s ideas safely to the world!!

The Applied Engineering team works across research, engineering, product, and design to bring OpenAI’s technology to consumers and businesses. We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

 

About the Role

We’re seeking an Infrastructure Engineer with experience in building and operating infrastructure at scale. You’ll join a nimble team where you’ll help drive deployment of OpenAI’s technology into new environments and infrastructure to enable the critical missions in the public sector. This role engages cross-functionally with internal product, security, and compliance teams to build required functionality and ensure we’re delivering a scalable, reliable platform that can run wherever our customers need our technology most.

This role is based in Washington D.C. and San Francisco, CA. Occasional travel to customer sites is required for this role. 

In this role, you will:

Design and build performant, reliable, and scalable infrastructure, both on-premises and in cloud, for our public sector customers.

Accelerate engineering productivity by empowering your fellow engineers with excellent tooling and systems

Bring new features and research capabilities to the world by partnering with product engineers to lay the necessary technical foundations

Guide and advise product engineering teams on best practices for ensuring observable, scalable systems

Work with our on-site teams and customers to ensure the reliability of the systems we build. This includes an on-call rotation to respond to critical incidents as needed.

Partner with teams across the business, including engineering, security, and compliance, to enable our infrastructure to operate within the unique constraints of new environments.

 

You might thrive in this role if you:

Hold an active US security clearance

Have 8+ years of experience in engineering, including 4+ years of experience in infrastructure

Built, operated, and maintained infrastructure in environments with unique and challenging constraints.

Take pride in building and operating scalable, reliable, secure systems

Debug issues across the stack, inclusive of networking and performance

Thrive in dynamic environments and can navigate ambiguity with ease.

Have a voracious and intrinsic desire to learn and fill in missing skills—and an equally strong talent for sharing learnings clearly and concisely with others

Some of the technologies you’ll be working with include Kubernetes, Python, FastAPI, Cosmos DB, Postgres, and Terraform.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$220.5K – $385K + Offers Equity




36. HW/SW Co-Design Engineer
Platform - San Francisco

Apply now(opens in a new window)
About the Team

Our mission at OpenAI is to discover and enact the path to safe, beneficial AGI. To do this, we believe that many technical breakthroughs are needed in generative modeling, reinforcement learning, large scale optimization, active learning, among other topics.

The Research Platform team builds robust and scalable software to support our research efforts. It also offers core development services for mission critical goals and applications. 

We’re forming a new team to work with our partners on hardware optimization and co-design, and are looking for founding engineers. This team will be responsible for working with partners to optimize their hardware for our workloads, identifying promising new deep learning accelerators, and bringing those hardware platforms to production.

About the Role

As an Engineer on our Hardware Team, you will co-design future hardware from different vendors for programmability and performance. You will work with our kernel, compiler and machine learning engineers to understand their needs related to ML techniques, algorithms, numerical approximations, programming expressivity, and compiler optimizations. You will evangelize these constraints with various vendors to develop future hardware architectures amenable for efficient training and inference. If you are excited about maximizing HBM bandwidth, optimizing for low arithmetic intensity, expressive SIMD ISA, low-precision formats, optimizing for memory hierarchies, simulating workloads at various resolutions of the hardware and evangelizing these ideas with hardware engineers, this is the perfect opportunity!

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Co-design future hardware for programmability and performance with our hardware vendors

Assist hardware vendors in developing optimal kernels and add support for it in our compiler

Develop performance estimates for critical kernels for different hardware configurations 

Work with machine learning engineers, kernel engineers and compiler developers to understand their vision and needs from high performance accelerators

Manage communication and coordination with internal and external partners

Influence the roadmap of hardware partners to optimize them for OpenAI’s workloads.

Evaluate potential partners’ accelerators and platforms.

Build simulations and performance models to progressively improve decision making fidelity.

As the scope of the role and team grows, understand and influence roadmaps for hardware partners for our datacenter networks, racks, and buildings.

You might thrive in this role if you:

4+ years of industry experience, including experience harnessing compute at scale or building semiconductors.

Strong experience in software/hardware co-design

Deep understanding of GPU and/or other AI accelerators

Experience with CUDA or a related accelerator programming language

Experience driving Machine Learning accuracy with low precision formats

Experience aligning future hardware with a well established HPC infrastructure

Are familiar with the fundamentals of deep learning computing and chip microarchitecture.

Able to actively collaborate with ML engineers, kernel writers and compiler developers

These attributes are nice to have:

PhD in Computer Science and Engineering with a specialization in Computer Architecture, Parallel Computing. Compilers or other Systems

Strong coding skills in C/C++ and Python

Strong understanding of LLMs and challenges related to their training and inference 

Benefits and Perks

Medical, dental, and vision insurance for you and your family

Mental health and wellness support

401(k) plan with 4% matching

Unlimited time off and 18+ company holidays per year

Paid parental leave (20 weeks) and family-planning support

Annual learning & development stipend ($1,500 per year)

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$360K – $530K




37. Lead Product Manager, Core Product
Product Management - San Francisco

Apply now(opens in a new window)
About the Team

We are the team behind ChatGPT, a rapidly evolving AI companion designed to answer any question and perform any task intuitively. With over 200 million weekly active users globally, ChatGPT plays a significant role in ensuring that AI benefits all of humanity. And we’re just getting started. We have ambitious plans to further enhance the product by combining research, engineering, and design, making ChatGPT even more intuitive and indispensable in users’ daily lives.

About the Role

We’re seeking a Lead Product Manager to spearhead the development and evolution of ChatGPT’s core experiences. In this role, you will drive the product’s growth across all platforms—web, mobile, desktop, and third-party surfaces—ensuring a seamless and engaging experience for our rapidly expanding user base.

You will be a key player in shaping the future of ChatGPT, owning how millions of people interact with AI daily. This role is perfect for someone who is deeply passionate about product design, has a strong user-centric approach, and possesses the technical expertise to collaborate closely with engineering and research teams.

This position is based in San Francisco, CA. We utilize a hybrid work model with 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

• Vision & Strategy: Spearhead the development and implementation of cutting-edge AI research by crafting the vision, strategy, roadmap, and execution plan.

• Product Development: Convert user feedback into detailed product requirements, narratives, and technical specifications.

• Data-Driven Insights: Utilize data to deeply understand user needs and guide future product development.

• Cross-Functional Collaboration: Work closely with research, product design, and engineering teams to bring new capabilities to life.

You might thrive in this role if you:

• Have 6+ years of product management or related industry experience.

• Have experience being a hands-on individual contributor while simultaneously managing a high-performing team.

• Obtained a bachelor’s degree in Computer Science, Engineering, Information Systems, Analytics, Mathematics, Physics, Applied Sciences, or a related field.

• Have proven experience working in a technical environment with cross-functional teams to drive product vision, define requirements, and guide the team through key milestones.

• Are passionate about design and figuring out best-in-class solutions to UX, UI, and interaction challenges.

• Showcase strong leadership, organizational, and execution skills, along with proven communication abilities

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$385K – $465K + Offers Equity



38. Machine Learning Engineer, Applied AI
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

OpenAI is at the forefront of artificial intelligence, driving innovation and shaping the future with cutting-edge research. Our mission is to ensure that AI's benefits reach everyone. We are looking for visionary Machine Learning Engineers to join our Applied Group, where you'll transform groundbreaking research into real-world applications that can change industries, enhance human creativity, and solve complex problems.

About the Role

As a Machine Learning Engineer in OpenAI's Applied Group, you will have the opportunity to work with some of the brightest minds in AI. You'll contribute to deploying state-of-the-art models in production environments, helping turn research breakthroughs into tangible solutions. If you're excited about making AI technology accessible and impactful, this role is your chance to make a significant mark.

In this role, you will:

Innovate and Deploy: Design and deploy advanced machine learning models that solve real-world problems. Bring OpenAI's research from concept to implementation, creating AI-driven applications with a direct impact.

Collaborate with the Best: Work closely with researchers, software engineers, and product managers to understand complex business challenges and deliver AI-powered solutions. Be part of a dynamic team where ideas flow freely and creativity thrives.

Optimize and Scale: Implement scalable data pipelines, optimize models for performance and accuracy, and ensure they are production-ready. Contribute to projects that require cutting-edge technology and innovative approaches.

Learn and Lead: Stay ahead of the curve by engaging with the latest developments in machine learning and AI. Take part in code reviews, share knowledge, and lead by example to maintain high-quality engineering practices.

Make a Difference: Monitor and maintain deployed models to ensure they continue delivering value. Your work will directly influence how AI benefits individuals, businesses, and society at large.

You might thrive in this role if you:

Master's/  PhD degree in Computer Science, Machine Learning, Data Science, or a related field. 

Demonstrated experience in deep learning and transformers models

Proficiency in frameworks like PyTorch or Tensorflow

Strong foundation in data structures, algorithms, and software engineering principles.

Experience with search relevance, ads ranking  or LLMs is a plus.

Are familiar with methods of training and fine-tuning large language models, such as distillation, supervised fine-tuning, and policy optimization

Excellent problem-solving and analytical skills, with a proactive approach to challenges.

Ability to work collaboratively with cross-functional teams.

Ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines

Enjoy owning the problems end-to-end, and are willing to pick up whatever knowledge you're missing to get the job done

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K – $550K




39. Machine Learning Engineer, Integrity
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

The Integrity team at OpenAI is dedicated to ensuring that our cutting-edge technology is not only revolutionary, but also secure from a myriad of adversarial threats. We strive to maintain the integrity of our platforms as they scale. 

The Integrity team is at the front lines of defending against financial abuse, scaled attacks, and other forms of misuse that could undermine the user experience or harm our operational stability.

About the Role

As a Machine Learning Engineer in OpenAI's Applied Group, you will have the opportunity to work with some of the brightest minds in AI. You'll contribute to deploying state-of-the-art models in production environments, helping turn research breakthroughs into tangible solutions that improve the trust and safety of our platform. If you're excited about fine tuning LLMs and building ML models this role is your chance to make a significant mark.

In this role, you will:

Innovate and Deploy: Design and deploy advanced machine learning models that solve real-world problems. Bring OpenAI's research from concept to implementation, creating AI-driven applications with a direct impact.

Collaborate with the Best: Work closely with researchers, software engineers, and product managers to understand complex business challenges and deliver AI-powered solutions. Be part of a dynamic team where ideas flow freely and creativity thrives.

Optimize and Scale: Implement scalable data pipelines, optimize models for performance and accuracy, and ensure they are production-ready. Contribute to projects that require cutting-edge technology and innovative approaches.

Learn and Lead: Stay ahead of the curve by engaging with the latest developments in machine learning and AI. Take part in code reviews, share knowledge, and lead by example to maintain high-quality engineering practices.

Make a Difference: Monitor and maintain deployed models to ensure they continue delivering value. Your work will directly influence how AI benefits individuals, businesses, and society at large.

You might thrive in this role if you:

Master's/  PhD degree in Computer Science, Machine Learning, Data Science, or a related field. 

Demonstrated experience in deep learning and transformers models

Proficiency in frameworks like PyTorch or Tensorflow

Strong foundation in data structures, algorithms, and software engineering principles.

Experience with search relevance, ads ranking  or LLMs is a plus.

Are familiar with methods of training and fine-tuning large language models, such as distillation, supervised fine-tuning, and policy optimization

Excellent problem-solving and analytical skills, with a proactive approach to challenges.

Ability to work collaboratively with cross-functional teams.

Ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines

Enjoy owning the problems end-to-end, and are willing to pick up whatever knowledge you're missing to get the job done

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K – $550K




40. Machine Learning Engineer, Retrieval & Search
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

We bring OpenAI's technology to the world through products like ChatGPT and the OpenAI API.

We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

About the Role

We are looking for an experienced machine learning engineer to work on retrieval & search problems across our API and ChatGPT. As the AI landscape has evolved over the last few years, retrieval & search have emerged as key use cases for our models, and we are investing in ensuring that we can offer these search-based product experiences for our users. You will be at the center of our retrieval & search efforts as a company, and the progress you drive here will reach millions of end users.

In this role, you will:

Work on retrieval & search algorithms and methodologies in close collaboration with our research team, including problems in such domains as document search, enterprise search, knowledge retrieval, and web-scale search.

Deploy these search methodologies into production in both the API and ChatGPT to be used by millions of end users.

Explore novel research topics in retrieval & search that may inform our product strategy in the medium and long term.

Partner with researchers, engineers, product managers, and designers to bring new features and research capabilities to the world

Help create a diverse, equitable, and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group think

You might thrive in this role if you:

Have extensive prior experience building and maintaining production machine learning systems.

Have prior experience working with vector databases, search indices, or other data stores for search and retrieval use cases

Have prior experience building and iterating on internet-scale search systems

Own problems end-to-end, and are willing to pick up whatever knowledge you're missing to get the job done

Have the ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$310K – $550K




41. Manager, Customer Success, Strategics
Customer Success - San Francisco

Apply now(opens in a new window)
About the team

The Strategics Customer Success (CS) team is responsible for driving the adoption and value realization of Generative AI applications for developers and enterprises. We act as a trusted advisor and thought partner for our customers, working to build an effective backlog of GenAI use cases for their industry and drive them to production through strong guidance. As the leader of Customer Success Managers (CSM) in the Strategics segment, you’ll help the largest companies transform their business through solutions such as customer service, automated content generation, and novel applications that make use of our newest, most exciting models.

About the role

We are seeking a Customer Success leader to ensure the technical success of our most strategic customers across the globe. In this role, you will oversee a team responsible for driving the adoption, engagement, and value realization of all OpenAI products throughout the customer lifecycle. Success will be measured by customer activation and adoption, live production deployments, demonstrable value realization, and customer satisfaction. You will partner with Sales, Solutions Engineering, Solutions Architecture, and Product teams. 

In this role, you will:

Own the strategy and operating model of the Strategics CSM team, ensuring alignment with company objectives and the evolving needs of our customers.

Lead, build, and mentor a team of high-performing Strategics CSM to deliver exceptional customer outcomes, as demonstrated by production customer deployments, increased adoption, retention, expansion, and customer satisfaction. 

Develop scalable customer success programs, including customer success plans, KPI frameworks, risk/churn mitigation, and use case enablement strategies.

Represent the voice of enterprise customers to internal teams, influencing product roadmaps and go-to-market strategies.

Act as an AI thought leader and industry expert, advising customers on best practices and transformative opportunities with ChatGPT Enterprise.

You’ll thrive in this role if you:

Have 7+ years of experience in a customer-facing success role, managing C-level technical and business relationships with complex global organizations.

Have 3+ years of experience leading post-sales teams with a demonstrated ability to hire, develop, and manage technical teams.

Have developed and executed scalable customer success programs for customers across industries and regions.

Are an effective presenter and communicator who can translate business and technical topics to all audiences, including senior leaders.

Own problems end-to-end and are willing to pick up whatever knowledge you're missing to get the job done.

Have a humble attitude, an eagerness to help your colleagues, and a desire to do whatever it takes to make the team succeed.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$240K – $300K + Offers Equity




42. Manager, Engagement Management - EMEA
Go To Market - London, UK and Dublin, Ireland

Apply now(opens in a new window)
About the Team
The Engagement Management team ensures the successful post-sales deployment and value realization of ChatGPT Enterprise and other OpenAI products for customers across  industries.  Engagement Managers collaborate closely with Sales, Technical Success, and Product teams to deliver exceptional AI experiences and measurable business results. Our customers span Large Enterprise, Digital Native, and Startup organizations. As the leader of Engagement Managers in EMEA, you’ll help companies transform their business by adopting solutions that make use of our newest, most exciting models.

About the Role

We are seeking an Engagement Manager leader to ensure the post-sales success of our EMEA customers. In this role, you will oversee strategic implementations, customer adoption, and the development of scalable systems and processes. Success will be measured by customer activation and adoption, live production deployments, and customer satisfaction. You will partner with Sales, Solutions Engineering, Solutions Architecture, and Product teams. 

This role is open in our London office. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Own the strategy and operating model of the EMEA Engagement Management team, ensuring alignment with company objectives and the evolving needs of our customers.

Lead, build, and mentor a team of high-performing Engagement Managers to deliver exceptional customer outcomes, as demonstrated by production customer deployments, increased adoption, and customer satisfaction. 

Act as the primary technical escalation point during implementation, fostering trust and maintaining direct communication with executive-level stakeholders.

Represent the voice of the customer by synthesizing feedback and identifying recurring themes to influence product development and strategic planning.

You’ll thrive in this role if you:

Have 6+ years of experience in a customer-facing role, managing C-level technical and business relationships with complex global organizations.

Have 2+ years of experience leading post-sales teams with a demonstrated ability to hire, develop, and manage technical teams.

Have led complex implementations of Generative AI/traditional ML solutions and can drive measurable business outcomes.

Are an effective presenter and communicator who can translate business and technical topics to all audiences, including senior leaders.

Own problems end-to-end and are willing to pick up whatever knowledge you're missing to get the job done.

Have a humble attitude, an eagerness to help your colleagues, and a desire to do whatever it takes to make the team succeed.

Compensation, Benefits and Perks

This is a position with OpenAI UK Ltd., which controls the hiring and management of this position. Total compensation includes competitive salary, generous equity and benefits.

Private medical insurance covering 100% of premiums for employees and their dependents

Pension plan with 4% employer contribution

52 weeks maternity leave and 20 weeks parental leave

Unlimited time off

Annual learning & development stipend ($1,500 USD equivalent per year)

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.



43. ML Training Infrastructure Manager - Reasoning
AI Scientist - San Francisco

Apply now(opens in a new window)
About the Team
The RL team drives the core reasoning paradigm and has created groundbreaking innovations such as O1 and O3. We focus on pushing the boundaries of reinforcement learning research, building next-generation generative models, and deploying them at scale. As the leader of this team, you will help shape the future of reasoning by building new large-scale ML training infrastructure and playing a pivotal role in major research roadmaps and decision-making processes.

About the Role
Lead a Higher-Caliber Team: Manage, mentor, and grow a team of ML infrastructure experts focused on designing and building large-scale systems for reinforcement learning training.

Architect Scalable Training Platforms: Oversee the creation and optimization of distributed systems that handle massive amounts of data, ensuring robust performance and reliability.

Embed with Research: Collaborate closely with the core reasoning research team to integrate novel approaches and breakthroughs into production pipelines.

Ensure Operational Excellence: Define, implement, and maintain best practices for development, deployment, monitoring, and quality assurance across ML training infrastructure.

Drive Technical Roadmaps: Contribute to and influence the overall technical direction of RL research, prioritizing key infrastructure investments to enable cutting-edge science.

We Are Looking For:
Passion for AI and Research: Genuine enthusiasm for advancing the frontiers of AI/AGI research, with a strong desire to help shape the future of reasoning.

Technical Expertise: Proven track record of leading world-class teams in large-scale distributed system design for ML training.

Leadership: Ability to define and translate a broad vision into ambitious, actionable milestones that energize teams; experience in leading, mentoring, and developing high-performing teams.

Collaboration & Communication: Exceptional ability to build strong, productive partnerships across cross-functional teams. Skilled at navigating diverse perspectives, fostering alignment, and driving innovation to achieve organizational goals.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$360K – $440K + Offers Equity




44. Platform ML Engineering Manager, Model Graph
Platform - San Francisco

Apply now(opens in a new window)
About the Team

The Platform ML team builds the ML side of our state-of-the-art internal training framework used to train our cutting-edge models.  We work on distributed model execution as well as the interfaces and implementation for model code, training, and inference.

Our priorities are to maximize training throughput (how quickly we can train a new model) and researcher throughput (how quickly we can develop new models) with the goal of accelerating progress towards AGI.  We frequently collaborate with other teams to speed up the development of new capabilities.

About the Role

We are looking for an experienced engineering manager to help lead critical work on model definition and efficient distributed execution within our shared internal training stack.  Our internal training stack is used by Research for large scale and small scale runs.

In this role, you will:

Reduce the time it takes to try out new architecture ideas for training new models and increase the robustness of model code.

Collaborate closely with researchers and other systems engineers to maximize the benefits of our shared internal training stack.

Make it feasible to get SOTA throughput for our most important research models.

Hire world-class AI systems engineers in one of the most competitive hiring markets.

Coordinate the training needs of OpenAI's research teams.

Create a diverse, equitable, and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group think.

You might thrive in this role if you:

Have 3+ years of experience in engineering management and 7+ years as an IC working with high scale distributed systems and ML systems.

Have experience with ML systems, particularly high scale distributed training or inference for modern LLMs.

Have familiarity with the latest AI research and working knowledge of how these systems are efficiently implemented.

Care deeply about diversity, equity, and inclusion, and have a track record of building inclusive teams.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$440K – $530K + Offers Equity




45. Platform ML Engineering Manager, Training
Platform - San Francisco

Apply now(opens in a new window)
About the Team

The Platform ML team builds the ML side of our state-of-the-art internal training framework used to train our cutting-edge models.  We work on distributed model execution as well as the interfaces and implementation for model code, training, and inference.

Our priorities are to maximize training throughput (how quickly we can train a new model) and researcher throughput (how quickly we can develop new models) with the goal of accelerating progress towards AGI.  We frequently collaborate with other teams to speed up the development of new capabilities.

About the Role

We are looking for an experienced engineering manager to help lead critical work on our shared internal training stack and grow the team. Our training stack is primarily by teams in Research Platform.

In this role, you will:

Get SOTA throughput for our most important research models.

Reduce the time it takes to try out new research ideas for training new models.

Collaborate closely with researchers and other systems engineers to maximize the benefits of our shared internal training stack.

Hire world-class AI systems engineers in one of the most competitive hiring markets.

Coordinate the training needs of OpenAI's research teams.

Create a diverse, equitable, and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group think.

You might thrive in this role if you:

Have 3+ years of experience in engineering management and 7+ years as an IC working with high scale distributed systems and ML systems.

Have experience with ML systems, particularly high scale distributed training or inference for modern LLMs.

Have familiarity with the latest AI research and working knowledge of how these systems are efficiently implemented.

Care deeply about diversity, equity, and inclusion, and have a track record of building inclusive teams.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$440K – $530K + Offers Equity




46. Principal Engineer, GPU Platform
Applied AI Infrastructure - San Francisco

Apply now(opens in a new window)
About the Team
The Applied Engineering team works across research, engineering, product, and design to bring OpenAI’s technology to consumers and businesses.
You’ll join the team responsible for running the infrastructure that supports the models backing ChatGPT and the API. The systems we support include inference kubernetes clusters, GPU health, Infiniband performance, node lifecycle, and more.We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

About the Role
The inference compute team builds and maintains infrastructure abstractions allowing OpenAI to run models at scale.
This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Design and build the inference infrastructure that power our products, enabling reliability and performance

Ensure our infrastructure can scale to the next order of magnitude

Help create a diverse, equitable, and inclusive culture that makes all feel welcome while enabling radical candor and the challenging of group think

Like all other teams, we are responsible for the reliability of the systems we build. This includes an on-call rotation to respond to critical incidents as needed.

You might thrive in this role if you:

Have 10+ years building core infrastructure

Have experience running GPU clusters at scale

Have experience operating orchestration systems such as Kubernetes at scale

Take pride in building and operating scalable, reliable, secure systems

Are comfortable with ambiguity and rapid change

This role is exclusively based in our San Francisco HQ. We offer relocation assistance to new employees.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$385K – $550K + Offers Equity



47. Product Security Leader
Security - San Francisco

Apply now(opens in a new window)
About the Team

Security is at the foundation of OpenAI’s mission to ensure that artificial general intelligence benefits all of humanity.  

The Security team protects OpenAI’s technology, people, and products. We are technical in what we build but are operational in how we do our work, and are committed to supporting all products and research at OpenAI. Our Security team tenets include: prioritizing for impact, enabling researchers, preparing for future transformative technologies, and engaging a robust security culture. 

 About the Role

The Product Security Leader is responsible for ensuring the security and integrity of all products throughout their lifecycle, from development to deployment and maintenance. This role involves leading a team of security experts to identify vulnerabilities, implement robust security measures, and respond to emerging threats. Additionally, the Head of Product Security collaborates with cross-functional teams to integrate security best practices into product design and development processes, ensuring compliance with industry standards and regulations.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Develop and Implement Security Strategies: Formulate and execute comprehensive security policies, procedures, and frameworks to protect the product lifecycle from design to deployment.

Team Leadership and Management: Lead, mentor, and manage a team of security professionals, ensuring they are equipped with the necessary skills and resources to address security challenges.

Risk Assessment and Mitigation: Conduct regular risk assessments, vulnerability assessments, and threat modeling to identify and mitigate potential security risks in products.

Incident Response and Management: Oversee the response to security incidents, coordinating efforts to investigate, contain, and resolve breaches or vulnerabilities effectively.

Collaboration with Development Teams: Work closely with product development teams to integrate security best practices into the software development lifecycle, ensuring security is built into products from the ground up.

Compliance and Regulatory Adherence: Ensure that all products comply with relevant industry standards, regulations, and security certifications, keeping abreast of evolving security requirements and legislation.

 You might thrive in this role if you:

Extensive experience in information security, cybersecurity, or a related field, with a significant portion of that experience in leadership or management roles.

Deep understanding of security technologies, tools, and best practices, including experience with secure coding practices, threat modeling, risk assessments, and incident response.

Proven ability to lead and manage a team of security professionals, with strong skills in mentoring, coaching, and developing talent.

Excellent verbal and written communication skills, with the ability to effectively communicate security concepts to both technical and non-technical stakeholders and collaborate with cross-functional teams.

Up-to-date knowledge of current and emerging security threats, trends, and technologies, as well as familiarity with relevant regulatory and compliance requirements.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$385K – $465K + Offers Equity




48. Research Engineer
Research - San Francisco

Apply now(opens in a new window)
By applying to this role, you will be considered for Research Engineer roles across all teams at OpenAI.

About the Role

As a Research Engineer here, you will be responsible for building AI systems that can perform previously impossible tasks or achieve unprecedented levels of performance. We're looking for people with solid engineering skills (for example designing, implementing, and improving a massive-scale distributed machine learning system), writing bug-free machine learning code, and building the science behind the algorithms employed. 

The most outstanding deep learning results are increasingly attained at a massive scale, and these results require engineers who are comfortable working in large distributed systems. We expect engineering to play a key role in most major advances in AI of the future.

We expect you to:

Have strong programming skills

Have experience working in large distributed systems

Be excited about OpenAI’s approach to research 

Nice to have: 

Interested in and thoughtful about the impacts of AI technology

Past experience in creating high-performance implementations of deep learning algorithms

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$295K – $440K + Offers Equity




49. Research Engineer, Data Processing (Foundations)
Foundations - San Francisco

Apply now(opens in a new window)
About the Team

At OpenAI, we strongly believe in the importance of data and have seen repeatedly how large of an impact focusing on data quality can yield across all of our projects. The Data Processing team brings this focus to our flagship GPT models, owning the pipelines for turning raw data into the high quality, diverse, and multimodal datasets used to train our largest models. We work closely with teams focused on data acquisition, data quality, and multimodal data throughout Research. Most recently, in collaboration with these groups, we were responsible for building the dataset used to pre-train OpenAI’s newest multimodal model GPT-4o. 

In addition to building new datasets, we collaborate on data research and acquisition with teams in Research and Multimodal to explore ways to get more out of data, including questions around efficiency, efficacy, and diversity. We also own and continuously improve the infrastructure used across several teams to prepare data for training models small and large.

About the Role

As a Research Engineer here, you will be responsible for building AI systems that can perform previously impossible tasks or achieve unprecedented levels of performance.  We're looking for people with solid engineering skills who are comfortable working with large distributed systems and strive to write quality, well tested code.

The most outstanding deep learning results are increasingly attained at a massive scale, and these results require engineers who are comfortable working in large distributed systems.  We expect engineering to play a key role in most major advances in AI of the future.

In this role, you will:

Build and own data pipelines operating on internet-scale data spanning the text, image, and audio modalities

Collaborate with many teams within Foundations and across Research to incorporate our latest and greatest research into pre-training datasets

Research new methods for improving our datasets alongside researchers within Foundations

You might thrive in this role if you: 

Enjoy working at the cutting-edge of large language model research

Have experience running complicated processing on very large datasets

Are comfortable working in a fast-paced, dynamic environment - research can evolve quite rapidly!

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$360K – $530K + Offers Equity



50.Research Engineer, Future of Computing
Applied AI Engineering - San Francisco

Apply now(opens in a new window)
About the Team

The Future of Computing is an Applied Research team focused on prototyping and exploring how (consumer) computing might holistically evolve as we advance on our mission of building AGI.

About the Role

As a Research Engineer on the Future of Computing team, you will work together with both the best research scientists in the world and the greatest design talent of our generation to push the frontier of model capabilities. The ideal candidate will have a strong research background in addition to experience shipping AI products.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role you will:

Train and evaluate multimodal SoTA models along axis that are important to our emerging explorations.

Run through the necessary walls to take nascent research capabilities and turn them into capabilities we can build on top of.

Be one of the first members of the team and help define our team culture and how we work together.

You might thrive in this role if you:

Experience training and fine-tuning large multimodal LLMs

Experience building applications with LLMs

Have strong engineering skills to unblock yourself

Have strong cross-functional skills to speak the “language” of both research and product.

Love exposure to a bit of everything – we’re collaborators with a hugely diverse set of research.

Do rigorous science (rather than vibes based). We need confidence in the experiments we run to move quickly.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$360K – $440K + Offers Equity



51. Research Engineer, Multimodal Safety
Multimodal - San Francisco

Apply now(opens in a new window)
About the Team

Our team is dedicated to shaping the future of artificial intelligence by equipping ChatGPT with the ability to hear, see, speak, and create visually compelling images, transforming how people interact with AI in everyday life. We prioritize safety throughout the development process to ensure that our most advanced models can be safely deployed in real-world applications, ultimately benefiting society. This focus on safety is central to OpenAI’s mission of building and deploying safe AGI, reinforcing our dedication to AI safety and promoting a culture of trust and transparency.

About the Role

We are seeking a research engineer to pioneer innovative techniques that redefine safety, enhancing the comprehension and capabilities of our state-of-the-art multimodal foundation models. In this role, you will conduct rigorous safety assessments and develop methods, such as safety reward models and multimodal classifiers, to ensure our models are intrinsically compliant with safety protocols. You will also help with red teaming efforts to test the robustness of our models, collaborating closely with cross-functional teams, including safety and legal, to ensure our systems meet all safety standards and legal requirements.

The ideal candidate has a solid foundation in multimodal research and post training techniques, with a passion for pushing boundaries and achieving tangible impact. Familiarity with large suites of metrics or human data pipelines is a plus. You should be adept at writing high-quality code, developing tools for model evaluation, and iteratively improving our metrics based on real-world feedback. Strong communication skills are essential to work effectively with both technical and non-technical stakeholders.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

Build evaluation pipelines to assess risk along various axes, especially with multimodal inputs and outputs.

Implement risk mitigation techniques such as building safety reward models and RL. 

Develop and refine multimodal moderation models to detect and mitigate known and emerging patterns of AI misuse and abuse.

Work with other safety teams within the company to iterate on our content policies to ensure effective prevention of harmful behavior. 

Work with our human data team to conduct internal and external red teaming to examine the robustness of our harm prevention systems and identify areas for future improvement.

Write maintainable, efficient, and well-tested code as part of our evaluation libraries.

You might thrive in this role if you:

Are a collaborative team player – willing to do whatever it takes in a start-up environment.

Have experience working in complex technical environments.

Are passionate about bringing magical AI experiences to millions of users.

Enjoy diving into the subtle details of datasets and evaluations.

Have experience with multimodal research and post-training techniques.

Are very proficient in Python.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$295K – $440K




52. Research Engineer, Preparedness
Safety Systems - San Francisco

Apply now(opens in a new window)
About the team

The Safety Systems team is responsible for various safety work to ensure our best models can be safely deployed to the real world to benefit the society and is at the forefront of OpenAI's mission to build and deploy safe AGI, driving our commitment to AI safety and fostering a culture of trust and transparency.

Frontier AI models have the potential to benefit all of humanity, but also pose increasingly severe risks. To ensure that AI promotes positive change, the Preparedness team helps us prepare for the development of increasingly capable frontier AI models. This team is tasked with identifying, tracking, and preparing for catastrophic risks related to frontier AI models.

Specifically, the mission of the Preparedness team is to:

Closely monitor and predict the evolving capabilities of frontier AI systems, with an eye towards misuse risks whose impact could be catastrophic (not necessarily existential) to our society; and

Ensure we have concrete procedures, infrastructure and partnerships to mitigate these risks and, more broadly, to safely handle the development of powerful AI systems.

Our team will tightly connect capability assessment, evaluations, and internal red teaming for frontier models, as well as overall coordination on AGI preparedness. The team’s core goal is to ensure that we have the infrastructure needed for the safety of highly-capable AI systems—from the models we develop in the near future to those with AGI-level capabilities. 

About you

We are looking to hire exceptional research engineers that can push the boundaries of our frontier models. Specifically, we are looking for those that will help us shape our empirical grasp of the whole spectrum of AI safety concerns and will own individual threads within this endeavor end-to-end.

In this role, you'll:

Work on identifying emerging AI safety risks and new methodologies for exploring the impact of these risks

Build (and then continuously refine) evaluations of frontier AI models that assess the extent of identified risks

Design and build scalable systems and processes that can support these kinds of evaluations

Contribute to the refinement of risk management and the overall development of "best practice" guidelines for AI safety evaluations

We expect you to be:

Passionate and knowledgeable about short-term and long-term AI safety risks

Able to think outside the box and have a robust “red-teaming mindset”

Experienced in ML research engineering, ML observability and monitoring, creating large language model-enabled applications, and/or another technical domain applicable to AI risk

Able to operate effectively in a dynamic and extremely fast-paced research environment as well as scope and deliver projects end-to-end

It would be great if you also have:

First-hand experience in red-teaming systems—be it computer systems or otherwise

A good understanding of the (nuances of) societal aspects of AI deployment

An ability to work cross-functionally

Excellent communication skills

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$200K – $370K + Offers Equity




53. Research Engineer, Pre-training Architecture
Foundations - San Francisco

Apply now(opens in a new window)
About the Team

The architecture team is responsible for advancing the neural network architecture of OpenAI’s flagship language models. Our work spans the entire spectrum of architecture development and deployment all the way from the foundational science to the engineering that allows us to train and deploy our models efficiently at scale. Our work has tremendous leverage and deep implications across our stack and we collaborate closely with many other research and engineering teams.

About the Role

As a Research Engineer, you will develop a deep understanding about model architectures and iterate on research ideas to improve OpenAI's frontier models. You will systematically study existing architectures and come up with and implement novel ideas to gain understanding and find improvements to our state-of-the-art models.

You might thrive in this role if you:

Are passionate about building mathematical intuitions and performing careful empirical research

Have strong software engineering skills

Are familiar with distributed systems and computer architectures

Enjoy developing deep a understanding of complex systems and collaborating closely with other researchers and engineers

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$360K – $530K + Offers Equity




54. Research Engineer / Research Scientist, Alignment
Alignment - San Francisco

Apply now(opens in a new window)
About the Team

The Alignment team at OpenAI is dedicated to ensuring that our AI systems are safe, trustworthy, and consistently aligned with human values, even as they scale in complexity and capability. Our work is at the cutting edge of AI research, focusing on developing methodologies that enable AI to robustly follow human intent across a wide range of scenarios, including those that are adversarial or high-stakes. We concentrate on the most pressing challenges, ensuring our work addresses areas where AI could have the most significant consequences. By focusing on risks that we can quantify and where our efforts can make a tangible difference, we aim to ensure that our models are ready for the complex, real-world environments in which they will be deployed.

The two pillars of our approach are: (1) harnessing improved capabilities into alignment, making sure that our alignment techniques improve, rather than break, as capabilities grow, and (2) centering humans by developing mechanisms and interfaces that enable humans to both express their intent and to effectively supervise and control AIs, even in highly complex situations.

About the Role

As a Research Engineer / Research Scientist on the Alignment team, you will be at the forefront of ensuring that our AI systems consistently follow human intent, even in complex and unpredictable scenarios. Your role will involve designing and implementing scalable solutions that ensure the alignment of AI as their capabilities grow and that integrate human oversight into AI decision-making.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

We are seeking research engineers and research scientists to help design and implement experiments for alignment research. Responsibilities may include:

Develop and evaluate alignment capabilities that are subjective, context-dependent, and hard to measure.

Design evaluations to reliably measure risks and alignment with human intent and values.

Build tools and evaluations to study and test model robustness in different situations.

Design experiments to understand laws for how alignment scales as a function of compute, data, lengths of context and action, as well as resources of adversaries.

Design and evaluate new Human-AI-interaction paradigms and scalable oversight methods that redefine how humans interact with, understand, and supervise our models.

Train model to be calibrated on correctness and risk.

Designing novel approaches for using AI in alignment research

You might thrive in this role if you:

Are a team player – willing to do a variety of tasks that move the team forward.

Have a PhD or equivalent experience in research in computer science, computational science, data science, cognitive science, or similar fields.

Have strong engineering skills, particularly in designing and optimizing large-scale machine learning systems(e.g., PyTorch).

Have a deep understanding of the science behind alignment algorithms and techniques.

Can develop data visualization or data collection interfaces (e.g., TypeScript, Python).

Enjoy fast-paced, collaborative, and cutting-edge research environments.

Want to focus on developing AI models that are trustworthy, safe, and reliable, especially in high-stakes scenarios.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$295K – $440K + Offers Equity



55. Research Engineer / Research Scientist, Alignment
Alignment - San Francisco

Apply now(opens in a new window)
About the Team

The Alignment team at OpenAI is dedicated to ensuring that our AI systems are safe, trustworthy, and consistently aligned with human values, even as they scale in complexity and capability. Our work is at the cutting edge of AI research, focusing on developing methodologies that enable AI to robustly follow human intent across a wide range of scenarios, including those that are adversarial or high-stakes. We concentrate on the most pressing challenges, ensuring our work addresses areas where AI could have the most significant consequences. By focusing on risks that we can quantify and where our efforts can make a tangible difference, we aim to ensure that our models are ready for the complex, real-world environments in which they will be deployed.

The two pillars of our approach are: (1) harnessing improved capabilities into alignment, making sure that our alignment techniques improve, rather than break, as capabilities grow, and (2) centering humans by developing mechanisms and interfaces that enable humans to both express their intent and to effectively supervise and control AIs, even in highly complex situations.

About the Role

As a Research Engineer / Research Scientist on the Alignment team, you will be at the forefront of ensuring that our AI systems consistently follow human intent, even in complex and unpredictable scenarios. Your role will involve designing and implementing scalable solutions that ensure the alignment of AI as their capabilities grow and that integrate human oversight into AI decision-making.

This role is based in San Francisco, CA. We use a hybrid work model of 3 days in the office per week and offer relocation assistance to new employees.

In this role, you will:

We are seeking research engineers and research scientists to help design and implement experiments for alignment research. Responsibilities may include:

Develop and evaluate alignment capabilities that are subjective, context-dependent, and hard to measure.

Design evaluations to reliably measure risks and alignment with human intent and values.

Build tools and evaluations to study and test model robustness in different situations.

Design experiments to understand laws for how alignment scales as a function of compute, data, lengths of context and action, as well as resources of adversaries.

Design and evaluate new Human-AI-interaction paradigms and scalable oversight methods that redefine how humans interact with, understand, and supervise our models.

Train model to be calibrated on correctness and risk.

Designing novel approaches for using AI in alignment research

You might thrive in this role if you:

Are a team player – willing to do a variety of tasks that move the team forward.

Have a PhD or equivalent experience in research in computer science, computational science, data science, cognitive science, or similar fields.

Have strong engineering skills, particularly in designing and optimizing large-scale machine learning systems(e.g., PyTorch).

Have a deep understanding of the science behind alignment algorithms and techniques.

Can develop data visualization or data collection interfaces (e.g., TypeScript, Python).

Enjoy fast-paced, collaborative, and cutting-edge research environments.

Want to focus on developing AI models that are trustworthy, safe, and reliable, especially in high-stakes scenarios.

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. 

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status. 

OpenAI Affirmative Action and Equal Employment Opportunity Policy Statement

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$295K – $440K + Offers Equity






# OpenAI
174 jobs
All teams
All locations
Account Director - Japan
Sales
Tokyo, Japan
Apply now
AI Abuse & Threat Intelligence Analyst
Intelligence & Investigations
San Francisco
Apply now
AI Policy Counsel
Legal
San Francisco
Apply now
Analytics Data Engineer, Applied Engineering
Applied AI Engineering
San Francisco
Apply now
Analytics Engineer
Growth
San Francisco
Apply now
Android Engineer, ChatGPT Core Experiences
Applied AI Engineering
San Francisco
Apply now
Android Engineer, ChatGPT Search
Applied AI Engineering
San Francisco
Apply now
Backend Software Engineer, Intelligent Support Engineering
User Operations
San Francisco
Apply now
Backend Software Engineer, Leverage Engineering
Leverage Engineering
Apply now
Bizops Lead
Business Operations
San Francisco
Apply now
Client Platform Engineer
IT
San Francisco
Apply now
Compliance Program Manager
Security
San Francisco
Apply now
Compute & Infrastructure Accounting Manager
Finance
San Francisco
Apply now
Customer Support Engineer
User Operations
San Francisco
Apply now
Customer Support Engineer (User Operations Generalist)
User Operations
Apply now
Cybersecurity Evaluations Engineer
Safety Systems
San Francisco
Apply now
Data Engineer, Safety Systems
Applied AI Engineering
San Francisco
Apply now
Data Infrastructure Engineer
Applied AI Engineering
San Francisco
Apply now
Data Scientist, Business
Growth
Apply now
Data Scientist, Monitoring Operations
Intelligence & Investigations
Apply now
Data Scientist, Product
Data Science
San Francisco
Apply now
Deal Desk Manager - EMEA
Finance
Dublin, Ireland
Apply now
Developer Advocate, Developer Experience
Go To Market
London, UK
Apply now
Developer Advocate, Developer Experience - Japan
Technical Success
Tokyo, Japan
Apply now
Developer Advocate, Developer Experience - Singapore
Go To Market
Remote - Singapore
Apply now
Distributed Training Engineer, Sora
Sora
San Francisco
Apply now
Engagement Manager
Customer Success
San Francisco
Apply now
Engineering Manager, Applied GPU Platform
Applied AI Engineering
San Francisco
Apply now
Engineering Manager, Automation
User Operations
San Francisco
Apply now
Engineering Manager, Distributed Systems
Platform
San Francisco
Apply now
Engineering Manager, Financial Systems
Applied AI Engineering
San Francisco
Apply now
Engineering Manager, Human Data
Human Data
San Francisco
Apply now
Engineering Manager, Observability
Applied AI Engineering
San Francisco
Apply now
Enterprise Security Engineer
IT
San Francisco
Apply now
Enterprise Site Reliability Engineer
IT
San Francisco
Apply now
Executive Business Partner
Executive Operations
San Francisco
Apply now
Financial Systems Senior Manager
Finance
San Francisco
Apply now
Firmware Engineer
Platform
San Francisco
Apply now
Forward Deployed Engineer
Go To Market
San Francisco
Apply now
Front End Software Engineer, Leverage Engineering
Leverage Engineering
Apply now
Full-Stack Engineer
Applied AI
Apply now
Full-Stack Software Engineer, Intelligent Support Engineering
User Operations
San Francisco
Apply now
Full Stack Software Engineer, Leverage Engineering
Leverage Engineering
Apply now
GTM Enablement Lead - Japan
Revenue Operations
Tokyo, Japan
Apply now
Head of Data Science, Strategic Finance
Strategic Finance
San Francisco
Apply now
Head of Global Mobility
People
Apply now
Head of People Systems
People
Apply now
HW/SW Co-Design Engineer
Platform
San Francisco
Apply now
Infrastructure Engineer
Applied AI
Apply now
International Controller
Finance
Dublin, Ireland
Apply now
International Strategy & Ops Lead
Go To Market
San Francisco
Apply now
iOS Engineer, ChatGPT Core Experiences
Applied AI Engineering
San Francisco
Apply now
Lead Product Manager, Core Product
Product Management
San Francisco
Apply now
Machine Learning Engineer, Applied AI
Applied AI Engineering
San Francisco
Apply now
Machine Learning Engineer, Integrity
Applied AI Engineering
San Francisco
Apply now
Machine Learning Engineer, Retrieval & Search
Applied AI Engineering
San Francisco
Apply now
Manager, Customer Success, Strategics
Customer Success
San Francisco
Apply now
Manager, Engagement Management - EMEA
Go To Market
Apply now
Mechanical Engineer
Platform
San Francisco
Apply now
Mechanical Product Engineer, Robotics
New Product Explorations
San Francisco
Apply now
ML Training Infrastructure Manager - Reasoning
AI Scientist
San Francisco
Apply now
Platform ML Engineering Manager, Model Graph
Platform
San Francisco
Apply now
Platform ML Engineering Manager, Training
Platform
San Francisco
Apply now
Principal Engineer, GPU Platform
Applied AI Infrastructure
San Francisco
Apply now
Product Manager, ChatGPT for Work
Product Management
San Francisco
Apply now
Product Manager, ChatGPT Growth
Product Management
San Francisco
Apply now
Product Manager, International Growth
Product Management
San Francisco
Apply now
Product Manufacturing Engineer
Platform
San Francisco
Apply now
Product Quality Engineer
Platform
San Francisco
Apply now
Product Security Leader
Security
San Francisco
Apply now
Research Engineer
Research
San Francisco
Apply now
Research Engineer, Data Processing (Foundations)
Foundations
San Francisco
Apply now
Research Engineer, Future of Computing
Applied AI Engineering
San Francisco
Apply now
Research Engineer, Multimodal Safety
Multimodal
San Francisco
Apply now
Research Engineer, Preparedness
Safety Systems
San Francisco
Apply now
Research Engineer, Pre-training Architecture
Foundations
San Francisco
Apply now
Research Engineer / Research Scientist, Alignment
Alignment
San Francisco
Apply now
Research Engineer / Research Scientist, Post-Training
Post-training
San Francisco
Apply now
Research Engineer / Scientist, ChatGPT RLHF
Post-training
San Francisco
Apply now
Research Engineer / Scientist - Multimodal Product Oriented Research
Post-training
San Francisco
Apply now
Research Engineer / Scientist - Perception
Multimodal
San Francisco
Apply now
Research Engineer/Scientist, Personality and Model Behavior
Post-training
San Francisco
Apply now
Research Engineer/Scientist, Robustness & Safety Training
Safety Systems
San Francisco
Apply now
Research Engineer / Scientist, Safety Reasoning
Safety Systems
San Francisco
Apply now
Researcher (Engineer/Scientist), Training Architecture
Training
San Francisco
Apply now
Research Infrastructure Engineer - Post-Training
Post-training
San Francisco
Apply now
Research Manager, Alignment
Alignment
San Francisco
Apply now
Research Scientist
Research
San Francisco
Apply now
Research Scientist - CoT, Science of Deep Learning
Reinforcement Learning
San Francisco
Apply now
Research Scientist, Health AI
Safety Systems
San Francisco
Apply now
Research Scientist, Human-AI Interaction
Human Data
San Francisco
Apply now
Research Scientist, Scaling Laws (Foundations)
Foundations
San Francisco
Apply now
Security Engineer, Application Security
Security
San Francisco
Apply now
Security Engineer, Detection & Response - Japan
Security
Tokyo, Japan
Apply now
Security Engineer, Detection & Response - Singapore
Security
Remote - Singapore
Apply now
Senior Employee Relations Investigator
People
Apply now
Senior Manager, Revenue Systems
Finance
San Francisco
Apply now
Senior Software Engineer, Data Acquisition
Foundations
San Francisco
Apply now
Senior Software Engineer, Identity Platform
Applied AI Engineering
San Francisco
Apply now
Site Reliability Engineer
Applied AI
Apply now
Site Reliability Engineer, Enterprise IAM
IT
San Francisco
Apply now
Software Engineer, Account Protection
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Agent Infrastructure
Research
San Francisco
Apply now
Software Engineer, Anti Fraud & Abuse
Applied AI Engineering
San Francisco
Apply now
Software Engineer - API Designer
Applied AI Engineering
San Francisco
Apply now
Software Engineer – API SDK
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Applied Engineering
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Backend
Sora
San Francisco
Apply now
Software Engineer, Backend
Applied AI Engineering
San Francisco
Apply now
Software Engineer, ChatGPT Enterprise
Applied AI Engineering
Seattle
Apply now
Software Engineer, Data Acquisition
Foundations
San Francisco
Apply now
Software Engineer, Data Visualization
Platform
San Francisco
Apply now
Software Engineer, Developer Productivity
Platform
San Francisco
Apply now
Software Engineer, Dev Productivity
Applied AI Infrastructure
San Francisco
Apply now
Software Engineer, Distributed Systems
Platform
San Francisco
Apply now
Software Engineer, Financial Engineering
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Financial Tooling
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Frontend
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Full Stack
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Full Stack (People Innovation)
People
San Francisco
Apply now
Software Engineer, Infrastructure
Applied AI Infrastructure
San Francisco
Apply now
Software Engineer, Integrity Foundations
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Model Inference
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Networking
Platform
San Francisco
Apply now
Software Engineer, Observability
Applied AI Infrastructure
San Francisco
Apply now
Software Engineer - Power Management, Hardware Health
Platform
San Francisco
Apply now
Software Engineer, Privacy
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Real Time
Applied AI Engineering
Seattle
Apply now
Software Engineer, Reliability
Applied AI Infrastructure
San Francisco
Apply now
Software Engineer, Safety
Safety Systems
San Francisco
Apply now
Software Engineer, Security Product and Platform
Security
Apply now
Software Engineer, Systems Generalist
Applied AI Engineering
San Francisco
Apply now
Software Engineer, Triton Compiler
Platform
San Francisco
Apply now
Solutions Architect
Applied AI
Apply now
Solutions Architect, Digital Natives
Technical Success
San Francisco
Apply now
Solutions Architect, Enterprise
Technical Success
London, UK
Apply now
Solutions Architect, Enterprise
Technical Success
Apply now
Solutions Architect Manager, EMEA
Technical Success
London, UK
Apply now
Solutions Architect Manager, Strategics
Technical Success
San Francisco
Apply now
Solutions Architect, Startups
Technical Success
San Francisco
Apply now
Solutions Architect, Startups
Technical Success
London, UK
Apply now
Solutions Architect, Strategics
Technical Success
New York City
Apply now
Solutions Engineer - DACH
Go To Market
London, UK
Apply now
Solutions Engineer, Large Enterprise and Digital Natives, EMEA
Technical Success
London, UK
Apply now
Solutions Engineer, Midmarket and Enterprise
Technical Success
San Francisco
Apply now
Solutions Engineer, Midmarket and Enterprise
Technical Success
New York City
Apply now
Solutions Engineer, Midmarket and Enterprise - EMEA
Technical Success
London, UK
Apply now
Solutions Engineer, Startups
Technical Success
San Francisco
Apply now
Sr. Engineering Manager, Data Acquisition (Foundations)
Foundations
San Francisco
Apply now
Strategic Finance, Analyst (Infrastructure)
Strategic Finance
San Francisco
Apply now
Strategic Finance, Compute
Strategic Finance
San Francisco
Apply now
Strategic Finance, Infrastructure
Strategic Finance
San Francisco
Apply now
Strategic Finance Lead, ChatGPT Team
Strategic Finance
San Francisco
Apply now
Strategic Finance Lead, Infrastructure Software
Strategic Finance
San Francisco
Apply now
Strategic Finance Lead, Marketing
Strategic Finance
San Francisco
Apply now
Strategic Finance Lead, Product
Strategic Finance
San Francisco
Apply now
Strategic Finance Lead, Product Revenue
Strategic Finance
San Francisco
Apply now
Strategic Finance Senior Analyst
Strategic Finance
San Francisco
Apply now
Stream Infrastructure Engineer
Applied AI Engineering
San Francisco
Apply now
Supercomputing, Infrastructure
Supercomputing
San Francisco
Apply now
Supercomputing, Software Engineer - Scheduling
Supercomputing
San Francisco
Apply now
Supercomputing, Software Engineer - Storage
Supercomputing
San Francisco
Apply now
Support Knowledge Management Architect
User Operations
San Francisco
Apply now
Systems Integration Electrical Engineer, Robotics
New Product Explorations
San Francisco
Apply now
Tech Lead Manager, ChatGPT Research Acceleration
Applied AI Engineering
San Francisco
Apply now
Tech Lead Manager, Data Acquisition (Foundations)
Foundations
San Francisco
Apply now
Tech Lead Manager, Human Data
Human Data
San Francisco
Apply now
Technical Revenue Accounting Manager
Finance
San Francisco
Apply now
TLM, Core Model, Post-Training
Post-training
San Francisco
Apply now
TLM, Developer Productivity
Platform
San Francisco
Apply now
TPM Manager, Robotics
New Product Explorations
San Francisco
Apply now
Workday Integrations Engineer
People
Apply now
Workday Systems Analyst for Compensation, Security, Reporting
People
Apply now
Workday Systems Analyst for Payroll, Absence, Time and Benefits
People
Apply now



