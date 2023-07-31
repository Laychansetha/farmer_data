import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
from streamlit_extras.colored_header import colored_header

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Summary ICS")

# To update farmer data from Siem Pang
last_day = 215
complete_ics = 312
nc_farmers = 7
increase = complete_ics - last_day
remain = 1089 - complete_ics

colored_header(
    label="Siem Pang",
    description="Note: In Siem Pang totally we have 1089 farmers new and existing",
    color_name="violet-70",
)
col1, col2, col3 = st.columns(3)
col1.metric(label="Completed ICS", value=complete_ics, delta=increase)
col2.metric(label="Total Farmers", value=1089, delta=-nc_farmers)
col3.metric(label="Remain Farmers", value=remain, delta=complete_ics)
style_metric_cards()


# To update farmer data from Lumphat
lp_last_day = 4
lp_complete_ics = 5
lp_nc_farmers = 0
lp_increase = lp_complete_ics - lp_last_day
lp_remain = 215 - lp_complete_ics

colored_header(
    label="Lumphat",
    description="Note: In Lumphat totally we have 215 farmers new and existing",
    color_name="red-70",
)
col1, col2, col3 = st.columns(3)
col1.metric(label="Completed ICS", value=lp_complete_ics, delta=lp_increase)
col2.metric(label="Total Farmers", value=215, delta=-lp_nc_farmers)
col3.metric(label="Remain Farmers", value=lp_remain, delta=lp_complete_ics)
style_metric_cards()