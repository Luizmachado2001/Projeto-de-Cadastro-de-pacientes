import sqlite3

class Dados:
    def __init__(self):
        self.connect = sqlite3.Connection("banco.db")
        self.cur = self.connect.cursor()
        self.created_table()


    def created_table(self):
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
        sql = """
            INSERT INTO DADOS (name, email, city, estado, number, cpf, relato_paciente) VALUES (?,?,?,?,?,?,?)
        """
        if self.verificando_name(name):
            print("name já foi cadastrado")
        else:
            self.cur.execute(sql, (name, email, city, estado, number, cpf, relato))
            self.connect.commit()
            self.connect.close()



