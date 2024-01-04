import streamlit as st
import time
from datetime import time




def converter(value):
    m, s, mm = value.split(":")
    t_s = int(m)*60+int(s)+int(mm)/1000
    return t_s

val = st.time_input("Set Timer", value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("Please set a timer")
else:
    bar = st.progress(0)
    for i in range(10):
        bar.progress((i+1)*10)
        time.sleep(1)  

current_time = time.localtime()
seconds_left = 59 - current_time.tm_sec
minutes_left = 59 - current_time.tm_min
hours_left = 23 - current_time.tm_hour
total_seconds = seconds + minutes * 60 + hours * 3600 + days * 86400

