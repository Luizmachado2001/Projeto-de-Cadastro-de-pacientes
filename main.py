from tkinter import *
from tkinter import messagebox
from banco_dados import Dados

from tela import Tela

configuration_w = {
    "Cadastro de Pacientes": [0.30, 0.01, "#191919", "white"],
    "Deseja Cadastrar um Cliente": [0.28, 0.30, "#191919", "white"],
    "Botao": [0.45, 0.47, "#fff", 4],
    "Botao_2": [0.45, 0.60, "#fff", 4],
}

class Application():
    def __init__(self):
        Tela()


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
            dados.Create_Dados_table(lista[0], lista[1], lista[2],lista[3], lista[4], lista[5], lista[6])
        elif len(lista[6]) in range(0, 19):
            # Caso o comprimento do relato esteja na faixa de 0 a 10 caracteres.
            print("Comprimento do relato dentro da faixa permitida.")
        else:
            # Caso contrário, mostra a mensagem de atenção no relato.
            messagebox.showinfo(title="Atenção no relato", message=info["Atenção no relato"][0])



Application()

