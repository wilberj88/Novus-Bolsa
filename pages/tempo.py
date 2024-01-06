import streamlit as st
import time as ts
import pandas as pd
from datetime import time
from d3blocks import D3Blocks


# Initialize
d3 = D3Blocks()


# Load example data
df = d3.import_example('random_time', n=10000, c=300, date_start="1-1-2000 00:10:05", date_stop="1-1-2000 23:59:59")


# Plot
d3.movingbubbles(df, speed={"slow": 1000, "medium": 200, "fast": 10}, filepath='movingbubbles.html')




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

 
