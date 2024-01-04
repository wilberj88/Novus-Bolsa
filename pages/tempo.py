import streamlit as st
import time as ts
import pandas as pd
from datetime import time


st.title('General Timer')

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
hora = "00:01:00"
sec = converter(str(hora))
bar = st.progress(0)
per = sec/100
progress_status = st.empty()
for i in range(100):
    bar.progress((i+1))
    progress_status.write(str(i+1)+" %")
    ts.sleep(per) 

st.title('1 minute Timer')
hora = "01:00:00"
sec = converter(str(hora))
bar = st.progress(0)
per = sec/100
progress_status = st.empty()
for i in range(100):
    bar.progress((i+1))
    progress_status.write(str(i+1)+" %")
    ts.sleep(per)  


st.title('1 hour Timer')
hora = "59:59:99"
sec = converter(str(hora))
bar = st.progress(0)
per = sec/100
progress_status = st.empty()
for i in range(100):
    bar.progress((i+1))
    progress_status.write(str(i+1)+" %")
    ts.sleep(per)  

 
