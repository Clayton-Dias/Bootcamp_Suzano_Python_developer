class Pessoa:
    """
    Classe para representar uma pessoa.
    """
    def __init__(self, nome, ano_nascimento):
        """
        Inicializa um objeto Pessoa.

        Args:
            nome (str): Nome da pessoa.
            ano_nascimento (int): Ano de nascimento da pessoa.
        """
        self.nome = nome  # Atributo público
        self._ano_nascimento = ano_nascimento  # Atributo protegido (convenção para indicar que não deve ser acessado diretamente)

    @property
    def idade(self):
        """
        Calcula e retorna a idade da pessoa com base no ano de nascimento.

        Returns:
            int: A idade da pessoa.
        """
        _ano_atual = 2022  # Ano atual (fixo para este exemplo)
        return _ano_atual - self._ano_nascimento  # Calcula a idade


# Cria uma instância da classe Pessoa
pessoa = Pessoa("Guilherme", 1994)  # Cria uma pessoa chamada Guilherme, nascida em 1994

# Imprime o nome e a idade da pessoa
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")  # Acessa o atributo público nome e a propriedade idade