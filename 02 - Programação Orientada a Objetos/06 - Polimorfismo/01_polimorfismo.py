class Passaro:
    """
    Classe base para representar um pássaro.
    """
    def voar(self):
        """
        Simula a ação de voar de um pássaro.
        """
        print("Voando...")


class Pardal(Passaro):
    """
    Classe que representa um pardal, herdando da classe Passaro.
    """
    def voar(self):
        """
        Implementação específica do voo para um pardal.
        """
        print("Pardal pode voar")


class Avestruz(Passaro):
    """
    Classe que representa uma avestruz, herdando da classe Passaro.
    """
    def voar(self):
        """
        Implementação específica do voo para uma avestruz (que não voa).
        """
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    """
    Classe que representa um avião, herdando da classe Passaro (exemplo de uso inadequado de herança).
    """
    def voar(self):
        """
        Implementação específica do voo para um avião.
        """
        print("Avião está decolando...")


def plano_voo(obj):
    """
    Executa o plano de voo para um objeto que possui o método voar.

    Args:
        obj: Um objeto que possui o método voar.
    """
    obj.voar()


# Executa o plano de voo para diferentes objetos
plano_voo(Pardal())   # Saída: Pardal pode voar
plano_voo(Avestruz())  # Saída: Avestruz não pode voar
plano_voo(Aviao())    # Saída: Avião está decolando...

# Observação: O exemplo com o Aviao ilustra um uso incorreto de herança.
# Um avião não "é um" pássaro (relação "é um" é a base da herança), mas sim "tem a capacidade de" voar.
# Uma abordagem mais adequada seria usar interfaces ou composição para modelar a capacidade de voar.