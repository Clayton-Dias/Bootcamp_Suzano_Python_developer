# Criando um dicionário usando fromkeys, onde as chaves são "nome" e "telefone"
# Sem especificar um valor padrão, os valores serão None
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# Criando um dicionário usando fromkeys e definindo "vazio" como valor padrão para todas as chaves
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

