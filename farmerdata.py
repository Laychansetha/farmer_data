import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

st.title("Summary Farmer Data")

col1, col2, col3 = st.columns(3)
col1.metric(label="Gain", value=5000, delta=1000)
col2.metric(label="Loss", value=5000, delta=-1000)
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
