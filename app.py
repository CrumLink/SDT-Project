import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Vehicle Data Analysis App')

# Introduction section
st.markdown("""
## Purpose of This Report
This interactive web application provides a comprehensive analysis of used vehicle data. Our goal is to offer insights into various aspects of the used car market, including pricing trends, vehicle conditions, and feature distributions. Whether you're a potential buyer, a car enthusiast, or a data analyst, this report will equip you with valuable information derived from over 50,000 vehicle listings.

## How to Navigate the App
- Explore a variety of visualizations that highlight key aspects of the data.
- Use interactive elements to filter and delve deeper into specific areas of interest.
- Each section of the app is designed to provide focused insights on different attributes like price, model year, fuel type, and more.

We hope this application empowers you with the knowledge to make informed decisions or satisfies your curiosity about the used vehicle market.

Thank you for visiting, and we welcome your feedback to continuously improve this experience.
""")


df = pd.read_csv('vehicles_us.csv')

st.header('Data Visualization App')

if st.checkbox('Show Raw Data'):
    st.write(df)
    
#Histogram   
st.subheader('Histogram')
column_to_plot = st.selectbox('Choose a column for histogram:', df.columns)
histogram = px.histogram(df, x=column_to_plot)
st.plotly_chart(histogram) 

#Scatter Plot
st.subheader('Scatter Plot')
x_axis = st.selectbox('Choose X-axis:', df.columns)
y_axis = st.selectbox('Choose Y-axis:', df.columns)
scatter_plot = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(scatter_plot)