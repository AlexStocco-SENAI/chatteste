import mysql.connector

class Conexao:
    
    def conectar():
        #Conectando ao banco de dados
        mydb = mysql.connector.connect(
            host="10.110.140.130",
            user="equipe",
            password="123456789",
            database="crabiz"
            )
        return mydb