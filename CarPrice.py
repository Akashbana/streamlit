import datetime
import streamlit as st # type: ignore
import pandas as pd # type: ignore
import pickle 

cars_df = pd.read_csv("./cars24.csv")

st.header("Cars24 price prediction")

st.dataframe(cars_df.head())

fuel_type = st.selectbox("Fuel type",("Diesel","Petrol"))

transmission_type = st.selectbox("Transmission type",("Automatic","Manual"))  

encode_dict = {"fuel_type":{"Diesel":1,"Petrol":2},
               "transmission_type":{"Automatic":2,"Manual":1} 
               } 

st.bar_chart(cars_df, x = 'fuel_type', y='mileage') 




