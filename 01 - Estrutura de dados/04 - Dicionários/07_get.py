# Dicionário contendo um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Tentativa de acessar uma chave inexistente diretamente resultaria em KeyError
# contatos["chave"]  # KeyError

# Usando o método get para acessar uma chave inexistente retorna None, evitando erro
resultado = contatos.get("chave")  # None
print(resultado)

# Usando get com um valor padrão (neste caso, um dicionário vazio)
resultado = contatos.get("chave", {})  # {}
print(resultado)

# Usando get para acessar uma chave existente, retorna o valor associado
resultado = contatos.get("guilherme@gmail.com", {})  
# Retorna: {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)

