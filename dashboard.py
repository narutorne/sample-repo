import os
from datetime import datetime, timedelta

import pandas_datareader.data as web
import requests
import streamlit as st
import yfinance as yf

st.title("S&P 500 Dashboard")

# Fetch S&P 500 data
start = datetime.today() - timedelta(days=365)
end = datetime.today()
sp500 = yf.Ticker("^GSPC")
data = sp500.history(start=start, end=end)
st.subheader("S&P 500 Price")
st.line_chart(data['Close'])

# Economic indicators
indicator_symbols = {
    "Consumer Price Index": "CPIAUCSL",
    "Unemployment Rate": "UNRATE",
}
for name, symbol in indicator_symbols.items():
    try:
        indicator = web.DataReader(symbol, "fred", start)
        st.subheader(name)
        st.line_chart(indicator)
    except Exception as e:
        st.warning(f"Failed to load {name}: {e}")

# News section
api_key = os.getenv("NEWSAPI_KEY")
if api_key:
    params = {
        "q": "S&P 500",
        "apiKey": api_key,
        "language": "en",
        "pageSize": 5,
    }
    response = requests.get("https://newsapi.org/v2/everything", params=params, timeout=10)
    if response.ok:
        articles = response.json().get("articles", [])
        st.subheader("Latest News")
        for article in articles:
            st.markdown(f"**[{article['title']}]({article['url']})**")
            st.write(article.get("description", ""))
    else:
        st.warning("Failed to load news")
else:
    st.info("Set NEWSAPI_KEY environment variable to display news.")
