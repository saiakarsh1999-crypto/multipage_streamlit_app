import time
import numpy as np
import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.empty()

# Initialize with initial random walk seed
data = np.random.randn(1, 1)
chart.line_chart(data)

for i in range(1, 51):
    new_rows = data[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    data = np.concatenate([data, new_rows])
    chart.line_chart(data)
    progress = i * 2
    status_text.text(f"{progress}% Complete")
    progress_bar.progress(progress)
    time.sleep(0.04)

progress_bar.empty()

st.button("Re-run")
