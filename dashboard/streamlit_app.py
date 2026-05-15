import streamlit as st
from app.db import load_all
from app.plotter import plot

st.title("EB-3 China Tracker")

data = load_all()
st.write(data)

plot(data)
st.image("visa_trend.png")
