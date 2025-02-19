# Criando um dicionário de contatos, onde cada chave é um e-mail e o valor é outro dicionário com nome e telefone
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Percorrendo o dicionário e imprimindo a chave (e-mail) e o valor (dicionário com nome e telefone)
for chave in contatos:
    print(chave, contatos[chave])  # Exibe o e-mail e os dados associados

print("=" * 100)  # Linha separadora para melhor visualização

# Outra forma de percorrer o dicionário usando items(), obtendo tanto a chave quanto o valor diretamente
for chave, valor in contatos.items():
    print(f'Chave: {chave}, Valor: {valor}')  # Exibe a chave (e-mail) e os dados formatados
