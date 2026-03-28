import streamlit as st
import pandas as pd

from scheduler.johnson import johnsons_rule
from scheduler.timing import calculate_times
from scheduler.gantt import plot_gantt

st.markdown("###  Model Assumptions")
st.write("""
- All patients follow Test → Scan sequence  
- No emergency cases considered  
- Processing times are known and fixed  
- Only one test unit and one scan unit  
""")
st.title(" Patient Scheduling (Test → Scan)")

if "data" not in st.session_state:
    st.session_state.data = []

# Input
name = st.text_input("Patient Name")
test_time = st.number_input("Test Time", min_value=1)
scan_time = st.number_input("Scan Time", min_value=1)

if st.button("Add Patient"):
    if name:
        st.session_state.data.append({
            "name": name,
            "test": test_time,
            "scan": scan_time
        })
if st.button("Load Demo Case"):
    st.session_state.data = [
        {'name': 'P1', 'test': 2, 'scan': 6},
        {'name': 'P2', 'test': 5, 'scan': 1},
        {'name': 'P3', 'test': 4, 'scan': 3},
    ]
    st.success("Demo data loaded!")
# Display Data
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)

    if st.button("Clear All Patients"):
        st.session_state.data = []
        st.success("All data cleared!")

# Sample Data
if st.button("Use Sample Data"):
    st.session_state.data = [
        {'name': 'P1', 'test': 3, 'scan': 8},
        {'name': 'P2', 'test': 6, 'scan': 2},
        {'name': 'P3', 'test': 4, 'scan': 7},
        {'name': 'P4', 'test': 5, 'scan': 3},
    ]

# Optimize
if st.button("Optimize"):

    if len(st.session_state.data) < 2:
        st.warning("Add at least 2 patients to optimize")
    else:
        sequence = johnsons_rule(st.session_state.data)
        result, makespan, idle = calculate_times(sequence)
    
    st.subheader("Optimal Sequence")
    st.write(" → ".join([job['name'] for job in sequence]))

    col1, col2 = st.columns(2)
    col1.metric("Elapsed Time", makespan)
    col2.metric("Idle Time (Scan)", idle)

    st.dataframe(pd.DataFrame(result))

    plot_gantt(result)

    # existing outputs...

    # 👉 ADD HERE (end of block)
    import json
    st.download_button(
        label="Download Schedule",
        data=json.dumps(result, indent=4),
        file_name="schedule.json",
        mime="application/json"
    )

st.markdown("###  Interpretation")
st.write("""
- The sequence minimizes total completion time (makespan)
- Idle time indicates unused scan capacity
- Lower idle time → better system efficiency
""")

st.markdown("---")
st.caption("Operations Research Project | Healthcare Optimization System")