import streamlit as st
import time
from datetime import time

current_time = time.localtime()
seconds_left = 59 - current_time.tm_sec
minutes_left = 59 - current_time.tm_min
hours_left = 23 - current_time.tm_hour
total_seconds = seconds + minutes * 60 + hours * 3600 + days * 86400

bar = st.progress(0)
for i in range(total_seconds):
    bar.progress((i+1)*10)
    time.sleep(1)  
