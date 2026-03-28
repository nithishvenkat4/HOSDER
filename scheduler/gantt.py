import matplotlib.pyplot as plt
import streamlit as st

def plot_gantt(result):
    fig, ax = plt.subplots()

    for i, r in enumerate(result):
        ax.barh("Test", r['test_end'] - r['test_start'], left=r['test_start'])
        ax.barh("Scan", r['scan_end'] - r['scan_start'], left=r['scan_start'])

        ax.text(r['test_start'], 0, r['patient'])
        ax.text(r['scan_start'], 1, r['patient'])

    ax.set_xlabel("Time")
    ax.set_title("Gantt Chart - Patient Scheduling")

    st.pyplot(fig)