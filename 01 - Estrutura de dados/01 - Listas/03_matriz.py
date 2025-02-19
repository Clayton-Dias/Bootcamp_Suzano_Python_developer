# Definição de uma matriz (lista de listas) contendo números e caracteres
matriz = [
    [1, "a", 2],   # Primeira linha da matriz
    ["b", 3, 4],   # Segunda linha da matriz
    [6, 5, "c"]    # Terceira linha da matriz
]

# Exibe a primeira linha da matriz
print(matriz[0])  # Saída: [1, "a", 2]

# Acessa e imprime o primeiro elemento da primeira linha (linha 0, coluna 0)
print(matriz[0][0])  # Saída: 1

# Acessa e imprime o último elemento da primeira linha (linha 0, última coluna)
print(matriz[0][-1])  # Saída: 2

# Acessa e imprime o último elemento da última linha (última linha, última coluna)
print(matriz[-1][-1])  # Saída: "c"
