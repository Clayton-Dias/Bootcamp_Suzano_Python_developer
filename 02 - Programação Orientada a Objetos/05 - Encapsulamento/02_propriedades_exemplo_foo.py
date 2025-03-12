class Foo:
    """
    Classe de exemplo para demonstrar o uso de properties (getters, setters e deleters).
    """
    def __init__(self, x=None):
        """
        Inicializa um objeto Foo.

        Args:
            x (int, optional): Valor inicial de x. Defaults to None.
        """
        self._x = x  # Atributo privado (por convenção) para armazenar o valor de x

    @property
    def x(self):
        """
        Getter para a propriedade x. Retorna o valor de _x ou 0 se _x for None.

        Returns:
            int: O valor de _x ou 0.
        """
        return self._x or 0  # Retorna _x se não for None, senão retorna 0

    @x.setter
    def x(self, value):
        """
        Setter para a propriedade x. Adiciona o valor fornecido ao valor atual de _x.

        Args:
            value (int): Valor a ser adicionado a _x.
        """
        self._x += value  # Adiciona o valor fornecido a _x

    @x.deleter
    def x(self):
        """
        Deleter para a propriedade x. Define o valor de _x como 0.
        """
        self._x = 0  # Define _x como 0


# Cria uma instância da classe Foo com valor inicial de x = 10
foo = Foo(10)

# Imprime o valor de x (usa o getter)
print(foo.x)  # Saída: 10

# Deleta a propriedade x (usa o deleter, definindo _x como 0)
del foo.x

# Imprime o valor de x novamente (usa o getter, que agora retorna 0)
print(foo.x)  # Saída: 0

# Define a propriedade x como 10 (usa o setter, adicionando 10 ao valor atual de _x, que é 0)
foo.x = 10

# Imprime o valor de x (usa o getter, que agora retorna 10)
print(foo.x)  # Saída: 10