import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


series=pd.read_excel(r"C:\Users\Gabriel\Downloads\vacinacaopordata.xlsx",engine='openpyxl')

series['Data']=pd.to_datetime(series['Data'])

plt.figure(figsize=(13,6))
plt.plot(series['Data'],series['Doses Aplicadas'])

plt.ylabel('Doses Aplicadas(por milhões de doses)')
plt.title('Vacinações realizadas ao longo do tempo(até o dia 25/05/2021)')


plt.show()