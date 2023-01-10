import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


series=pd.read_excel(r'C:\Users\Gabriel\Downloads\vacuf.xlsx', engine='openpyxl')

INFOS_UFS=gpd.read_file(r'C:\Users\Gabriel\Downloads\bcim_2016_21_11_2018.gpkg', layer='lim_unidade_federacao_a')



	
INFOS_UFS.rename({'sigla':'UF'}, axis=1, inplace=True)



mapa=INFOS_UFS.merge(series, left_on=['UF'], right_on=['UF'])




mapa.plot(column='Doses Aplicadas',
		  cmap='Reds',
		  figsize=(10,6),
		  edgecolor='black',
		  legend=True
	)
	


	
plt.title("Painel da Vacinação contra a Covid-19 em Cada Estado")

plt.show()
	
