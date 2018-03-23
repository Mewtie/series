from mainModuleV1 import *

lista_series = datos_series()

serie = serie()
tittle = input(str("Ingrese el nombre de la serie\n"))
serie.addSetting(newTitle = tittle)

premiere = input(str("Ingrese el dia de estreno\n"))
serie.addPremiere(premiere)

lista_series = datos_series()
lista_series.addSerie(serie)

lista_series.showSeries()
lista_series.saveData()
