import streamlit as st
import pandas as pd
import plotly.express as px

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