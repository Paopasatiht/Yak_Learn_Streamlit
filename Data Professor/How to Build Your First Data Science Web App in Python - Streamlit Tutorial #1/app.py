import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
# Simple Stock Price App

Shown are the stock closing price and volume for Apple, Google, and Microsoft.         

''')

# define ticker symbol
tickerSymbol =  'AAPL'
# get data from ticker
tickerData = yf.Ticker(tickerSymbol)
# get history price
tickerDf = tickerData.history(period='1d', start='2020-01-01', end='2020-04-01')
# Open High Low Close Volume Dividends Stock Splits

st.write("""
## Close Price         
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price         
""")
st.line_chart(tickerDf.Volume)