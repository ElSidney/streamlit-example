from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests


# Make a request to the OKEx API to get the latest price of a token future
def get_price(symbol):
    url = f"https://www.okex.com/api/v5/instruments?instType=SPOT&instId=ETH-USD"
    response = requests.get(url)
    data = response.json()
    return data

# Use Streamlit to create a simple app to display the price
st.title("OKEx Token Future Price")
symbol = st.text_input("Enter the symbol for the token future")
price = get_price(symbol)
st.write("The latest price of the token future is:", price, "USD")

