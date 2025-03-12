class Cachorro:
    """
    Classe que representa um cachorro.
    """
    def __init__(self, nome, cor, acordado=True):
        """
        Inicializa um objeto Cachorro.

        Args:
            nome (str): Nome do cachorro.
            cor (str): Cor do cachorro.
            acordado (bool, optional): Indica se o cachorro está acordado. Defaults to True.
        """
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        """
        Método chamado quando o objeto Cachorro está sendo removido da memória.
        """
        print("Removendo a instância da classe.")

    def falar(self):
        """
        Simula o som que o cachorro faz.
        """
        print("auau")


def criar_cachorro():
    """
    Função para criar um objeto Cachorro e imprimir seu nome.
    """
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


# Cria uma instância da classe Cachorro
c = Cachorro("Chappie", "amarelo")

# Chama o método falar do objeto c
c.falar()

# Imprime "Ola mundo"
print("Ola mundo")

# Remove o objeto c da memória (chama o método __del__)
del c

# Imprime "Ola mundo" várias vezes
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# A função criar_cachorro() está comentada, então não será executada
# criar_cachorro()