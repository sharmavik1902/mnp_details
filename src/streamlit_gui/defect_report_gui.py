import requests
import streamlit as st
from datetime import datetime
import pandas as pd
API_URL = "https://mnp-details-gui.onrender.com"
'''-------------------------------------------------------------'''

def report_defect():
    st.title("Report Defect")

    equipment_id = st.text_input("Equipment Name")
    part_id = st.text_input("Affected Part")
    defect_description = st.text_input("Description")
    reported_by = st.text_input("Reported By")

    if st.button("Report Defect"):
        response = requests.post(f"{API_URL}/report_defect/", json={
            "equipment_id": equipment_id,
            "part_id": part_id,
            "defect_description": defect_description,
            "reported_by": reported_by,
        },
        timeout=10  # Timeout for robustness
        )

        # Handle response
        if response.status_code == 200:
            st.success("Defect updated successfully!")
        else:
            st.error(f"Failed to update defect. Error: {response.status_code} - {response.text}")

'''-------------------------------------------------------------------------------------------------'''


def get_defect_by_multi_tab():
    st.title("Filter Defect List")

    select_status = st.selectbox("Choo Status:", ["Reported", "Closed"])
    st.write(select_status)


    if select_status != "All":

        eqp_list_response = requests.get(f"{API_URL}/equipment_list/{select_status}")
        st.write(eqp_list_response)

        if eqp_list_response.status_code == 200:
            eqp_list_json = eqp_list_response.json()
            if isinstance(eqp_list_json, list):  # Ensure it is a list
                eqpmnt_list = [item["equipment_id"] for item in eqp_list_json]

    st.write(eqpmnt_list)
    select_eqp = st.selectbox("Choo Equipment", ["All"]+eqpmnt_list)

    part_list = []
    if select_eqp != "All":
        part_list_response = requests.get(f"{API_URL}/part_list/{select_eqp}")

        if part_list_response.status_code == 200:
            part_list_json = part_list_response.json()
            if isinstance(part_list_json, list):  # Ensure it is a list
                part_list = [item["part_id"] for item in part_list_json]

    select_defect = st.selectbox("Choo Defect", ["All"]+part_list)



