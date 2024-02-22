#---------------#
# 	Libraries
#---------------#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st
from datetime import date
from PIL import Image
from dataprep import  split_cols,ext_fecha

st.set_option('deprecation.showPyplotGlobalUse', False)
#function to read data

def load_data():
	data = pd.read_csv("C:\\Users\\User\\OneDrive\\Documentos\\Cursos de ML\\Data Science 4B\\Netflix\\NetflixViewingHistory.csv", parse_dates=['Date'])
	return data 

#SETEO DE PAGINA
st.set_page_config(layout="wide")
#st.markdown(f'<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)

imagen = Image.open("C:\\Users\\User\\OneDrive\\Documentos\\Cursos de ML\\Data Science 4B\\Netflix\\new logo.png")
st.image(imagen,use_column_width=True)
#st.title('NETFLIX DASHBOARD')

# READ DATASET
data = load_data()

##Split data
data = split_cols(data)
df = ext_fecha(data)

#st.write(df.head())

#-----------------#
# KPIS
#-----------------#
# crear variable de fecha el dia de hoy
hoy = pd.Timestamp(date.today())
#Buscar el primer dia de fecha de inicio
primer_dia = df['Date'].min()
#Calcular el tiempo
tiempo = (hoy - primer_dia).days

#calulo gasto 
costo_mensual = 6.99
conversion = 6.99 * 58.61 
gasto = tiempo/30 * costo_mensual
en_pesos = tiempo/30 * conversion

#calcular al año
serie = 45
pelicula = 100
consumo = df['tipo'].value_counts()
#Calculo del consumo
min_peli = consumo['pelicula'] * pelicula
#calcular el minuto por seires
min_serie = consumo['serie'] * serie

peli_ano = min_peli /60/24
serie_ano = min_serie /60/24

col1,col2,col3, col4 = st.columns(4)

with col1:
	st.metric(label="Tiempo Utilizando", value=str(tiempo) +' '+'días')

with col2:

	st.metric(label="Gatos Al Año en $", value= round(en_pesos))

with col3:
	st.metric(label="Al Año dedicas a ver series", value=str(round(serie_ano)) +' '+'días')

with col4:
	st.metric(label="Al Año dedicas a ver Peliculas", value=str(round(peli_ano)) +' '+'días')


#Dias de las semana
tab0,tab1, tab2, tab3,tab4 = st.tabs(['las 10 Peliculas mas Vistas','Las 10 Seies Mas Vistas',"Día Mayor Consumo", 'meses de mayor consumo',"diferencias entre series y peliculas"])

with tab0:
	
	st.subheader('Cuales son las 10 Peliculas mas Vistas?')
	#fig, ax = plt.subplots(figsize = [8,2])
	#ax = sns.barplot(y = dia_sem, color= 'pink', ax =ax)
	df[df.tipo =='pelicula'].nivel1.value_counts().head(10).sort_values(ascending =True).plot.barh(cmap = 'Pastel1')
	st.pyplot()


with tab1:
	
	st.subheader('Cuales son las 10 Series mas Vistas?')
	#fig, ax = plt.subplots(figsize = [8,2])
	#ax = sns.barplot(y = dia_sem, color= 'pink', ax =ax)
	df[df.tipo =='serie'].nivel1.value_counts().head(10).sort_values(ascending =True).plot.barh(cmap = 'Pastel1')
	st.pyplot()


with tab2:
	st.subheader('Dia de la semana de mayor consumo?')
	fig, ax = plt.subplots(figsize = [8,2])
	ax = sns.countplot(x = df.dia_semana, color= 'pink', ax =ax)
	fig
	st.write(df.dia_semana.value_counts())

with tab3:
	st.subheader('El consumo a lo largo del año es constante o hay meses de mayor consumo')
	fig, ax = plt.subplots(figsize = [8,2])
	ax = sns.countplot(x = df.mes, color ='pink', ax = ax)
	fig
	st.write(df.mes.value_counts())

with tab4:
	st.subheader('existen diferencias entre series y peliculas')
	fig, ax = plt.subplots(figsize = [8,2])
	ax = sns.countplot(x = df.dia_semana, hue = df.tipo, palette='pastel', ax = ax)
	fig
	
st.success('''
	Made by:   
	`Luis Hernandez`  
	luishernandezmatos@yahoo.com
	''')
	

