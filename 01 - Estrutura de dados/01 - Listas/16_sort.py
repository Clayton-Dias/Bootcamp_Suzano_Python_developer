# Lista inicial de linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista em ordem alfabética
linguagens.sort()  # Saída: ["c", "csharp", "java", "js", "python"]
print(linguagens)

# Reinicializa a lista para a ordem original
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista em ordem alfabética reversa
linguagens.sort(reverse=True)  # Saída: ["python", "js", "java", "csharp", "c"]
print(linguagens)

# Reinicializa a lista para a ordem original
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista pelo tamanho das palavras (do menor para o maior)
linguagens.sort(key=lambda x: len(x))  # Saída: ["c", "js", "java", "python", "csharp"]
print(linguagens)

# Reinicializa a lista para a ordem original
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista pelo tamanho das palavras (do maior para o menor)
linguagens.sort(key=lambda x: len(x), reverse=True)  # Saída: ["python", "csharp", "java", "js", "c"]
print(linguagens)
