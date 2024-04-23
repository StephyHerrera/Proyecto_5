import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Condición de los Vehículos')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir scatter') 
 

if hist_button: # al hacer clic en el botón
 # escribir un mensaje
 st.write('Creación de un scatter para el conjunto de datos de anuncios de venta de coches')
            
   # crear un histograma
fig = px.scatter(car_data, x="odometer", y="price")
st.plotly_chart(fig, use_container_width=True)
        