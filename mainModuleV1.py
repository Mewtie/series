#!/usr/bin/python3
import datetime
import pickle

class serie():

    def __init__(self):

        self.__title = "Default"
        self.__sort = "Default"
        self.__language = "Default"


        self.__premiere = "Default"
        self.__state = "Default"
        self.__url = "Default"
        self.__episode = 0
    # Testing features

    def addSetting(self, newTitle = "Default", newSort = "Default", newLanguage = "Default", newPremiere = "Default", newUrl = "Default"):

        self.__title = newTitle
        self.__sort = newSort
        self.__language = newLanguage

        # Date format : yyyy-mm-dd
        # choices notDefined, unknown

        self.addPremiere(newPremiere)
        self.addUrl(newUrl)


    def addPremiere(self, newPremiere = "Default"):
        # Date format : yyyy mm dd
        # choices notDefined, unknown
        # premiere es el día de estreno del ultimo episodio visto

        self.__premiere = newPremiere

        if (self.__premiere[0] == "2" ):

            partsFromPremiere = self.__premiere.split()
            objDatePremiere = datetime.date( int(partsFromPremiere[0]), int(partsFromPremiere[1]), int(partsFromPremiere[2]) )

            self.__premiere = objDatePremiere



        if(type(self.__premiere) == str):

            if self.__premiere == "Default":
                self.__state = "Desconocido"

        elif(type(self.__premiere == object)):

            self.updateStatus()

    def updateStatus(self):
        # Date format : yyyy-mm-dd
        # choices notDefined, unknown

        if(type(self.__premiere == object)):

            __today = datetime.date.today()
            episodios = 0

            if self.__premiere > __today:
                self.__state = "Aun no esta al aire"

            elif self.__premiere == __today:
                self.__state = "Al aire"
                self.__episode = 0

            elif self.__premiere < __today:
                self.__state = "Al aire"

                __subTract = __today - self.__premiere
                __subTractInParts = str(__subTract).split()

                if int(__subTractInParts[0]) < 7:
                    self.__episode = 0

                elif int(__subTractInParts[0]) >= 7:
                    dato = int(__subTractInParts[0])

                    while dato >= 7:
                        dato = dato - 7
                        episodios = episodios + 1

                    self.__episode = episodios


    def addUrl(self, newUrl):
        self.__url = newUrl

    def showTitle(self):
        return self.__title

    def showStatus(self):
        return self.__state
    def showEpisode(self):
        return self.__episode
    def showPremiere(self):
        return self.__premiere
class datos_series():
    lista_series = []

    def __init__(self):
        archive = open("DB_series", "ab+")
        archive.seek(0)

        try:
            self.lista_series = pickle.load(archive)
            print("Se ha cargado la base de datos de las series")
        except:
            print("No hay base de datos anterio\nSe creara una nueva")
        finally:
            archive.close()
            del (archive)

    def addSerie(self, serie):
        self.lista_series.append(serie)
        print("Se agrego la serie con el titulo de : " + serie.showTitle())
    def showSeries(self):
        for i in range(len(self.lista_series)):
            print(self.lista_series[i].showTitle())
            print(self.lista_series[i].showStatus())
            print(self.lista_series[i].showPremiere())
            print(self.lista_series[i].showEpisode())
    def saveData(self):
        archive = open("DB_series", "wb")
        pickle.dump(self.lista_series, archive)
        archive.close()
        del (archive)
        print("Las series han sido guardadas")
