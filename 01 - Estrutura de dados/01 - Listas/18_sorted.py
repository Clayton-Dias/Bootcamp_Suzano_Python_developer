# Lista inicial de linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Usa a função sorted() para ordenar a lista pelo tamanho das palavras (do menor para o maior)
print(sorted(linguagens, key=lambda x: len(x)))
# Saída: ["c", "js", "java", "python", "csharp"]

# Usa a função sorted() para ordenar a lista pelo tamanho das palavras (do maior para o menor)
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# Saída: ["python", "csharp", "java", "js", "c"]

"""
    Diferença entre sort() e sorted():
        sort(): Modifica a lista original e não retorna um novo objeto.
        sorted(): Retorna uma nova lista ordenada sem alterar a lista original.
    """
