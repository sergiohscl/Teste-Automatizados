import requests

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if resposta.sucess:
            return 'CONECTADO COM SUCESSO'
        