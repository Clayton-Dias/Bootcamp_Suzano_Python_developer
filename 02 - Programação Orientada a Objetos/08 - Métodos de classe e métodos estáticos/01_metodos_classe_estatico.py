import datetime

class Pessoa:
    """
    Classe para representar uma pessoa.
    """
    def __init__(self, nome, idade):
        """
        Inicializa um objeto Pessoa.

        Args:
            nome (str): Nome da pessoa.
            idade (int): Idade da pessoa.
        """
        self.nome = nome  # Atributo de instância (nome da pessoa)
        self.idade = idade  # Atributo de instância (idade da pessoa)

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        """
        Cria um objeto Pessoa a partir da data de nascimento.

        Args:
            ano (int): Ano de nascimento.
            mes (int): Mês de nascimento.
            dia (int): Dia de nascimento.
            nome (str): Nome da pessoa.

        Returns:
            Pessoa: Um novo objeto Pessoa.
        """
        
        idade = datetime.datetime.now().year - ano  # Calcula a idade com base no ano de nascimento e no ano atual
        #idade = 2022 - ano  # Calcula a idade com base no ano de nascimento (ano atual fixo em 2022)
        return cls(nome, idade)  # Retorna um novo objeto Pessoa (usa a classe atual)

    @staticmethod
    def e_maior_idade(idade):
        """
        Verifica se uma pessoa é maior de idade.

        Args:
            idade (int): Idade da pessoa.

        Returns:
            bool: True se a pessoa for maior de idade, False caso contrário.
        """
        return idade >= 18  # Retorna True se a idade for maior ou igual a 18, senão False


# Cria um objeto Pessoa usando o método de classe criar_de_data_nascimento
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")  # Cria uma pessoa chamada Guilherme, nascida em 1994 (idade calculada como 2022-1994=28)

# Imprime o nome e a idade da pessoa
print(p.nome, p.idade)  # Saída: Guilherme 28

# Verifica se uma pessoa é maior de idade usando o método estático e_maior_idade
print(Pessoa.e_maior_idade(18))  # Saída: True
print(Pessoa.e_maior_idade(8))   # Saída: False

