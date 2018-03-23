from mainModuleV1 import *
from tkinter import *

class menu():
    def __init__(self):
        self.objWindow = Tk()
        self.objWindow.title("Organizador de Series")
        self.objWindow.geometry("420x280")
        self.fileImgTitle = PhotoImage(file = "files/imgTitle.gif")
        self.imgTitle = Label(self.objWindow, image = self.fileImgTitle)
        self.imgTitle.pack()




    def mainMenu(self):
        self.addSerieBottom = Button(self.objWindow, text = "Agregar Serie", command = self.redimencionar)
        self.addSerieBottom.pack()
        self.removeSerieBottom = Button(self.objWindow, text = "Remover Serie", command = self.redimencionar1)
        self.removeSerieBottom.pack()
        self.toListSerieBottom = Button(self.objWindow, text = "Listar Series")
        self.toListSerieBottom.pack()
        self.loadDataBaseBottom = Button(self.objWindow, text = "Cargar una base de datos")
        self.loadDataBaseBottom.pack()

        self.objWindow.mainloop()

    def redimencionar(self):
        self.objWindow.geometry("600x420")

    def redimencionar1(self):
        self.objWindow.geometry("420x280")



objMenu = menu()
objMenu.mainMenu()
