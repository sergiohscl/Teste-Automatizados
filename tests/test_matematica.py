""" 
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia false)

    API:
        obter_todos_os_dados -> method
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

import unittest
from unittest.mock import patch
from Pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):  # metodo para estanciar a classe antes do test
        self.p1 = Pessoa('Sergio', 'Henrique')

    def test_pessoa_nome_correct(self):
        self.assertEqual(self.p1.nome, 'Sergio')
    
    def test_pessoa_nome_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_sobrenome_correct(self):
        self.assertEqual(self.p1.sobrenome, 'Henrique')
    
    def test_pessoa_sobrenome_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
    
    def test_pessoa_dados_obtidos_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        
    def test_obter_todos_os_dados_sucesso(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO COM SUCESSO')
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_erro_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)

""" 
Pelo que entendi, isso é para determinar o código que é 
executado apenas quando o script é executado 
diretamente/independentemente, não como um módulo 
dentro de outro script.
 """