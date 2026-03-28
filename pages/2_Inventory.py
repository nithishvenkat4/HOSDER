import streamlit as st
from scheduler.inventory import calculate_eoq


st.markdown("###  EOQ Explanation")
st.write("""
EOQ determines the optimal order quantity that minimizes:
- Ordering cost
- Holding cost

This helps hospitals manage medical supplies efficiently.
""")
st.title("Inventory Optimization (EOQ)")

st.write("Optimize medical supply ordering")

demand = st.number_input("Annual Demand (D)", min_value=1)
ordering_cost = st.number_input("Ordering Cost (S)", min_value=1)
holding_cost = st.number_input("Holding Cost (H)", min_value=1)

if st.button("Calculate EOQ"):
    eoq, total_cost = calculate_eoq(demand, ordering_cost, holding_cost)

    col1, col2 = st.columns(2)
    col1.metric("EOQ", eoq)
    col2.metric("Total Cost", total_cost)

    st.markdown("###  Interpretation")
st.write("""
- EOQ minimizes total inventory cost
- Helps avoid overstocking and shortages
""")

st.markdown("---")
st.caption("Operations Research Project | Healthcare Optimization System")