class Animal:
    """
    Classe base para representar um animal.
    """
    def __init__(self, nro_patas):
        """
        Inicializa um objeto Animal.

        Args:
            nro_patas (int): Número de patas do animal.
        """
        self.nro_patas = nro_patas

    def __str__(self):
        """
        Retorna uma representação em string do objeto Animal.
        """
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    """
    Classe que representa um mamífero, herdando da classe Animal.
    """
    def __init__(self, cor_pelo, **kw):
        """
        Inicializa um objeto Mamifero.

        Args:
            cor_pelo (str): Cor do pelo do mamífero.
            **kw: Argumentos adicionais a serem passados para a classe pai (Animal).
        """
        self.cor_pelo = cor_pelo
        super().__init__(**kw)  # Chama o construtor da classe pai (Animal)


class Ave(Animal):
    """
    Classe que representa uma ave, herdando da classe Animal.
    """
    def __init__(self, cor_bico, **kw):
        """
        Inicializa um objeto Ave.

        Args:
            cor_bico (str): Cor do bico da ave.
            **kw: Argumentos adicionais a serem passados para a classe pai (Animal).
        """
        self.cor_bico = cor_bico
        super().__init__(**kw)  # Chama o construtor da classe pai (Animal)


class Gato(Mamifero):
    """
    Classe que representa um gato, herdando da classe Mamifero.
    """
    pass  # A classe Gato herda todos os atributos e métodos da classe Mamifero


class Ornitorrinco(Mamifero, Ave):
    """
    Classe que representa um ornitorrinco, herdando das classes Mamifero e Ave.
    """
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        """
        Inicializa um objeto Ornitorrinco.

        Args:
            cor_bico (str): Cor do bico do ornitorrinco.
            cor_pelo (str): Cor do pelo do ornitorrinco.
            nro_patas (int): Número de patas do ornitorrinco.
        """
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)  # Chama os construtores das classes pais (Mamifero e Ave)

        #print(Ornitorrinco.__mro__) ou print(Onitorrinco.mro()) -> exibe a ordem de resolução de métodos (MRO - Method Resolution Order) da classe Ornitorrinco. A ordem de resolução de métodos define a ordem na qual as classes base são pesquisadas quando um método é chamado em uma instância da classe.  
        # mro() é considerado mais legível e é a forma geralmente utilizada na comunidade Python.
         

# Cria uma instância da classe Gato
gato = Gato(nro_patas=4, cor_pelo="Preto")

# Imprime o objeto gato (usa o método __str__)
print(gato)

# Cria uma instância da classe Ornitorrinco
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")

# Imprime o objeto ornitorrinco (usa o método __str__)
print(ornitorrinco)