# Dicionário contendo um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Remove e retorna o valor associado à chave especificada
resultado = contatos.pop("guilherme@gmail.com")  
# Retorna: {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# Tentativa de remover novamente a mesma chave, mas como já foi removida, retorna o valor padrão {}
resultado = contatos.pop("guilherme@gmail.com", {})  # Retorna: {}
print(resultado)
