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


# def get_defect_by_multi_tab():
#     st.title("🔍 Filter Defect List")
#
#     # Status selection
#     select_status = st.selectbox("Choose Status:", ["Select Status", "Reported", "Closed"])
#
#     eqpmnt_list = []  # Initialize equipment list
#     if select_status != "Select Status":
#         eqp_list_response = requests.get(f"{API_URL}/equipment_list/{select_status}")
#         if eqp_list_response.status_code == 200:
#             eqp_list_json = eqp_list_response.json()
#             if isinstance(eqp_list_json, dict):  # Ensure it's a dictionary
#                 eqpmnt_list = [item["equipment_id"] for item in eqp_list_json.get("equipment_list", [])]
#         else:
#             eqpmnt_list = ["❌ Equipment list not fetched"]
#
#     select_eqp = st.selectbox("Choose Equipment:", ["Select Equipment"] + eqpmnt_list)
#
#     part_list = []  # Initialize part list
#     if select_eqp != "Select Equipment":
#         part_list_response = requests.get(f"{API_URL}/part_list/{select_eqp}")
#         if part_list_response.status_code == 200:
#             part_list_json = part_list_response.json()
#             if isinstance(part_list_json, dict):  # Ensure it's a dictionary
#                 part_list = [item["part_id"] for item in part_list_json.get("part_list", [])]
#         else:
#             part_list = ["❌ Parts not fetched"]
#
#     select_part = st.selectbox("Choose Part:", ["Select Part"] + part_list)
#
#     report_list = []  # Initialize defect list
#     if select_part != "Select Part":
#         report_list_response = requests.get(f"{API_URL}/distinct_defect/{select_part}")
#         if report_list_response.status_code == 200:
#             report_list_json = report_list_response.json()
#             if isinstance(report_list_json, dict):  # Ensure it's a dictionary
#                 report_list = [item["defect_description"] for item in report_list_json.get("distinct_defect", [])]
#         else:
#             report_list = ["❌ Report not fetched"]
#
#     select_report = st.selectbox("Choose Report:", ["Select Report"] + report_list)
#
#     assigned_technician = st.text_input("Technician Name")
#     type_of_activity = st.text_input("Type of Activity")
#     remarks = st.text_input("Additional Remarks")
#     consumption = st.text_input("Consumables")
#     spare = st.text_input("Spare Part Used")
#     defect_status = st.selectbox("Choose Status:", ["Reported", "Closed","Under Review","Resolved","Duplicate"])
#     downtime_hours = st.text_input("Down Time")
#     resolution_date = st.date_input("Rectification Date")
#     equipment_id = select_eqp
#     part_id = select_part
#     defect_description = select_report
#
#     if st.button("Update Defect to DB"):
#         response = requests.post(f"{API_URL}/update_defect/", json={
#
#               "assigned_technician": assigned_technician,
#               "defect_status": defect_status,
#               "downtime_hours": downtime_hours,
#               "remarks": remarks,
#               "type_of_activity": type_of_activity,
#               "consumption": consumption,
#               "spare": spare,
#               "resolution_date": resolution_date,
#               "equipment_id": equipment_id,
#               "part_id": part_id,
#               "defect_description": defect_description
#         },
#         timeout=10  # Timeout for robustness
#         )
#
#         # Handle response
#         if response.status_code == 200:
#             st.success("Defect updated successfully!")
#         else:
#             st.error(f"Failed to update defect. Error: {response.status_code} - {response.text}")

import streamlit as st
import requests

API_URL = "https://your-api-url.com"  # Ensure API_URL is defined


def fetch_data(endpoint):
    """Helper function to fetch data from the API."""
    try:
        response = requests.get(f"{API_URL}/{endpoint}", timeout=10)
        if response.status_code == 200:
            return response.json()
        st.error(f"Error fetching {endpoint}: {response.status_code}")
        return {}
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {str(e)}")
        return {}


def get_defect_by_multi_tab():
    st.title("🔍 Filter Defect List")

    # Status Selection
    select_status = st.selectbox("Choose Status:", ["Select Status", "Reported", "Closed"])

    eqpmnt_list = []
    if select_status != "Select Status":
        eqp_data = fetch_data(f"equipment_list/{select_status}")
        eqpmnt_list = [item["equipment_id"] for item in eqp_data.get("equipment_list", [])]

    select_eqp = st.selectbox("Choose Equipment:", ["Select Equipment"] + eqpmnt_list)

    part_list = []
    if select_eqp != "Select Equipment":
        part_data = fetch_data(f"part_list/{select_eqp}")
        part_list = [item["part_id"] for item in part_data.get("part_list", [])]

    select_part = st.selectbox("Choose Part:", ["Select Part"] + part_list)

    report_list = []
    if select_part != "Select Part":
        report_data = fetch_data(f"distinct_defect/{select_part}")
        report_list = [item["defect_description"] for item in report_data.get("distinct_defect", [])]

    select_report = st.selectbox("Choose Report:", ["Select Report"] + report_list)

    # Defect Update Form
    with st.form("update_defect_form"):
        assigned_technician = st.text_input("Technician Name")
        type_of_activity = st.text_input("Type of Activity")
        remarks = st.text_area("Additional Remarks")
        consumption = st.text_input("Consumables")
        spare = st.text_input("Spare Part Used")
        defect_status = st.selectbox("Defect Status:", ["Reported", "Closed", "Under Review", "Resolved", "Duplicate"])
        downtime_hours = st.number_input("Down Time (hrs)", min_value=0.0, step=0.5)
        resolution_date = st.date_input("Rectification Date")

        submit = st.form_submit_button("Update Defect to DB")

        if submit:
            payload = {
                "assigned_technician": assigned_technician,
                "defect_status": defect_status,
                "downtime_hours": downtime_hours,
                "remarks": remarks,
                "type_of_activity": type_of_activity,
                "consumption": consumption,
                "spare": spare,
                "resolution_date": resolution_date,
                "equipment_id": select_eqp,
                "part_id": select_part,
                "defect_description": select_report
            }

            try:
                response = requests.post(f"{API_URL}/update_defect/", json=payload, timeout=10)
                if response.status_code == 200:
                    st.success("Defect updated successfully!")
                else:
                    st.error(f"Failed to update defect: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error updating defect: {str(e)}")
