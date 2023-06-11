# Instalando ambiente virtual
python3 -m venv venv

# Ativando e desativando ambiente virtual
. venv/bin/activate

deactivate

# rodando o unittest
python -m unittest tests/test_pessoa.py

# Instalando pytest
pip install pytest

# rodando pytest
pytest

pytest -v -m (nome da marcação)

# exibe o print que estiver na função teste.
pytest -rP 