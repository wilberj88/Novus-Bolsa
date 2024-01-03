import streamlit as st
import requests
import pandas as pd
from lightweight_charts.widgets import StreamlitChart

if "symbols_list" not in st.session_state:
    st.session_state.symbols_list = None
    
st.set_page_config(
    layout = 'wide',
    page_title = 'Crypto Dashboard'
)

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
    </style>
    """, unsafe_allow_html = True
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

api_key = 'YOUR TAAPI.IO API KEY'
        
title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1,0.2,1,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Crypto<br>Dashboard</p>', unsafe_allow_html = True)

with btc_col:
    with st.container():
        btc_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=BTC/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="btc_text">BTC / USDT<br></p><p class="price_details">{btc_price}</p>', unsafe_allow_html = True)

with eth_col:
    with st.container():
        eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">ETH / USDT<br></p><p class="price_details">{eth_price}</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container():
        xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">XMR / USDT<br></p><p class="price_details">{xmr_price}</p>', unsafe_allow_html = True)

with sol_col:
    with st.container():
        sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">SOL / USDT<br></p><p class="price_details">{sol_price}</p>', unsafe_allow_html = True)

with xrp_col:
    with st.container():
        xrp_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XRP/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xrp_text">XRP / USDT<br></p><p class="price_details">{xrp_price}</p>', unsafe_allow_html = True)
