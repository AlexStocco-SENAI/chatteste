from conexao import Conexao
from hashlib import sha256

class Usuario:
    def __init__(self) :
        self.nome = None
        self.telefone = None
        self.senha = None
        self.logado = False
        
    def cadastrar(self, telefone, nome, senha):
        
        #criptogrando a senha
            senha = sha256(senha.encode()).hexdigest()
        
        # try:
            #Conectando ao banco de dados
            mydb = Conexao.conectar()
            
            #Criando o cursor
            mycursor = mydb.cursor()
            
            #Primeira forma
            # sql = "INSERT INTO tb_usuario (tel, nome, senha) VALUES (%s, %s, %s)"
            # val = (telefone, nome, senha)
            # mycursor.execute(sql, val)
            
            #Segunda forma
            sql = f"INSERT INTO tb_usuario (tel, nome, senha) VALUES ('{telefone}', '{nome}', '{senha}')"
            mycursor.execute(sql)
            
            mydb.commit()
            
            mydb.close()
            
            self.telefone = telefone
            self.nome = nome
            self.senha = senha
            self.logado = True
            
            return True
        
        #except:
            return False
        
    def logar(self, telefone, senha):
        
        #criptogrando a senha
        senha = sha256(senha.encode()).hexdigest()
        
        mydb = Conexao.conectar()
        
        mycursor = mydb.cursor()
        
        # 1 FORMA
        sql = "SELECT tel, nome, senha FROM tb_usuario WHERE tel=%s AND senha=%s;"
        valores = (telefone,senha)
        mycursor.execute(sql,valores)
        
        #2 FORMA
        # sql = f"SELECT tel, nome, senha  FROM tb_usuario WHERE tel='{telefone}' AND senha='{senha}';"
        # mycursor.execute(sql)
        
        resultado = mycursor.fetchone()
        
        if not resultado == None:
            self.logado = True
            self.nome = resultado[1]
            self.telefone =resultado[0]
            self.senha = resultado[2]
        else:
            self.logado = False