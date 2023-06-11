"""
class Pessoa
    __init__
        nome str

    API:                 https://jsonplaceholder.typicode.com/users/1
        dados -> method    
            Ok
            404
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../app'
            )
        )
    )
except:
    raise

#import unittest
from unittest import main, TestCase
from unittest.mock import patch
from Pessoa import Pessoa


class TestPessoa(TestCase):
    def setUp(self): # metodo para estanciar a classe antes dos testes
        self.p1 = Pessoa('Sergio')

    def test_pessoa_nome_correct(self):
        self.assertEqual(self.p1.nome, 'Sergio')

    def test_pessoa_nome_str(self):
        self.assertIsInstance(self.p1.nome, str)
        

    def test_dados_sucess(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.sucess = True

            self.assertEqual(self.p1.dados(), 'CONECTADO COM SUCESSO')
    
if __name__ == '__main__':
    main(verbosity=2)