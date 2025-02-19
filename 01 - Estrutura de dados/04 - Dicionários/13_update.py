# Dicionário inicial contendo contatos
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# O método update sobrescreve completamente o valor associado à chave "guilherme@gmail.com",
# substituindo todo o dicionário interno pelo novo {'nome': 'Gui'}, removendo o telefone.
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

# O método update adiciona um novo contato ao dicionário,
# pois "giovanna@gmail.com" ainda não existia no dicionário.
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos)  
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
