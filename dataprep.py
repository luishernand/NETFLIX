import pandas as pd 
import numpy as np
from datetime import date

#Function to split columns create news and concat
def split_cols(data):
	separacion= data.Title.str.split(pat =':', expand=False).to_frame()
	#Conteo del numero de las partes
	separacion['num_partes'] = separacion.Title.apply(len)
	#consideramos como pelicula lo de mas sera una serie
	separacion['tipo'] = np.where(separacion.num_partes<3,'pelicula','serie')
	data = pd.concat([data, separacion['tipo']], axis = 1)

	#diviidr por sus diferentes niveles
	separacion_cols = data.Title.str.split(':', expand=True)
	separacion_cols.columns= ['Titulo', 'nivel1','nivel2','nivel3', 'nivel4', 'nivel5']
	data = pd.concat([data, separacion_cols[['Titulo']]], axis =1)

	return data

#Funcion parat extraer de la fecha los componentes (año, mes.....)
def ext_fecha(data):
	data['año'] = data['Date'].dt.year
	data['mes_num'] = data['Date'].dt.month
	data['mes'] = data['Date'].dt.month_name()
	data['dia_mes'] = data['Date'].dt.day
	data['dia_semana'] = data['Date'].dt.day_name()
    
	return data


