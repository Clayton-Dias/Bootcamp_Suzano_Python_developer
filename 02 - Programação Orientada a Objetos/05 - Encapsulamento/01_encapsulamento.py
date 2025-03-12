class Conta:
    """
    Classe para representar uma conta bancária.
    """
    def __init__(self, nro_agencia, saldo=0):
        """
        Inicializa um objeto Conta.

        Args:
            nro_agencia (str): Número da agência da conta.
            saldo (float, optional): Saldo inicial da conta. Defaults to 0.
        """
        self._saldo = saldo  # Atributo protegido (convenção para indicar que não deve ser acessado diretamente)
        self.nro_agencia = nro_agencia  # Atributo público

    def depositar(self, valor):
        """
        Deposita um valor na conta.

        Args:
            valor (float): Valor a ser depositado.
        """
        # Lógica para depositar o valor (exemplo básico)
        self._saldo += valor

    def sacar(self, valor):
        """
        Saca um valor da conta.

        Args:
            valor (float): Valor a ser sacado.
        """
        # Lógica para sacar o valor (exemplo básico)
        self._saldo -= valor

    def mostrar_saldo(self):
        """
        Retorna o saldo atual da conta.

        Returns:
            float: O saldo da conta.
        """
        # Lógica para mostrar o saldo
        return self._saldo


# Cria uma instância da classe Conta
conta = Conta("0001", 100)  # Cria uma conta com agência "0001" e saldo inicial 100

# Deposita 100 na conta
conta.depositar(100)

# Imprime o número da agência da conta
print(conta.nro_agencia)  # Acessa o atributo público nro_agencia

# Imprime o saldo da conta
print(conta.mostrar_saldo())  # Chama o método mostrar_saldo() para obter o saldo