import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header('my histogram')
st.write('some random text')
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
