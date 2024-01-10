import streamlit as st
import time as ts
import pandas as pd
from datetime import time
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
import calendar
from datetime import date

today = date.today().day
currentYear = date.today().year
currentMonth = date.today().month
currentMonthName = calendar.month_name[currentMonth]

try:
    monthrange = calendar.monthrange(currentYear, currentMonth)[1]
    percentOfTheMonth = (today / monthrange) * 100
    percentOfTheMonth = '{:,.2f}'.format(percentOfTheMonth)
except:
    st.write("An error happened. Could not calculate the % of the month.")
else:
    st.write(str(percentOfTheMonth) + ' % of ' + currentMonthName + ' is completed.' + ' (As of ' + str(date.today()) + '.)')

with st.spinner('Wait for it...'):
    ts.sleep(5)
st.success('Done!')

my_html = """
<script>
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}

window.onload = function () {
    var fiveMinutes = 60 * 5,
        display = document.querySelector('#time');
    startTimer(fiveMinutes, display);
};
</script>

<body>
  <div>Registration closes in <span id="time">05:00</span> minutes!</div>
</body>
"""

html(my_html)

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

 
