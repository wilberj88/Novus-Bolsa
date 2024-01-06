import streamlit as st
import time as ts
import pandas as pd
from datetime import time
import time
from streamlit_lottie import st_lottie


st.title('General Timer')
with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")


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
    progress_status = st.empty()
    for i in range(100):
        bar.progress((i+1))
        progress_status.write(str(i+1)+" %")
        ts.sleep(per)  


st.title('1 second Timer')
segundo = "00:01:00"
sec = converter(str(segundo))
bar_segundo = st.progress(0)
per = sec/100
progress_status = st.empty()
for i in range(100):
    bar_segundo.progress((i+1))
    progress_status.write(str(i+1)+" %")
    ts.sleep(per) 

st.title('1 minute Timer')
minuto = "01:00:00"
sec = converter(str(minuto))
bar_minuto = st.progress(0)
per = sec/100
progress_status = st.empty()
for i in range(100):
    bar_minuto.progress((i+1))
    progress_status.write(str(i+1)+" %")
    ts.sleep(per)  


st.title('1 hour Timer')
hora = "59:59:99"
sec = converter(str(hora))
bar_hora = st.progress(0)
per = sec/100
progress_status = st.empty()
for i in range(100):
    bar_hora.progress((i+1))
    progress_status.write(str(i+1)+" %")
    ts.sleep(per)  

 
