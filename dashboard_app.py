import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Dashboard Mockup")

st.write("This is a mockup dashboard for data visualization.")

# Example metric
st.metric("Sample Metric", "123", "+10")

# Example chart
data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
st.line_chart(data)
