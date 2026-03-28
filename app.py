import streamlit as st

st.set_page_config(page_title="Healthcare OR System", layout="centered")

st.title(" Healthcare Operations Optimization System")

st.markdown("""
###  Modules Available:
-  Patient Scheduling (Johnson’s Rule)
-  Inventory Optimization (EOQ)

Use the sidebar to navigate between modules.
""")

st.success("Developed using Operations Research techniques")