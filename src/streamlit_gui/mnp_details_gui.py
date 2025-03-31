import requests
import streamlit as st
API_URL = "http://127.0.0.1:8080"

'''-----------------------'''

def save_mnp_detail():
    st.title("Save manpower detail")

    name = st.text_input("Name")
    age = st.text_input("Age")
    mobile_no = st.text_input("Mobile No.")
    address = st.text_input("Address")

    if st.button("Submit"):
        response = requests.post(f"{API_URL}/mnp_detail/", json={
                "name":name,
                "age":age,
                "mobile_no":mobile_no,
                "address":address,
        },
            timeout=10  # Add a timeout for robustness
        )

            # Handle response
        if response.status_code == 200:
            st.success("Detail updated successfully!")
        else:
            st.error(f"Failed to update detail. Error: {response.status_code} - {response.text}")