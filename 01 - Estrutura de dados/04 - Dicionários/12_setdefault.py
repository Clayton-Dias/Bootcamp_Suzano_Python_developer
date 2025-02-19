# Dicionário inicial contendo informações de um contato
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# O método setdefault verifica se a chave "nome" existe. Como já existe, mantém o valor atual ("Guilherme").
contato.setdefault("nome", "Giovanna")  # Retorna "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# O método setdefault verifica se a chave "idade" existe. Como não existe, adiciona a chave com o valor fornecido (28).
contato.setdefault("idade", 28)  # Retorna 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
