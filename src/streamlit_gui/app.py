import streamlit as st
from mnp_details_gui import save_mnp_detail
from mnp_details_gui import save_mmd_dpr_tab

st.title("Manpower Details")

# Create tabs and unpack the list into individual tab elements
tab1, tab2 = st.tabs(["Manpower Detail","DPR Update"])

# Use the first tab (index 0) with a context manager
with tab1:
    save_mnp_detail()
with tab2:
    save_mmd_dpr_tab()


# python -m streamlit run src/streamlit_gui/app.py