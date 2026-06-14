import sqlite3

class Dados:
    """
        Classe responsável pela comunicação com o banco de dados SQLite.
        Gerencia criação de tabelas, verificação e inserção de pacientes.
    """

    def __init__(self):
        self.connect = sqlite3.connect("banco.db")
        self.cur = self.connect.cursor()
        self.created_table()


    def created_table(self) -> None:
        """
           Cria a tabela DADOS no banco de dados caso ainda não exista,
           contendo os campos: nome, email, cidade, estado, número, cpf e relato do paciente.
        """

        sql="""
            CREATE TABLE IF NOT EXISTS DADOS
            (name text, email text, city text, estado text, number integer, cpf text, relato_paciente text)
        """
        self.cur.execute(sql)
        self.connect.commit()


    def verificando_name(self, name):
        """Verifica se o paciente já existe no banco pelo nome."""

        sql = """
            SELECT NAME FROM DADOS
        """
        self.cur.execute(sql)

        lista = self.cur.fetchall()
        for item in lista:
            if name in item:
                return True
        return False

    def enviar_dados(self, name, email, city, estado, number, cpf, relato="none"):
        """
           Verifica se o paciente já existe no banco pelo nome,
           caso não exista, insere os dados do paciente na tabela DADOS.
        """

        sql = """
            INSERT INTO DADOS (name, email, city, estado, number, cpf, relato_paciente) VALUES (?,?,?,?,?,?,?)
        """
        if self.verificando_name(name):
            print("name já foi cadastrado")
        else:
            self.cur.execute(sql, (name, email, city, estado, number, cpf, relato))
            self.connect.commit()
            self.connect.close()



