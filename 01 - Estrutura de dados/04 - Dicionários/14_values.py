# Dicionário de contatos com e-mails como chaves e informações como valores
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# O método .values() retorna uma visão dos valores do dicionário, ou seja, os dicionários internos
resultado = contatos.values()

# Exibe os valores do dicionário, que são os detalhes dos contatos
print(resultado)
# Saída esperada:
# dict_values([
#   {'nome': 'Guilherme', 'telefone': '3333-2221'},
#   {'nome': 'Giovanna', 'telefone': '3443-2121'},
#   {'nome': 'Chappie', 'telefone': '3344-9871'},
#   {'nome': 'Melaine', 'telefone': '3333-7766'}
# ])

