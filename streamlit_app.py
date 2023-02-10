from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def get_price(symbol):
    url = f"https://api.coinex.com/v1/market/future/ticker?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return data["last"]

import requests
import streamlit as st

# Make a request to the CoinEx API to get the latest price of a token future
def get_price(symbol):
    url = f"https://api.coinex.com/v1/market/future/ticker?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return data["last"]

# Use Streamlit to create a simple app to display the price
st.title("CoinEx Token Future Price")
symbol = st.text_input("Enter the symbol for the token future")
price = get_price(symbol)
st.write("The latest price of the token future is:", price, "USD")
