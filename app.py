import streamlit as st
import pandas as pd
import plotly.express as px

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
car_data = pd.read_csv(
    '/Users/david/Documents/GitHub/project_sprint7/vehicles_us.csv')


st.header('Datos sobre venta de automoviles')

hist_button = st.checkbox('Construir histograma')

if hist_button:
    st.write(
        'Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.checkbox('Construir grafico de dispersion')

if scatter_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncions de venta de coches.')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
