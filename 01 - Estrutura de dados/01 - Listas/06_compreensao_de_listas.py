# Filtrar lista - cria uma nova lista apenas com os números pares
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]  # Filtra os números divisíveis por 2
print(pares)  # Saída: [30, 2, 34]

# Modificar valores - cria uma nova lista com os quadrados dos números originais
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]  # Eleva cada número ao quadrado
print(quadrado)  # Saída: [1, 900, 441, 4, 81, 4225, 1156]
