contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Verifica se "guilherme@gmail.com" está nas chaves do dicionário contatos
resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

# Verifica se "megui@gmail.com" está nas chaves do dicionário contatos
resultado = "megui@gmail.com" in contatos  # False
print(resultado)

# Verifica se "idade" está nas chaves do dicionário aninhado de "guilherme@gmail.com"
resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

# Verifica se "telefone" está nas chaves do dicionário aninhado de "giovanna@gmail.com"
resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)
