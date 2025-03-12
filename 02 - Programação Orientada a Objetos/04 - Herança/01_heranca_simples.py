class Veiculo:
    """
    Classe base para representar um veículo.
    """
    def __init__(self, cor, placa, numero_rodas):
        """
        Inicializa um objeto Veiculo.

        Args:
            cor (str): Cor do veículo.
            placa (str): Placa do veículo.
            numero_rodas (int): Número de rodas do veículo.
        """
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        """
        Simula a ação de ligar o motor do veículo.
        """
        print("Ligando o motor")

    def __str__(self):
        """
        Retorna uma representação em string do objeto Veiculo.
        """
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    """
    Classe que representa uma motocicleta, herdando da classe Veiculo.
    """
    pass # A classe Motocicleta herda todos os atributos e métodos da classe Veiculo


class Carro(Veiculo):
    """
    Classe que representa um carro, herdando da classe Veiculo.
    """
    pass # A classe Carro herda todos os atributos e métodos da classe Veiculo


class Caminhao(Veiculo):
    """
    Classe que representa um caminhão, herdando da classe Veiculo.
    """
    def __init__(self, cor, placa, numero_rodas, carregado):
        """
        Inicializa um objeto Caminhao.

        Args:
            cor (str): Cor do caminhão.
            placa (str): Placa do caminhão.
            numero_rodas (int): Número de rodas do caminhão.
            carregado (bool): Indica se o caminhão está carregado.
        """
        super().__init__(cor, placa, numero_rodas) # Chama o construtor da classe pai (Veiculo)
        self.carregado = carregado

    def esta_carregado(self):
        """
        Imprime se o caminhão está carregado ou não.
        """
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# Cria instâncias das classes Motocicleta, Carro e Caminhao
moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

# Imprime os objetos moto, carro e caminhao (usa o método __str__)
print(moto)
print(carro)
print(caminhao)