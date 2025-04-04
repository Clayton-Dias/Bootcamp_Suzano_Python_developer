import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    """
    Classe base para clientes do banco.
    """
    def __init__(self, endereco):
        """
        Inicializa um cliente com um endereço.

        Args:
            endereco (str): Endereço do cliente.
        """
        self.endereco = endereco
        self.contas = []  # Lista para armazenar as contas do cliente

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação na conta do cliente.

        Args:
            conta (Conta): A conta onde a transação será realizada.
            transacao (Transacao): A transação a ser realizada.
        """
        transacao.registrar(conta)  # Registra a transação na conta

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.

        Args:
            conta (Conta): A conta a ser adicionada.
        """
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Classe para representar clientes que são pessoas físicas, herdando de Cliente.
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        """
        Inicializa uma pessoa física com nome, data de nascimento, CPF e endereço.

        Args:
            nome (str): Nome completo da pessoa física.
            data_nascimento (str): Data de nascimento da pessoa física.
            cpf (str): CPF da pessoa física.
            endereco (str): Endereço da pessoa física.
        """
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    """
    Classe base para contas bancárias.
    """
    def __init__(self, numero, cliente):
        """
        Inicializa uma conta com número, cliente e informações padrão.

        Args:
            numero (str): Número da conta.
            cliente (Cliente): Cliente titular da conta.
        """
        self._saldo = 0  # Saldo inicial da conta
        self._numero = numero
        self._agencia = "0001"  # Agência padrão
        self._cliente = cliente
        self._historico = Historico()  # Histórico de transações da conta

    @classmethod
    def nova_conta(cls, cliente, numero):
        """
        Método de fábrica para criar novas contas.

        Args:
            cliente (Cliente): Cliente titular da conta.
            numero (str): Número da conta.

        Returns:
            Conta: Uma nova instância da classe Conta.
        """
        return cls(numero, cliente)

    @property
    def saldo(self):
        """
        Retorna o saldo da conta.
        """
        return self._saldo

    @property
    def numero(self):
        """
        Retorna o número da conta.
        """
        return self._numero

    @property
    def agencia(self):
        """
        Retorna o número da agência da conta.
        """
        return self._agencia

    @property
    def cliente(self):
        """
        Retorna o cliente titular da conta.
        """
        return self._cliente

    @property
    def historico(self):
        """
        Retorna o histórico de transações da conta.
        """
        return self._historico

    def sacar(self, valor):
        """
        Realiza um saque na conta, verificando se há saldo suficiente.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque for realizado com sucesso, False caso contrário.
        """
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): Valor a ser depositado.

        Returns:
            bool: True se o depósito for realizado com sucesso, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    """
    Classe para contas correntes, herdando de Conta e adicionando limite e limite de saques.
    """
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        """
        Inicializa uma conta corrente com número, cliente, limite de crédito e limite de saques.

        Args:
            numero (str): Número da conta corrente.
            cliente (Cliente): Cliente titular da conta corrente.
            limite (float, optional): Limite de crédito da conta corrente. Defaults to 500.
            limite_saques (int, optional): Limite de saques diários da conta corrente. Defaults to 3.
        """
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente, verificando o limite de crédito e o limite de saques diários.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque for realizado com sucesso, False caso contrário.
        """
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)  # Chama o método sacar da classe pai

        return False

    def __str__(self):
        """
        Retorna uma representação em string da conta corrente.
        """
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    """
    Classe para armazenar o histórico de transações de uma conta.
    """
    def __init__(self):
        """
        Inicializa o histórico com uma lista vazia de transações.
        """
        self._transacoes = []

    @property
    def transacoes(self):
        """
        Retorna a lista de transações.
        """
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma transação ao histórico.

        Args:
            transacao (Transacao): A transação a ser adicionada.
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Tipo da transação (Saque, Deposito)
                "valor": transacao.valor,  # Valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Data e hora da transação
            }
        )


class Transacao(ABC):
    """
    Classe abstrata para transações bancárias.
    """
    @property
    @abstractproperty
    def valor(self):
        """
        Método abstrato para obter o valor da transação.
        """
        pass

    @abstractclassmethod
    def registrar(self, conta):
        """
        Método abstrato para registrar a transação em uma conta.
        """
        pass


class Saque(Transacao):
    """
    Classe para representar saques.
    """
    def __init__(self, valor):
        """
        Inicializa um saque com um valor.

        Args:
            valor (float): Valor do saque.
        """
        self._valor = valor

    @property
    def valor(self):
        """
        Retorna o valor do saque.
        """
        return self._valor

    def registrar(self, conta):
        """
        Registra o saque na conta.

        Args:
            conta (Conta): A conta onde o saque será registrado.
        """
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """
    Classe para representar depósitos.
    """
    def __init__(self, valor):
        """
        Inicializa um depósito com um valor.

        Args:
            valor (float): Valor do depósito.
        """
        self._valor = valor

    @property
    def valor(self):
        """
        Retorna o valor do depósito.
        """
        return self._valor

    def registrar(self, conta):
        """
        Registra o depósito na conta.

        Args:
            conta (Conta): A conta onde o depósito será registrado.
        """
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    """
    Exibe o menu principal do banco.
    """
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    """
    Filtra clientes por CPF.

    Args:
        cpf (str): CPF do cliente a ser filtrado.
        clientes (list): Lista de clientes.

    Returns:
        Cliente: O cliente com o CPF especificado, ou None se não encontrado.
    """
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    """
    Recupera a conta de um cliente (assume que o cliente tem apenas uma conta).

    Args:
        cliente (Cliente): O cliente cuja conta será recuperada.

    Returns:
        Conta: A conta do cliente, ou None se o cliente não tiver contas.
    """
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta (melhorar para permitir escolher)
    return cliente.contas[0]


def depositar(clientes):
    """
    Realiza um depósito em uma conta.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    """
    Realiza um saque em uma conta.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    """
    Exibe o extrato de uma conta.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    """
    Cria um novo cliente.
    """
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    """
    Cria uma nova conta corrente para um cliente existente.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    """
    Lista todas as contas existentes.
    """
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    """
    Função principal que executa o sistema bancário.
    """
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()