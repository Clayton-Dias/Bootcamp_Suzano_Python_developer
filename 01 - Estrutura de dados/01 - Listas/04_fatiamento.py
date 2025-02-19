# Definição de uma lista com os caracteres da palavra "python"
lista = ["p", "y", "t", "h", "o", "n"]

# Fatia a lista a partir do índice 2 até o final
print(lista[2:])  # Saída: ["t", "h", "o", "n"]

# Fatia a lista do início até o índice 2 (não inclui o índice 2)
print(lista[:2])  # Saída: ["p", "y"]

# Fatia a lista do índice 1 até o índice 3 (não inclui o índice 3)
print(lista[1:3])  # Saída: ["y", "t"]

# Fatia a lista do índice 0 ao índice 3, pulando de 2 em 2 elementos
print(lista[0:3:2])  # Saída: ["p", "t"]

# Retorna toda a lista sem modificações
print(lista[::])  # Saída: ["p", "y", "t", "h", "o", "n"]

# Retorna a lista invertida
print(lista[::-1])  # Saída: ["n", "o", "h", "t", "y", "p"]

