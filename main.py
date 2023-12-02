from tkinter import *

configuration = {
    "title": "Cadastro de Pacientes",
    "geometry": "300x300",
    "background": "#191919",
    "resizable": [False, False],
    "minsize": [300, 300],
    "maxsize": [300, 300]
}

configuration_tela2 = {
    "title": "Área de Cadastro dos Pacientes",
    "geometry": "527x587",
    "background": "#191919",
    "resizable": [False, False],
    "minsize": [527, 587],
    "maxsize": [527,  587]
}

configuration_w = {
    "Cadastro de Pacientes": [0.30, 0.01, "#191919", "white"],
    "Deseja Cadastrar um Cliente": [0.28, 0.30, "#191919", "white"],
    "Botao": [0.45, 0.47, "#fff", 4],
    "Botao_2": [0.45, 0.60, "#fff", 4],
}

class Application():
    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.inputs()
        self.janela.mainloop()

    def tela(self):
        self.janela.title(configuration["title"])
        self.janela.geometry(configuration["geometry"])
        self.janela.config(bg=configuration["background"])
        self.janela.resizable(configuration["resizable"][0], configuration["resizable"][1])
        self.janela.minsize(configuration["minsize"][0], configuration["minsize"][1])
        self.janela.maxsize(configuration["maxsize"][0], configuration["maxsize"][1])

    def inputs(self):
        self.msg = Label(self.janela, text="Cadastro de Pacientes", foreground=configuration_w["Cadastro de Pacientes"][3])
        self.msg.config(bg=configuration_w["Cadastro de Pacientes"][2])
        self.msg.place(relx=configuration_w["Cadastro de Pacientes"][0], rely=configuration_w["Cadastro de Pacientes"][1])

        self.msg2 = Label(self.janela, text="Deseja Cadastrar um Cliente?", foreground=configuration_w["Deseja Cadastrar um Cliente"][3])
        self.msg2.config(bg=configuration_w["Deseja Cadastrar um Cliente"][2])
        self.msg2.place(relx=configuration_w["Deseja Cadastrar um Cliente"][0],rely=configuration_w["Deseja Cadastrar um Cliente"][1])

        #self.bt_limpar = Button(self.frame_1, text="Apagar", bd=2, bg="#107db2", fg='white', font=('verdana', 8, 'bold'))
        self.botao = Button(self.janela, text="Sim", bg=configuration_w["Botao"][2], bd=configuration_w["Botao"][3], font=("verdana", 8, "bold"), command=lambda: self.analisando(1))
        self.botao.place(relx=configuration_w["Botao"][0], rely=configuration_w["Botao"][1])

        #botão não!
        self.botao_2 = Button(self.janela, text="Não", bg=configuration_w["Botao_2"][2], bd=configuration_w["Botao_2"][3], font=("verdana", 8, "bold"), command=lambda: self.analisando(0))
        self.botao_2.place(relx=configuration_w["Botao_2"][0], rely=configuration_w["Botao_2"][1])

    def analisando(self, arg):
        if arg == 1:
            self.janela.destroy()
            self.Tela_2()
        else:
            self.janela.destroy()

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

        self.entry7 = Entry(self.janela2, bd=3, bg="#E6E7DA")
        self.entry7.place(relx=0.15, rely=0.62, height=134, width=350)

        #Botão para enviar
        self.botao_enviar = Button(self.janela2, bg="#E6E7DA", bd=3, text="Enviar", command=lambda: self.Enviar_dados(self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7))
        self.botao_enviar.place(relx=0.40, rely=0.90, width=100)


    def Enviar_dados(self, name, email, city, estado, number, cpf, relato):
        contador = 0
        lista = [name, email, city, estado, number, cpf, relato]
        for item in lista:
            if item.get() == "":
                print(f"{item} vazio")
            elif item.get() != "":
                contador += 1
                print(f"{item} tem item")
                if contador >= 7:
                    print("Enviar")


Application()
