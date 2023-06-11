from app.matematica import Matematica
import pytest

# @pytest.mark.number
# def test_somar():
#     assert Matematica.somar(1, 2) == 3
#     assert Matematica.somar(4, 5) == 9

# @pytest.mark.strings
# def test_somar_string():
#     result = Matematica.somar('Hello', 'World')
#     assert result == 'HelloWorld'
#     assert type(result) is str
#     assert 'Hello' in result

@pytest.mark.parametrize('num1, num2, result', 
        [
            (1, 2, 3), 
            (4, 5, 9), 
            ('Hello', 'World','HelloWorld')
        ])
def test_add(num1, num2, result):
    assert Matematica.somar(num1, num2) == result