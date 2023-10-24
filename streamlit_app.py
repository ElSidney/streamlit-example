from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests


# Make a request to the OKEx API to get the latest price of a token future
def get_price(symbol):
    url = f"GET /api/v5/public/funding-rate?instId=BTC-USD-SWAP"
    response = requests.get(url)
    data = response.json()
    return data



