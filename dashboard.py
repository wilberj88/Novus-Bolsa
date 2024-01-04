import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import pandas as pd
import time
from datetime import time

if "symbols_list" not in st.session_state:
    st.session_state.symbols_list = None
    
st.set_page_config(
    layout = 'wide',
    page_title = 'Mis Finanzas 2024'
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


title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1.3,0.2,1,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Mis Finanzas 2024<br>Dashboard</p>', unsafe_allow_html = True)

with btc_col:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Ingresos<br></p><p class="price_details">34060.92</p>', unsafe_allow_html = True)
       
with eth_col:
    with st.container(border=True):
        #eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">Gastos<br></p><p class="price_details">1789.26</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container(border=True):
        #xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">Inversiones<br></p><p class="price_details">162.1</p>', unsafe_allow_html = True)

with sol_col:
    with st.container(border=True):
        #sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">Ahorros<br></p><p class="price_details">32.27</p>', unsafe_allow_html = True)

with xrp_col:
    with st.container(border=True):
        #xrp_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XRP/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xrp_text">Deudas<br></p><p class="price_details">0.5449</p>', unsafe_allow_html = True)


params_col, chart_col, data_col = st.columns([0.7,1.6,1.1])

with params_col:
    
    with st.form(key = 'params_form'):
        
        st.markdown(f'<p class="params_text">PARÁMETROS', unsafe_allow_html = True)
                
        listado_modos = ['Conservador', 'Precavido', 'Arriesgado']
        modo = st.selectbox('Selecciona un modo financiero', listado_modos, key = 'modo')

        listado_edad_retiro = ['50 años','55 años','60 años','65 años','70 años']
        retiro = st.selectbox('¿A qué edad deseas pensionarte?', listado_edad_retiro, key = 'retiro')
        
        interval_col, period_col = st.columns(2)
        with interval_col:
            interval = st.selectbox('Interval', ['1m', '5m', '15m', '30m', '1h', '2h', '4h', '12h', '1d'], key = 'interval_selectbox')
        with period_col:
            period = st.number_input('Period', min_value = 10, max_value = 500, value = 365, step = 1, key = 'period_no_input')
        st.divider()
        st.markdown('')
        update_chart = st.form_submit_button('Update chart')
        st.markdown('')
        
        if update_chart:
           

            with chart_col:

                with st.container(border=True):
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
                
               

                                  


