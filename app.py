from flask import Flask, render_template, request, jsonify, session
from usuario import Usuario

app = Flask(__name__)

app.secret_key = "batatinhafrita123"

@app.route("/")
@app.route("/cadastro")
def pag_cadastro():
    return render_template('cadastro.html')

@app.route("/cadastro_via_requisicao")
def pag_cadastro_ajax():
    return render_template('cadastro_via_requisicao.html')


#Rota para processamento de cadastro feito atravês de envio de dados pelo form
@app.route("/cadastro_form_submit", methods = ["POST"])
def post_cadastro():

    #Pegando os dados do formulario
    nome = request.form['nome']
    telefone = request.form['telefone']
    senha = request.form['senha']
    
    #instanciando usuario
    usuario = Usuario()
    
    #efetuando o cadastro e retornando resultado
    if usuario.cadastrar(telefone,nome,senha):
        session['usuario_logado'] = {'nome':usuario.nome,
                                     'telefone':usuario.telefone}
        return "Usuário Cadastrado!"
    else:
        session.clear()
        return "Erro ao cadastrar!"
    
    
    

#Rota para processamento de cadastro feito atravês de requisição AJAX
@app.route("/cadastro_requisicao_ajax", methods = ["POST"])
def post_cadastro_ajax():
    #Recebendo os dados em json
    dados_cadastro = request.get_json()
    
    nome = dados_cadastro['nome']
    telefone =dados_cadastro['telefone']
    senha = dados_cadastro['senha']
    
    #Instanciando usuario
    usuario = Usuario()
    
    if usuario.cadastrar(telefone,nome, senha):
        return jsonify({'mensagem':'Cadastrado com sucesso'}), 200
    else:
        return jsonify({'mensagem':'Erro ao cadastrar'}), 500
    
app.run(debug=True)

