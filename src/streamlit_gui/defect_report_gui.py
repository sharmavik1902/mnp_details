import requests
import streamlit as st
from datetime import datetime
import pandas as pd
API_URL = "https://mnp-details-gui.onrender.com"
# '''-------------------------------------------------------------'''

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

# '''-------------------------------------------------------------------------------------------------'''




def fetch_data(url):
    """Fetch data from the API and handle errors."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {str(e)}")
        return {}


def get_defect_by_multi_tab():
    st.title("🔍 Update Defects")
    defect_table = fetch_data(f"{API_URL}/all_defect/")
    df = pd.DataFrame(defect_table)


    # Status Selection
    select_status = st.selectbox("Choose Status:", ["Select Status", "Reported", "Closed"])
    # defect_table = fetch_data(f"{API_URL}/all_defect/")
    # df = pd.DataFrame(defect_table)

    eqpmnt_list = []
    if select_status != "Select Status":
        eqpmnt_list = df[df["defect_status"] == select_status]["equipment_id"].unique().tolist()

        # eqp_data = fetch_data(f"{API_URL}/equipment_list/{select_status}")
        # eqpmnt_list = [item["equipment_id"] for item in eqp_data.get("equipment_list", [])]

    select_eqp = st.selectbox("Choose Equipment:", ["Select Equipment"] + eqpmnt_list)

    part_list = []
    if select_eqp != "Select Equipment":
        part_list = df[(df["defect_status"] == select_status) & (df["equipment_id"] == select_eqp)]["part_id"].unique().tolist()
        # part_data = fetch_data(f"{API_URL}/part_list/{select_eqp}")
        # part_list = [item["part_id"] for item in part_data.get("part_list", [])]

    select_part = st.selectbox("Choose Part:", ["Select Part"] + part_list)

    report_list = []
    if select_part != "Select Part":
        report_list = df[(df["defect_status"] == select_status) & (df["equipment_id"] == select_eqp) & (df["part_id"] == select_part)][
            "part_id"].unique().tolist()
        # report_data = fetch_data(f"{API_URL}/distinct_defect/{select_part}")
        # report_list = [item["defect_description"] for item in report_data.get("distinct_defect", [])]

    select_report = st.selectbox("Choose Report:", ["Select Report"] + report_list)

    if select_report != "Select Report":
        # Defect Update Form
        with st.form("update_defect_form"):
            assigned_technician = st.text_input("Technician Name", value="NA")
            type_of_activity = st.text_input("Type of Activity", value="NA")
            remarks = st.text_area("Additional Remarks", value="NA")
            consumption = st.text_input("Consumables", value="NA")
            spare = st.text_input("Spare Part Used", value="NA")
            defect_status = st.selectbox("Defect Status:",
                                         ["Reported", "Closed", "Under Review", "Resolved", "Duplicate"])
            downtime_hours = st.number_input("Down Time (hrs)", value=0.0)
            resolution_date = st.date_input("Rectification Date", value=datetime.date.today())

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
                    "resolution_date": resolution_date.isoformat(),
                    "equipment_id": select_eqp,
                    "part_id": select_part,
                    "defect_description": select_report
                }

                try:
                    response = requests.post(f"{API_URL}/update_defect/", json=payload, timeout=10)
                    if response.status_code == 200:
                        st.success("✅ Defect updated successfully!")
                    else:
                        st.error(f"❌ Failed to update defect: {response.status_code} - {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Error updating defect: {str(e)}")


