import streamlit as st
import time as ts
import pandas as pd
from datetime import time




def converter(value):
    m, s, mm = value.split(":")
    t_s = int(m)*60+int(s)+int(mm)/1000
    return t_s

val = st.time_input("Set Timer", value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("Please set a timer")
else:
    sec = converter(str(val))
    bar = st.progress(0)
    per = sec/100
    for i in range(100):
        bar.progress((i+1))
        st.write(str(i)+" %")
        ts.sleep(per)  

def run_progress_bar(seconds, minutes, hours, days):
    total_seconds = seconds + minutes * 60 + hours * 3600 + days * 86400

    progress_bar = st.progress(0)

    for i in range(total_seconds + 1):
        time.sleep(1)
        progress_bar.progress(int(i * 100 / total_seconds))

    st.success("¡Proceso completado!")

st.title("Barra de Progreso con Streamlit")

current_time = ts.localtime()
seconds_left = 59 - current_time.tm_sec
minutes_left = 59 - current_time.tm_min
hours_left = 23 - current_time.tm_hour
days_left = 0
