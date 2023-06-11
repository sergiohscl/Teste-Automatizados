import requests

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False
    
    def dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if resposta.sucess:
            return 'CONECTADO COM SUCESSO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'
        