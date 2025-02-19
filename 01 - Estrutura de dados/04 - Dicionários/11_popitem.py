# Dicionário contendo um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Remove e retorna um par chave-valor do dicionário como uma tupla
resultado = contatos.popitem()  
# Retorna: ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# Tentativa de remover outro item quando o dicionário já está vazio causaria um KeyError
# contatos.popitem()  # KeyError

