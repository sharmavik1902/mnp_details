import streamlit as st
from mnp_details_gui import save_mnp_detail, save_mmd_dpr_tab, fetch_equp_histry_tab
from defect_report_gui import report_defect, update_defect_by_multi_tab
from ai_ui import ai_filter

# App Title to onmot
st.title("🛠 ONMOT")

# User role selection
user_role = st.radio("Select Your Role:", ["Planner", "Worker"], horizontal=True)

# Define tabs based on role
if user_role == "Planner":
    tab_names = ["👷 Manpower Detail", "🔍 Equipment History", "⚙️ Update Defect", "AI Search"]
    tab_functions = [save_mnp_detail, fetch_equp_histry_tab, update_defect_by_multi_tab, ai_filter()]
elif user_role == "Worker":
    tab_names = ["📋 DPR Update", "⚠️ Report Defect"]
    tab_functions = [save_mmd_dpr_tab, report_defect]

# Display tabs dynamically
if tab_names:
    tab_instances = st.tabs(tab_names)
    for tab, func in zip(tab_instances, tab_functions):
        with tab:
            func()













# python -m streamlit run src/streamlit_gui/app.py