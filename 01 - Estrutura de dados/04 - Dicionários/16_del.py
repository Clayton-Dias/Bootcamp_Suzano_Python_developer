# Dicionário de contatos com e-mails como chaves e informações detalhadas como valores
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Remove a chave "telefone" do contato de Guilherme
del contatos["guilherme@gmail.com"]["telefone"]

# Remove completamente o contato de Chappie do dicionário
del contatos["chappie@gmail.com"]

# Exibe o dicionário atualizado após as remoções
print(contatos)

# Saída esperada:
# {
#   'guilherme@gmail.com': {'nome': 'Guilherme'},
#   'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
#   'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}
# }

