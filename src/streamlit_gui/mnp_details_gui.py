import requests
import streamlit as st
from datetime import datetime
API_URL = "https://mnp-details.onrender.com"

'''-----------------------'''

# def save_mnp_detail():
#     st.title("Save manpower detail")
#
#     name = st.text_input("Name")
#     age = st.text_input("Age")
#     mobile_no = st.text_input("Mobile No.")
#     address = st.text_input("Address")
#
#     if st.button("Add M/P Detail"):
#         response = requests.post(f"{API_URL}/mnp_detail/", json={
#                 "name":name,
#                 "age":age,
#                 "mobile_no":mobile_no,
#                 "address":address,
#         },
#             timeout=10  # Add a timeout for robustness
#         )
#
#             # Handle response
#         if response.status_code == 200:
#             st.success("Detail updated successfully!")
#         else:
#             st.error(f"Failed to update detail. Error: {response.status_code} - {response.text}")
#
# '''-----------------------------------------------------------------------------------'''
# def save_mmd_dpr_tab():
#     st.title("Save MMD DPR")
#
#     unit_no = st.text_input("Unit No.")
#     area = st.text_input("Area")
#     equipment = st.text_input("Equipment")
#     dept = st.text_input("Dept")
#     work_description = st.text_input("Work Description")
#     permit_no = st.text_area("Permit No")
#     mp_deployed = st.text_area("Manpower Deployed")
#     job_start = st.date_input("Work Start Date/Time", datetime.now())
#     job_stop = st.date_input("Work Completion Date", datetime.now())
#     spares = st.text_area("Spares Part")
#     consumables = st.text_area("Consumables")
#     status = st.selectbox("Status of Work", ["Open", "In Progress", "Closed"])
#     if st.button("Add DPR"):
#         response = requests.post(f"{API_URL}/mmd_dpr/", json={
#                 "unit_no":unit_no,
#                 "area":area,
#                 "equipment":equipment,
#                 "dept":dept,
#                 "work_description":work_description,
#                 "permit_no":permit_no,
#                 "mp_deployed":mp_deployed,
#                 "job_start":job_start.isoformat(),
#                 "job_stop":job_stop.isoformat(),
#                 "spares":spares,
#                 "consumables":consumables,
#                 "status":status},
#             timeout=10  # Add a timeout for robustness
#         )
#
#             # Handle response
#         if response.status_code == 200:
#             st.success("Expenses updated successfully!")
#         else:
#             st.error(f"Failed to update expenses. Error: {response.status_code} - {response.text}")
#

def save_mnp_detail():
    st.title("Save Manpower Detail")

    name = st.text_input("Name")
    age = st.text_input("Age")
    mobile_no = st.text_input("Mobile No.")
    address = st.text_input("Address")

    if st.button("Add M/P Detail"):
        response = requests.post(f"{API_URL}/mnp_detail/", json={
            "name": name,
            "age": age,
            "mobile_no": mobile_no,
            "address": address,
        },
        timeout=10  # Timeout for robustness
        )

        # Handle response
        if response.status_code == 200:
            st.success("Detail updated successfully!")
        else:
            st.error(f"Failed to update detail. Error: {response.status_code} - {response.text}")

'''-----------------------------------------------------------------------------------'''

def save_mmd_dpr_tab():
    st.title("Save MMD DPR")

    unit_no = st.text_input("Unit No.")
    area = st.text_input("Area")
    equipment = st.text_input("Equipment")
    dept = st.text_input("Dept")
    work_description = st.text_area("Work Description")
    permit_no = st.text_area("Permit No")
    mp_deployed = st.text_area("Manpower Deployed")

    # Proper date handling
    job_start_date = st.date_input("Work Start Date", datetime.today().date())
    job_start_time = st.time_input("Work Start Time", datetime.now().time())
    job_start = datetime.combine(job_start_date, job_start_time)  # Merge date & time

    job_stop_date = st.date_input("Work Completion Date", datetime.today().date())
    job_stop_time = st.time_input("Work Completion Time", datetime.now().time())
    job_stop = datetime.combine(job_stop_date, job_stop_time)  # Merge date & time

    spares = st.text_area("Spares Part")
    consumables = st.text_area("Consumables")
    status = st.selectbox("Status of Work", ["Open", "In Progress", "Closed"])

    if st.button("Add DPR"):
        response = requests.post(f"{API_URL}/mmd_dpr/", json={
            "unit_no": unit_no,
            "area": area,
            "equipment": equipment,
            "dept": dept,
            "work_description": work_description,
            "permit_no": permit_no,
            "mp_deployed": mp_deployed,
            "job_start": job_start.isoformat(),
            "job_stop": job_stop.isoformat(),
            "spares": spares,
            "consumables": consumables,
            "status": status
        },
        timeout=10  # Timeout for robustness
        )

        # Handle response
        if response.status_code == 200:
            st.success("DPR updated successfully!")  # Fixed incorrect message
        else:
            st.error(f"Failed to update DPR. Error: {response.status_code} - {response.text}")
'''-----------------------------------------------------------------------------------------------------'''