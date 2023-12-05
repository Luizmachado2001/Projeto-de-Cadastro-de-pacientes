import sqlite3

class Dados():
    def __init__(self):
        self.conect = sqlite3.Connection("banco.db")
        self.cur = self.conect.cursor()
        self.Created_Table()


    def Created_Table(self):
        sql="""
            CREATE TABLE IF NOT EXISTS DADOS
            (name text, email text, city text, estado text, number integer, cpf text, relato_paciente text)
        """
        self.cur.execute(sql)
        self.conect.commit()

    def verificando_name(self, name):
        sql = """
            SELECT NAME FROM DADOS
        """
        self.cur.execute(sql)

        lista = self.cur.fetchall()
        for item in lista:
            if name in item:
                return True
        return False

    def Create_Dados_table(self, name, email, city, estado, number, cpf, relato="none"):
        sql = """
            INSERT INTO DADOS (name, email, city, estado, number, cpf, relato_paciente) VALUES (?,?,?,?,?,?,?)
        """
        if self.verificando_name(name):
            print("name já foi cadastrado")
        else:
            self.cur.execute(sql, (name, email, city, estado, number, cpf, relato))
            self.conect.commit()



Dados()
