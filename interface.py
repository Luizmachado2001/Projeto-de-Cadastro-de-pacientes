from tkinter import *
from tkinter import messagebox

class interface():
    def __init__(self, title="meu titulo", geometry="400x400", background="light blue"):
        self.janela = Tk()
        self.janela.title(title)
        self.janela.geometry(geometry)
        self.janela.configure(bg=background)

    def run(self):
        self.janela.mainloop()



interface = interface()
interface.run()