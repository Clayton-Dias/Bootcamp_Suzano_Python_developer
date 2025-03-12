class Estudante:
    """
    Classe para representar um estudante.
    """
    escola = "DIO"  # Atributo de classe (compartilhado por todas as instâncias)

    def __init__(self, nome, matricula):
        """
        Inicializa um objeto Estudante.

        Args:
            nome (str): Nome do estudante.
            matricula (int): Número de matrícula do estudante.
        """
        self.nome = nome  # Atributo de instância (específico para cada objeto)
        self.matricula = matricula  # Atributo de instância

    def __str__(self) -> str:
        """
        Retorna uma representação em string do objeto Estudante.
        """
        return f"{self.nome} - {self.matricula} - {self.escola}"  # Inclui o nome, a matrícula e o nome da escola


def mostrar_valores(*objs):
    """
    Imprime a representação em string de cada objeto fornecido.

    Args:
        *objs: Um número variável de objetos a serem impressos.
    """
    for obj in objs:
        print(obj)


# Cria instâncias da classe Estudante
aluno_1 = Estudante("Guilherme", 1)  # Cria um estudante chamado Guilherme, com matrícula 1
aluno_2 = Estudante("Giovanna", 2)  # Cria um estudante chamada Giovanna, com matrícula 2

# Imprime os valores dos objetos aluno_1 e aluno_2
mostrar_valores(aluno_1, aluno_2)  # Imprime a representação em string dos alunos

# Modifica o atributo de classe "escola"
Estudante.escola = "Python"  # Altera o nome da escola para "Python" (afeta todas as instâncias)

# Cria uma nova instância da classe Estudante
aluno_3 = Estudante("Chappie", 3)  # Cria um estudante chamado Chappie, com matrícula 3

# Imprime os valores dos objetos aluno_1, aluno_2 e aluno_3
mostrar_valores(aluno_1, aluno_2, aluno_3)  # Imprime a representação em string dos alunos (agora todos com a escola "Python")