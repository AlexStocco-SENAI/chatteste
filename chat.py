from usuario import Usuario
from mensagem import Mensagem
from contato import Contato
from conexao import Conexao

class Chat:
    
    def __init__(self, nome: str, telefone:str):
        self.nome_usuario = nome
        self.telefone_usuario = telefone
        
    def enviar_mensagem(self, conteudo: str, destinatario:Contato)-> bool:
        try:
            #Conectando ao banco de dados
            mydb = Conexao.conectar()
            
            #Criando o cursor
            mycursor = mydb.cursor()
            
            #Primeira forma
            sql = "INSERT INTO tb_mensagem (tel_remetente, mensagem) VALUES (%s, %s)"
            val = (self.telefone_usuario, conteudo)
            mycursor.execute(sql, val)
            
            #Segunda forma
            # sql = f"INSERT INTO tb_mensagem (tel_remetente, mensagem) VALUES ('{self.usuario.telefone}', '{conteudo}')"
            # mycursor.execute(sql)
            
            mydb.commit()
            
            mydb.close()
            
            return True
        except:
            return False
    
    def verificar_mensagem(self,quantidade: int):
        
        mydb = Conexao.conectar()
        
        mycursor = mydb.cursor()
        
        sql = "SELECT tel_remetente, mensagem FROM tb_mensagem"
        
        mycursor.execute(sql)
        
        resultado = mycursor.fetchall()
        
        mensagens = []
        for linha in resultado:
            mensagem = Mensagem(linha[0],linha[1])
            mensagens.append(mensagem)
        
        return (mensagens)
    
    def retorna_contatos(self):
        
        mydb = Conexao.conectar()
        
        mycursor = mydb.cursor()
        
        sql="SELECT nome, tel FROM tb_usuario ORDER BY nome"
        
        mycursor.execute(sql)
        
        resultado = mycursor.fetchall()
        
        lista_contatos = []
        lista_contatos.append({"nome":"TODOS","telefone":""})
        
        for linha in resultado:
            lista_contatos.append({"nome":linha[0],"telefone":linha[1]})
        
        return (lista_contatos)
    