import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

# procedemos a crear el encabezado

st.header('Aplicación Web')

# Creamos un botón para hcer clic y que construya un histograma

hist_button = st.button('Construir Histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncion de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar run gráfico oPlotly interactivo
    st.ploltly_chart(fig, use_container_width=True)

dis_button = st.button('Crear gráfico de dispersión')

if dis_button:
    st.write('Creación de grafico de dispersión para el conjunto de datos de anuncion de venta de coches')

    fig_dis = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig_dis, use_container_width=True)
