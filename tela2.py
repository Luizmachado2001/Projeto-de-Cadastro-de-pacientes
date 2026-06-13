configuration_tela2 = {
    "title": "Área de Cadastro dos Pacientes",
    "geometry": "527x587",
    "background": "#191919",
    "resizable": [False, False],
    "minsize": [527, 587],
    "maxsize": [527,  587]
}

from tkinter import Tk, Label, Button, Entry, Text


class Tela_2:
    def __init__(self):
        pass

    def Tela_2(self):
        self.janela2=Tk()
        self.Tela_2_config()
        self.Complementos()
        self.janela2.mainloop()

    def Tela_2_config(self):
        self.janela2.title(configuration_tela2["title"])
        self.janela2.geometry(configuration_tela2["geometry"])
        self.janela2.config(bg=configuration_tela2["background"])
        self.janela2.resizable(configuration_tela2["resizable"][0], configuration_tela2["resizable"][1])
        self.janela2.maxsize(configuration_tela2["maxsize"][0], configuration_tela2["maxsize"][1])
        self.janela2.minsize(configuration_tela2["minsize"][0], configuration_tela2["minsize"][1])

    def Complementos(self):
        #NOME DA PESSOA
        self.label1 = Label(self.janela2, text="SEU NOME COMPLETO", bg="#191919", foreground="#FFF")
        self.label1.place(relx = 0.37,  rely = 0.05)

        self.entry1 = Entry(self.janela2, bd=3, bg="#E6E7DA")
        self.entry1.place(relx = 0.15, rely = 0.10, height=33, width=350)

        #EMAIL
        self.label2 = Label(self.janela2, text="SEU E-MAIL", bg="#191919", foreground="#fff")
        self.label2.place(relx=0.40, rely=0.18)

        self.entry2 = Entry(self.janela2, bd=3, bg="#E6E7DA")
        self.entry2.place(relx=0.15, rely=0.24, height=33, width=350)

        #CIDADE
        self.label3 = Label(self.janela2, text="CIDADE", bg="#191919", foreground="#fff")
        self.label3.place(relx=0.25, rely=0.31)

        self.entry3 = Entry(self.janela2, bd=3, bg="#E6E7DA")
        self.entry3.place(relx=0.15, rely=0.36, height=33, width=170)

        #ESTADO
        self.label4 = Label(self.janela2, text="ESTADO", bg="#191919", foreground="#fff")
        self.label4.place(relx=0.60, rely=0.31)

        self.entry4 = Entry(self.janela2, bd=3, bg="#E6E7DA")
        self.entry4.place(relx=0.50, rely=0.36, height=33, width=165)

        #NUMERO DE TELEFONE!
        self.label5 = Label(self.janela2, text="NUMERO DE TELEFONE", bg="#191919", foreground="#fff")
        self.label5.place(relx=0.20, rely=0.44)

        self.entry5 = Entry(self.janela2, bd=3, bg="#E6E7DA")
        self.entry5.place(relx=0.15, rely=0.48, height=33, width=170)

        #CPF
        self.label6 = Label(self.janela2, text="CPF", bg="#191919", foreground="#fff")
        self.label6.place(relx=0.63, rely=0.44)

        self.entry6 = Entry(self.janela2, bd=3, bg="#E6E7DA")
        self.entry6.place(relx=0.50, rely=0.48, height=33, width=165)

        #RELATO DO PACIENTE!
        self.label7 = Label(self.janela2, text="DIGITE RELATO DO PACIENTE", bg="#191919", foreground="#fff")
        self.label7.place(relx=0.35, rely=0.57)

        self.entry7 = Text(self.janela2, bd=3, bg="#E6E7DA")
        self.entry7.place(relx=0.15, rely=0.62, height=134, width=350)

        #Botão para enviar
        self.botao_enviar = Button(self.janela2, bg="#E6E7DA", bd=3, text="Enviar", command=lambda: self.Enviar_dados(self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7))
        self.botao_enviar.place(relx=0.40, rely=0.90, width=100)