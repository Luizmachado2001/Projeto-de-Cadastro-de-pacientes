from tkinter import Tk, Label, Button, Entry, Text, messagebox
from Database.Dados import Dados

configuration_tela2 = {
    "title": "Área de Cadastro dos Pacientes",
    "geometry": "527x587",
    "background": "#191919",
    "resizable": [False, False],
    "minsize": [527, 587],
    "maxsize": [527,  587]
}

class Tela_2:
    def __init__(self):
        self.janela=Tk()
        self.Complementos()
        self.janela.title(configuration_tela2["title"])
        self.janela.geometry(configuration_tela2["geometry"])
        self.janela.config(bg=configuration_tela2["background"])
        self.janela.resizable(configuration_tela2["resizable"][0], configuration_tela2["resizable"][1])
        self.janela.maxsize(configuration_tela2["maxsize"][0], configuration_tela2["maxsize"][1])
        self.janela.minsize(configuration_tela2["minsize"][0], configuration_tela2["minsize"][1])
        self.janela.mainloop()


    def Complementos(self):
        #NOME DA PESSOA
        self.label1 = Label(self.janela, text="SEU NOME COMPLETO", bg="#191919", foreground="#FFF")
        self.label1.place(relx = 0.37,  rely = 0.05)

        self.entry1 = Entry(self.janela, bd=3, bg="#E6E7DA")
        self.entry1.place(relx = 0.15, rely = 0.10, height=33, width=350)

        #EMAIL
        self.label2 = Label(self.janela, text="SEU E-MAIL", bg="#191919", foreground="#fff")
        self.label2.place(relx=0.40, rely=0.18)

        self.entry2 = Entry(self.janela, bd=3, bg="#E6E7DA")
        self.entry2.place(relx=0.15, rely=0.24, height=33, width=350)

        #CIDADE
        self.label3 = Label(self.janela, text="CIDADE", bg="#191919", foreground="#fff")
        self.label3.place(relx=0.25, rely=0.31)

        self.entry3 = Entry(self.janela, bd=3, bg="#E6E7DA")
        self.entry3.place(relx=0.15, rely=0.36, height=33, width=170)

        #ESTADO
        self.label4 = Label(self.janela, text="ESTADO", bg="#191919", foreground="#fff")
        self.label4.place(relx=0.60, rely=0.31)

        self.entry4 = Entry(self.janela, bd=3, bg="#E6E7DA")
        self.entry4.place(relx=0.50, rely=0.36, height=33, width=165)

        #NUMERO DE TELEFONE!
        self.label5 = Label(self.janela, text="NUMERO DE TELEFONE", bg="#191919", foreground="#fff")
        self.label5.place(relx=0.20, rely=0.44)

        self.entry5 = Entry(self.janela, bd=3, bg="#E6E7DA")
        self.entry5.place(relx=0.15, rely=0.48, height=33, width=170)

        #CPF
        self.label6 = Label(self.janela, text="CPF", bg="#191919", foreground="#fff")
        self.label6.place(relx=0.63, rely=0.44)

        self.entry6 = Entry(self.janela, bd=3, bg="#E6E7DA")
        self.entry6.place(relx=0.50, rely=0.48, height=33, width=165)

        #RELATO DO PACIENTE!
        self.label7 = Label(self.janela, text="DIGITE RELATO DO PACIENTE", bg="#191919", foreground="#fff")
        self.label7.place(relx=0.35, rely=0.57)

        self.entry7 = Text(self.janela, bd=3, bg="#E6E7DA")
        self.entry7.place(relx=0.15, rely=0.62, height=134, width=350)

        #Botão para enviar
        self.botao_enviar = Button(self.janela, bg="#E6E7DA", bd=3, text="Enviar", command=lambda: self.Enviar_dados(self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7))
        self.botao_enviar.place(relx=0.40, rely=0.90, width=100)

    def Enviar_dados(self, name, email, city, estado, number, cpf, relato):
        info = {
            "Atenção": ["Está com campos vazios!"],
            "Atenção no relato": ["Está com mais caracteres que o limite permitido [20]"]
        }
        # contador que vai verificar se está com item dentro do argumento, se não estiver, não sobe o resultado.
        # O limite vai verificar se já mostrou a mensagem uma vez para evitar flood.
        contador, limit = 0, 1
        # Vai transformar em uma lista com os valores dos entrys e text os argumentos passados pela função.
        lista = [name.get(), email.get(), city.get(), estado.get(), number.get(), cpf.get(), relato.get("1.0", "end-1c")]
        # Vai pegar o valor do text do começo a última caracter.


        for item in lista:
            if item == "":
                # Verifica se o campo está vazio e se a mensagem já foi mostrada para evitar repetição.
                if limit == 1:
                    messagebox.showinfo(title="Atenção", message=info["Atenção"][0])
                    limit -= 1
            elif item != "":
                contador += 1

        # Verifica se há pelo menos 7 campos preenchidos e se o comprimento do relato é menor ou igual a 10.
        if contador >= 7 and len(lista[6]) <= 20:
            print("Dados enviados com sucesso!")
            dados = Dados()
            dados.enviar_dados(lista[0], lista[1], lista[2],lista[3], lista[4], lista[5], lista[6])
        elif len(lista[6]) in range(0, 19):
            # Caso o comprimento do relato esteja na faixa de 0 a 10 caracteres.
            print("Comprimento do relato dentro da faixa permitida.")
        else:
            # Caso contrário, mostra a mensagem de atenção no relato.
            messagebox.showinfo(title="Atenção no relato", message=info["Atenção no relato"][0])        