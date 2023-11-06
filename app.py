
# Streamlit app that allows users to find the best multi-stop travel options

import streamlit as st
import pandas as pd
import numpy as np
import requests


# basic page setup
st.set_page_config(
    page_title="Travel",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set up simple password protection
password = st.text_input("Password", type="password")
if password != "trav3l-gahrb":
    st.stop()

from travel.adapters.adapters import get_all_airports

all_airports = get_all_airports()

# sidebar
st.sidebar.markdown(
    "This app uses the [Kiwi](https://docs.kiwi.com/) API to find the best multi-stop travel options."
)
st.sidebar.markdown(
    "Enter your origin, destination and the available time span, and the app will find the best multi-stop travel options."
)
st.sidebar.text_input("Origin", key="origin")
st.sidebar.text_input("Destination", key="destination")
st.sidebar.date_input("Earliest departure date", key="departure_date")
st.sidebar.date_input("Latest return date", key="return_date")

# main page
st.title("Travel")
st.subheader("Find the best multi-stop travel options")

# build the travel decision-tree based on the user inputs
