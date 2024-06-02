from tkinter import *
from tkinter import messagebox

class interface():
    def __init__(self, title, geometry, background):
        self.janela = Tk()
        self.janela.title(title)
        self.janela.geometry(geometry)
        self.janela.configure(bg=background)
        self.janela.mainloop()



interface("tela 1", "350x350", "black")