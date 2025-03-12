from abc import ABC, abstractmethod #, abstractproperty


class ControleRemoto(ABC):
    """
    Classe abstrata para representar um controle remoto.
    """
    @abstractmethod
    def ligar(self):
        """
        Método abstrato para ligar o dispositivo.
        """
        pass

    @abstractmethod
    def desligar(self):
        """
        Método abstrato para desligar o dispositivo.
        """
        pass

    @property
    #@abstractproperty
    def marca(self):
        """
        Propriedade abstrata para obter a marca do dispositivo.
        """
        pass


class ControleTV(ControleRemoto):
    """
    Classe para representar um controle remoto de TV, herdando da classe ControleRemoto.
    """
    def ligar(self):
        """
        Liga a TV.
        """
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        """
        Desliga a TV.
        """
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        """
        Retorna a marca da TV.
        """
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    """
    Classe para representar um controle remoto de ar condicionado, herdando da classe ControleRemoto.
    """
    def ligar(self):
        """
        Liga o ar condicionado.
        """
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        """
        Desliga o ar condicionado.
        """
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        """
        Retorna a marca do ar condicionado.
        """
        return "LG"


# Cria uma instância da classe ControleTV
controleTV = ControleTV()

# Chama os métodos ligar e desligar do controle da TV
controleTV.ligar()  # Saída: Ligando a TV... \n Ligada!
controleTV.desligar() # Saída: Desligando a TV... \n Desligada!

# Imprime a marca da TV
print(controleTV.marca) # Saída: Philco


# Cria uma instância da classe ControleArCondicionado
controleAR = ControleArCondicionado()

# Chama os métodos ligar e desligar do controle do ar condicionado
controleAR.ligar() # Saída: Ligando o Ar Condicionado... \n Ligado!
controleAR.desligar() # Saída: Desligando o Ar Condicionado... \n Desligado!

# Imprime a marca do ar condicionado
print(controleAR.marca) # Saída: LG