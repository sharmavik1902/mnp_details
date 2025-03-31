import streamlit as st
from mnp_details_gui import save_mnp_detail

st.title("Manpower Details")

# Create tabs and unpack the list into individual tab elements
tabs = st.tabs(["Manpower Detail"])

# Use the first tab (index 0) with a context manager
with tabs[0]:
    save_mnp_detail()


# python -m streamlit run src/streamlit_gui/app.py