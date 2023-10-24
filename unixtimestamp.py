import streamlit as st

# importing datetime module
import time
import datetime

def datetime2unixtime(input_year, input_month, input_day, input_hr, input_mi, input_sec):
    input_datetime = datetime.datetime(input_year, input_month, input_day, input_hr, input_mi, input_sec)
    return time.mktime(input_datetime.timetuple())

def unixtime2datetime(input_timestamp):
    output = datetime.datetime.fromtimestamp(input_timestamp)
    output.strftime('%Y-%m-%d %H:%M:%S')
    return output


st.title("Unix Timestamp Converter")
# creates a horizontal line
st.write("---")

## Current datetime and unix timestamp
# cur_datetime = datetime.datetime.now()
# cur_unixtime = time.mktime(cur_datetime.timetuple())

col1, col2 = st.columns(2)
with col1:
    st.header("Datetime -> Unix Timestamp")
    input_year = st.number_input(value=2000, label="Year")
    input_month = st.number_input(value=1, label="Month")
    input_day = st.number_input(value=1, label="Day")
    input_hr = st.number_input(value=0, label="Hour")
    input_mi = st.number_input(value=0, label="Minute")
    input_sec = st.number_input(value=0, label="Second")
    if st.button("Datetime -> Unix Timestamp"):
        output_unixtimestamp = datetime2unixtime(input_year, input_month, input_day, input_hr, input_mi, input_sec)
        st.success(f"Unix Timestamp: {output_unixtimestamp}")
with col2:
    st.header("Unix Timestamp -> Datetime")
    input_unixtimestamp = st.number_input(value=0, label="Enter Unix Timestamp")
    # input_unixtimestamp = st.text_input(label="Unix Timestamp")

    if st.button("Unix Timestamp -> Datetime"):
        output_datetime = unixtime2datetime(input_unixtimestamp)
        st.success(f"Datetime: {output_datetime}")

