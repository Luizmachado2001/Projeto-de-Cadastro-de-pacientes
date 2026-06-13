from tkinter import Tk, Label, Button


configuration = {
    "title": "Cadastro de Pacientes",
    "geometry": "300x300",
    "background": "#191919",
    "resizable": [False, False],
    "minsize": [300, 300],
    "maxsize": [300, 300]
}

configuration_w = {
    "Cadastro de Pacientes": [0.30, 0.01, "#191919", "white"],
    "Deseja Cadastrar um Cliente": [0.28, 0.30, "#191919", "white"],
    "Botao": [0.45, 0.47, "#fff", 4],
    "Botao_2": [0.45, 0.60, "#fff", 4],
}


class Tela:
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

    def analisando(self, arg):
        if arg == 1:
            self.janela.destroy()
            self.Tela_2()
        else:
            self.janela.destroy()

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


