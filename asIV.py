import matplotlib.pyplot as plt



norte=4077677
centro_oeste=4801722
sul=10372845
sudeste=27788388
nordeste=15306888

regioes=[norte, centro_oeste, sul,sudeste, nordeste]

labels='Norte','Centro-Oeste','Sul','Sudeste','Nordeste'

cores=['gold', 'yellowgreen', 'coral', 'lightskyblue', 'red']
patches,texts,autotexts=plt.pie(regioes,colors=cores,autopct='%1.1f%%',startangle=90)

plt.title("Porcentagem de Vacinação po Região")
plt.legend(patches,labels,loc="lower right")
plt.axis('equal')
plt.show()