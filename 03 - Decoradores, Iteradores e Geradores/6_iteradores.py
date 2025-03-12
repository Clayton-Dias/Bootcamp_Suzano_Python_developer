class MeuIterador:
    """
    Um iterador personalizado que duplica os números de uma lista.
    """

    def __init__(self, numeros: list[int]):
        """
        Inicializa o iterador com uma lista de números.

        Args:
            numeros: A lista de números a serem iterados.
        """
        self.numeros = numeros  # Armazena a lista de números
        self.contador = 0  # Inicializa o contador para rastrear a posição atual na lista

    def __iter__(self):
        """
        Retorna o próprio iterador (self).

        Este método é necessário para que a classe seja iterável.
        """
        return self  # Retorna o próprio objeto como iterador

    def __next__(self):
        """
        Retorna o próximo valor (duplicado) na iteração.

        Raises:
            StopIteration: Quando não há mais elementos na lista.

        Returns:
            O dobro do próximo número na lista.
        """
        try:
            numero = self.numeros[self.contador]  # Obtém o número na posição atual do contador
            self.contador += 1  # Incrementa o contador para a próxima posição
            return numero * 2  # Retorna o dobro do número
        except IndexError:
            raise StopIteration  # Levanta a exceção StopIteration quando o contador excede o tamanho da lista


for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)  # Imprime o dobro de cada número gerado pelo iterador