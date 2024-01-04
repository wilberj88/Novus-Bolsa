import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import pandas as pd
import time

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

api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjU4MGJkMDkxNDBjZmQ3MjNkMTQyNDFhIiwiaWF0IjoxNzA0MjQ3MzU0LCJleHAiOjMzMjA4NzExMzU0fQ.M2HQZCbxV3-lGmg8Hh6lKFfWVs53DMP88hbSLqKM17o'
url = f'https://api.taapi.io/candles?secret={api_key}&exchange=binance&symbol=BTC/USDT&interval=1d&period=365'
hist_json = requests.get(url).json()
#hist_df = pd.DataFrame(hist_json).drop('timestampHuman', axis = 1).rename(columns = {'timestamp':'time'})
#hist_df.time = pd.to_datetime(hist_df.time, unit = 's')
#hist_df.tail()

title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1,0.2,1,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Crypto<br>Dashboard</p>', unsafe_allow_html = True)

with btc_col:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">BTC / USDT<br></p><p class="price_details">34060.92</p>', unsafe_allow_html = True)
       
with eth_col:
    with st.container(border=True):
        #eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">ETH / USDT<br></p><p class="price_details">1789.26</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container(border=True):
        #xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">XMR / USDT<br></p><p class="price_details">162.1</p>', unsafe_allow_html = True)

with sol_col:
    with st.container(border=True):
        #sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">SOL / USDT<br></p><p class="price_details">32.27</p>', unsafe_allow_html = True)

with xrp_col:
    with st.container(border=True):
        #xrp_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XRP/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xrp_text">XRP / USDT<br></p><p class="price_details">0.5449</p>', unsafe_allow_html = True)


params_col, chart_col, data_col = st.columns([0.7,1.6,1.1])

with params_col:
    
    with st.form(key = 'params_form'):
        
        st.markdown(f'<p class="params_text">CHART DATA PARAMETERS', unsafe_allow_html = True)
        
        st.divider()
        
        exchanges = ['binance', 'bitstamp', 'binancefutures', 'whitebit', 'bybit', 'gatetio', 'coinbase', 'binanceus', 'kraken']
        exchange = st.selectbox('Exchange', exchanges, key = 'exchange_selectbox')
        
        if st.session_state.symbols_list == None:
            symbols = []
            for i in exchanges:
                symbols_list = requests.get(f'https://api.taapi.io/exchange-symbols?secret={api_key}&exchange={i}').json()
                symbols.extend(symbols_list)
            symbol = st.selectbox('Symbol', symbols, key = 'symbol_selectbox')
            st.session_state.symbols_list = symbols
        else:
            symbol = st.selectbox('Symbol', st.session_state.symbols_list, key = 'symbol_selectbox')
        
        interval_col, period_col = st.columns(2)
        with interval_col:
            interval = st.selectbox('Interval', ['1m', '5m', '15m', '30m', '1h', '2h', '4h', '12h', '1d'], key = 'interval_selectbox')
        with period_col:
            period = st.number_input('Period', min_value = 10, max_value = 500, value = 365, step = 1, key = 'period_no_input')
        
        st.markdown('')
        update_chart = st.form_submit_button('Update chart')
        st.markdown('')
        
        if update_chart:
           

            with chart_col:

                with st.container(border=True):        
                    bar = st.progress(0)
                    for i in range(10):
                        bar.progress((i+1)*10)
                        time.sleep(1)             
                    def render_basic_radar():
                        option = {
                                "title": {"text": "Costos estimados por tipos de Riesgos Climáticos"},
                                "legend": {"data": ["Riesgo Detectado", "Riesgo Gestionado"]},
                                "radar": {
                                    "indicator": [
                                        {"name": "Derrumbes", "max": 6500},
                                        {"name": "Sequías", "max": 16000},
                                        {"name": "Incendios", "max": 30000},
                                        {"name": "Inundaciones", "max": 38000},
                                        {"name": "Deslizamientos", "max": 52000},
                                        {"name": "Contaminación", "max": 25000},
                                    ]
                                },
                                "series": [
                                    {
                                        "name": "Costo Estimado Vs Costo Mitigado",
                                        "type": "radar",
                                        "data": [
                                            {
                                                "value": [2000, 10000, 20000, 3500, 15000, 11800],
                                                "name": "Riesgo Detectado",
                                            },
                                            {
                                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                                "name": "Riesgo Gestionado",
                                            },
                                        ],
                                    }
                                ],
                            }
                        st_echarts(option, height="500px")
                    render_basic_radar()
                    
            with data_col:
                df = pd.DataFrame(
                    {
                        "name": ["Roadmap", "Extras", "Issues"],
                        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                        "stars": [random.randint(0, 1000) for _ in range(3)],
                        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                    }
                )
                st.dataframe(
                    df,
                    column_config={
                        "name": "App name",
                        "stars": st.column_config.NumberColumn(
                            "Github Stars",
                            help="Number of stars on GitHub",
                            format="%d ⭐",
                        ),
                        "url": st.column_config.LinkColumn("App URL"),
                        "views_history": st.column_config.LineChartColumn(
                            "Views (past 30 days)", y_min=0, y_max=5000
                        ),
                    },
                    hide_index=True,
                )
                st.caption("By Wilber Jimenez Hernandez")
                
               

                                  


