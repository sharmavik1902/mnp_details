import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import requests


API_URL = "https://mnp-details-gui.onrender.com"


# Load OpenAI API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Sample defects data (Replace this with your real data or load from DB)
defect_table = requests.get(f"{API_URL}/all_defect/")
data = pd.DataFrame(defect_table)

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Initialize LLM and agent
llm = OpenAI(temperature=0, openai_api_key=api_key)
agent = create_pandas_dataframe_agent(llm, df, verbose=False)

# Streamlit UI
st.set_page_config(page_title="Defect Query AI", layout="wide")
st.title("🧠 AI-Powered Defect Data Explorer")

query = st.text_input("Enter your query:", placeholder="e.g., show reported defects for Crusher 2 in March")



def ai_filter():
    if st.button("Run Query"):
        with st.spinner("Processing..."):
            try:
                result = agent.run(query)
                st.success("✅ Query executed successfully!")
                st.markdown("### 📊 Result:")
                st.write(result)
            except Exception as e:
                st.error(f"❌ Error: {e}")