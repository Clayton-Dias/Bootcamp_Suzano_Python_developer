class Bicicleta:
    """
    Classe que representa uma bicicleta.
    """
    def __init__(self, cor, modelo, ano, valor):
        """
        Inicializa um objeto Bicicleta.

        Args:
            cor (str): Cor da bicicleta.
            modelo (str): Modelo da bicicleta.
            ano (int): Ano de fabricação da bicicleta.
            valor (float): Valor da bicicleta.
        """
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        """
        Simula o som da buzina da bicicleta.
        """
        print("Plim plim...")

    def parar(self):
        """
        Simula a ação de parar a bicicleta.
        """
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        """
        Simula a ação de correr com a bicicleta.
        """
        print("Vrummmmm...")

    def __str__(self):
        """
        Retorna uma representação em string do objeto Bicicleta.
        """
        #returun f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= R${self.valor} ."
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
            


# Cria uma instância da classe Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# Chama os métodos do objeto b1
b1.buzinar()
b1.correr()
b1.parar()

# Imprime os atributos do objeto b1
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Cria outra instância da classe Bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)

# Imprime o objeto b2 (usa o método __str__)
print(b2)

# Chama o método correr do objeto b2
b2.correr()     ## Bicicleta.correr(b2)


print(b1)
print(b2)