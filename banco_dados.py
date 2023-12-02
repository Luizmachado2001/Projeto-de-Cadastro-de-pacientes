import sqlite3

conect = sqlite3.Connection("banco.db")

class Dados():
    def __init__(self):
        self.conect = conect
        self.cur = self.conect.cursor()
        self.Created_Table()
        self.Create_Dados_table("Luiz albert dos santos machado", "luizmachado20010gmail.com", "aracaju", "sergipe", 79998622, "3213312", "paciente descreveu que estava sentindo dor de cabeça")

    def created_dados(self):
        self.conect = sqlite3.Connection("banco.db")

    def Created_Table(self):
        sql="""
            CREATE TABLE IF NOT EXISTS DADOS
            (name text, email text, city text, estado text, number integer, cpf text, relato_paciente text)
        """
        self.cur.execute(sql)
        self.conect.commit()

    def verificando_name(self, name):
        sql="""
            SELECT NAME FROM DADOS
        """
        self.cur.execute(sql)

        lista = self.cur.fetchall()
        for item in lista:
            if name in item:
                return True
            else:
                return False


    def Create_Dados_table(self, name, email, city, estado, number, cpf, relato):
        sql="""
            INSERT INTO DADOS (name, email, city, estado, number, cpf, relato_paciente) VALUES (?,?,?,?,?,?,?)
        """
        if self.verificando_name(name):
            print(f"[{name}] Esse nome já foi cadastrado")
        else:
            self.cur.execute(sql, (name, email, city, estado, number, cpf, relato))
            self.conect.commit()

Dados()


