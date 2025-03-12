def meu_gerador(numeros: list[int]):
    """
    Um gerador que duplica cada número em uma lista.

    Args:
        numeros: Uma lista de números inteiros.

    Yields:
        O dobro de cada número na lista de entrada.
    """
    for numero in numeros:
        yield numero * 2  # A palavra-chave 'yield' transforma a função em um gerador.


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)  # Imprime o dobro de cada número gerado.
