import streamlit as st
from mnp_details_gui import save_mnp_detail, save_mmd_dpr_tab, fetch_equp_histry_tab
from defect_report_gui import report_defect

# App Title
st.title("🛠 ONMOT Reporting System")

# User role selection using expander
with st.expander("Select Your Role:"):
    user_role = st.selectbox("Choose Role:", ["Planner", "Worker"])

# Create tabs based on role
tabs = {}

if user_role == "Planner":
    tabs["👷 Manpower Detail"] = save_mnp_detail
    tabs["⚙️ Equipment History"] = fetch_equp_histry_tab
elif user_role == "Worker":
    tabs["📋 DPR Update"] = save_mmd_dpr_tab
    tabs["Report Defect"] = report_defect

# Render tabs dynamically
# if tabs:
#     selected_tab = st.selectbox("Select Tab:", list(tabs.keys()))
#     tabs[selected_tab]()
#
# # Render tabs dynamically
# if tabs:
#     selected_tab = st.radio("Select Tab:", list(tabs.keys()))
#     tabs[selected_tab]()
# import streamlit as st
# from mnp_details_gui import save_mnp_detail, save_mmd_dpr_tab, fetch_equp_histry_tab
# from defect_report_gui import report_defect
#
# # Define users (You can replace this with a proper authentication system)
# USER_CREDENTIALS = {
#     "admin": "12345",
#     "operator": "onmot2025"
# }
#
# # Initialize session state for authentication
# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False
#
# # Authentication Logic
# def login():
#     """Authenticate user login."""
#     st.title("🔒 Login to ONMOT Reporting")
#     username = st.text_input("Username", key="user")
#     password = st.text_input("Password", type="password", key="pass")
#
#     if st.button("Login"):
#         if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
#             st.session_state.authenticated = True
#             st.session_state.username = username  # Store username in session
#             st.success(f"✅ Welcome, {username}!")
#             st.rerun()
#         else:
#             st.error("❌ Invalid Username or Password")
#
# # Logout Function
# def logout():
#     """Logs out the user by resetting authentication state."""
#     st.session_state.authenticated = False
#     st.session_state.username = None
#     st.rerun()
#
# # If not authenticated, show login screen
# if not st.session_state.authenticated:
#     login()
# else:
#     # Display Logout Button
#     st.sidebar.button("🚪 Logout", on_click=logout)
#
#     # App Title
#     st.title("🛠 ONMOT Reporting System")
#
#     # Create tabs for different functionalities
#     tab1, tab2, tab3, tab4 = st.tabs(["👷 Manpower Detail", "📋 DPR Update", "⚙️ Equipment History", "Report Defect"])
#
#     # Use the first tab (index 0) with a context manager
#     with tab1:
#         save_mnp_detail()
#     with tab2:
#         save_mmd_dpr_tab()
#     with tab3:
#         fetch_equp_histry_tab()
#     with tab4:
#         report_defect()

# python -m streamlit run src/streamlit_gui/app.py