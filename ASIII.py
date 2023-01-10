import pandas as pd
import plotly.graph_objects as go

series=pd.read_excel(r'C:\Users\Gabriel\Downloads\vacinacaoporestado.xlsx', engine='openpyxl')

fig=go.Figure(data=go.Choropleth(locations=series['UF'], 
		z=series['Doses Aplicadas'].astype(int),
		locationmode='BR-states',
		colorscale='Blues',
		colorbar_title="Vacinação Contra a Covid-19",))
		
fig.update layout(
	title text='Painel da Vacinação Contra a Covid-19 no Brasil',
	geo scope='br',)
	
fig.show()