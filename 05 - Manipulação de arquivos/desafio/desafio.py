import textwrap  # Importa o módulo textwrap para lidar com formatação de texto, como a remoção de recuos.
from abc import ABC, abstractclassmethod, abstractproperty  # Importa classes e decoradores do módulo abc para trabalhar com classes abstratas.
from datetime import datetime  # Importa a classe datetime do módulo datetime para trabalhar com datas e horas.
from pathlib import Path  # Importa a classe Path do módulo pathlib para trabalhar com caminhos de arquivos e diretórios de forma mais amigável.

ROOT_PATH = Path(__file__).parent  # Define o caminho da raiz do projeto como o diretório onde o arquivo atual está localizado.


class ContasIterador:
    """
    Iterador para a lista de contas, formatando a saída de cada conta.
    """
    def __init__(self, contas):
        """
        Inicializa o iterador com a lista de contas.

        Args:
            contas (list): A lista de contas a serem iteradas.
        """
        self.contas = contas  # Armazena a lista de contas no atributo self.contas.
        self._index = 0  # Inicializa o índice interno para controlar a iteração.

    def __iter__(self):
        """
        Retorna o próprio objeto iterador.
        """
        return self  # Retorna a instância atual da classe como o iterador.

    def __next__(self):
        """
        Retorna a próxima conta na lista.

        Raises:
            StopIteration: Se não houver mais contas na lista.

        Returns:
            str: A representação formatada da próxima conta.
        """
        try:
            conta = self.contas[self._index]  # Obtém a conta atual da lista usando o índice.
            self._index += 1  # Incrementa o índice para a próxima iteração.
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """  # Retorna uma string formatada com informações da conta.
        except IndexError:
            raise StopIteration  # Levanta a exceção StopIteration quando não há mais contas na lista.
        finally:
            self._index += 1  # Incrementa o índice para a próxima iteração, garantindo que seja sempre incrementado, mesmo que ocorra um erro.


class Cliente:
    """
    Classe base para clientes do banco.
    """
    def __init__(self, endereco):
        """
        Inicializa um cliente com um endereço e uma lista de contas.

        Args:
            endereco (str): O endereço do cliente.
        """
        self.endereco = endereco  # Armazena o endereço do cliente.
        self.contas = []  # Inicializa uma lista vazia para armazenar as contas do cliente.
        self.indice_conta = 0  # Inicializa um índice para controlar as contas do cliente (não utilizado no código atual).

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação em uma conta específica, verificando o limite de transações diárias.

        Args:
            conta (Conta): A conta onde a transação será realizada.
            transacao (Transacao): A transação a ser realizada.
        """
        if len(conta.historico.transacoes_do_dia()) >= 2:  # Verifica se o número de transações do dia já atingiu o limite.
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")  # Imprime mensagem de erro se o limite for excedido.
            return  # Retorna sem realizar a transação.

        transacao.registrar(conta)  # Chama o método registrar da transação para processá-la na conta.

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.

        Args:
            conta (Conta): A conta a ser adicionada.
        """
        self.contas.append(conta)  # Adiciona a conta à lista de contas do cliente.


class PessoaFisica(Cliente):
    """
    Classe para representar clientes pessoa física, herda de Cliente.
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        """
        Inicializa um cliente pessoa física com informações adicionais.

        Args:
            nome (str): O nome completo do cliente.
            data_nascimento (str): A data de nascimento do cliente.
            cpf (str): O CPF do cliente.
            endereco (str): O endereço do cliente.
        """
        super().__init__(endereco)  # Chama o construtor da classe pai (Cliente).
        self.nome = nome  # Armazena o nome do cliente.
        self.data_nascimento = data_nascimento  # Armazena a data de nascimento do cliente.
        self.cpf = cpf  # Armazena o CPF do cliente.

    def __repr__(self) -> str:
        """
        Retorna uma representação string da instância da classe.
        """
        return f"<{self.__class__.__name__}: ('{self.nome}', '{self.cpf}')>"  # Retorna uma string com o nome da classe, nome e CPF do cliente.


class Conta:
    """
    Classe base para contas bancárias.
    """
    def __init__(self, numero, cliente):
        """
        Inicializa uma conta bancária com saldo, número, agência, cliente e histórico.

        Args:
            numero (str): O número da conta.
            cliente (Cliente): O cliente titular da conta.
        """
        self._saldo = 0  # Inicializa o saldo da conta como 0.
        self._numero = numero  # Armazena o número da conta.
        self._agencia = "0001"  # Define a agência da conta como "0001".
        self._cliente = cliente  # Armazena o cliente titular da conta.
        self._historico = Historico()  # Inicializa o histórico de transações da conta.

    @classmethod
    def nova_conta(cls, cliente, numero):
        """
        Cria uma nova instância da classe Conta.

        Args:
            cliente (Cliente): O cliente titular da conta.
            numero (str): O número da conta.

        Returns:
            Conta: Uma nova instância da classe Conta.
        """
        return cls(numero, cliente)  # Retorna uma nova instância da classe Conta com o número e cliente especificados.

    @property
    def saldo(self):
        """
        Retorna o saldo da conta.
        """
        return self._saldo  # Retorna o saldo da conta.

    @property
    def numero(self):
        """
        Retorna o número da conta.
        """
        return self._numero  # Retorna o número da conta.

    @property
    def agencia(self):
        """
        Retorna a agência da conta.
        """
        return self._agencia  # Retorna a agência da conta.

    @property
    def cliente(self):
        """
        Retorna o cliente titular da conta.
        """
        return self._cliente  # Retorna o cliente titular da conta.

    @property
    def historico(self):
        """
        Retorna o histórico de transações da conta.
        """
        return self._historico  # Retorna o histórico de transações da conta.

    def sacar(self, valor):
        """
        Realiza um saque na conta.

        Args:
            valor (float): O valor a ser sacado.

        Returns:
            bool: True se o saque foi realizado com sucesso, False caso contrário.
        """
        saldo = self.saldo  # Obtém o saldo atual da conta.
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo disponível.

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")  # Imprime mensagem de erro se o saldo for insuficiente.

        elif valor > 0:
            self._saldo -= valor  # Decrementa o saldo da conta pelo valor do saque.
            print("\n=== Saque realizado com sucesso! ===")  # Imprime mensagem de sucesso se o saque for realizado.
            return True  # Retorna True para indicar que o saque foi realizado com sucesso.

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Imprime mensagem de erro se o valor for inválido.

        return False  # Retorna False para indicar que o saque falhou.

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): O valor a ser depositado.

        Returns:
            bool: True se o depósito foi realizado com sucesso, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor  # Incrementa o saldo da conta pelo valor do depósito.
            print("\n=== Depósito realizado com sucesso! ===")  # Imprime mensagem de sucesso se o depósito for realizado.
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Imprime mensagem de erro se o valor for inválido.
            return False  # Retorna False para indicar que o depósito falhou.

        return True  # Retorna True para indicar que o depósito foi realizado com sucesso.


class ContaCorrente(Conta):
    """
    Classe para contas correntes, herda de Conta.
    """
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        """
        Inicializa uma conta corrente com número, cliente, limite e limite de saques.

        Args:
            numero (str): O número da conta.
            cliente (Cliente): O cliente titular da conta.
            limite (float): O limite de crédito da conta.
            limite_saques (int): O número máximo de saques permitidos na conta.
        """
        super().__init__(numero, cliente)  # Chama o construtor da classe pai (Conta).
        self._limite = limite  # Armazena o limite de crédito da conta.
        self._limite_saques = limite_saques  # Armazena o limite de saques da conta.

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        """
        Cria uma nova instância da classe ContaCorrente com limite e limite de saques personalizados.

        Args:
            cliente (Cliente): O cliente titular da conta.
            numero (str): O número da conta.
            limite (float): O limite de crédito da conta.
            limite_saques (int): O número máximo de saques permitidos na conta.

        Returns:
            ContaCorrente: Uma nova instância da classe ContaCorrente.
        """
        return cls(numero, cliente, limite, limite_saques)  # Retorna uma nova instância da classe ContaCorrente com os parâmetros especificados.

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente, verificando o limite e o número de saques.

        Args:
            valor (float): O valor a ser sacado.

        Returns:
            bool: True se o saque foi realizado com sucesso, False caso contrário.
        """
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )  # Calcula o número de saques já realizados na conta.

        excedeu_limite = valor > self._limite  # Verifica se o valor do saque excede o limite de crédito.
        excedeu_saques = numero_saques >= self._limite_saques  # Verifica se o número de saques excede o limite de saques.

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")  # Imprime mensagem de erro se o limite for excedido.

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")  # Imprime mensagem de erro se o limite de saques for excedido.

        else:
            return super().sacar(valor)  # Chama o método sacar da classe pai (Conta) se as verificações passarem.

        return False  # Retorna False para indicar que o saque falhou.

    def __repr__(self):
        """
        Retorna uma representação string da instância da classe (para debugging).
        """
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"  # Retorna uma string com o nome da classe, agência, número e nome do cliente.

    def __str__(self):
        """
        Retorna uma representação string da conta corrente (para exibição).
        """
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """  # Retorna uma string formatada com informações da conta corrente.


class Historico:
    """
    Classe para armazenar o histórico de transações de uma conta.
    """
    def __init__(self):
        """
        Inicializa o histórico de transações com uma lista vazia.
        """
        self._transacoes = []  # Inicializa uma lista vazia para armazenar as transações.

    @property
    def transacoes(self):
        """
        Retorna a lista de transações.
        """
        return self._transacoes  # Retorna a lista de transações.

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma transação ao histórico.

        Args:
            transacao (Transacao): A transação a ser adicionada.
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Obtém o nome da classe da transação.
                "valor": transacao.valor,  # Obtém o valor da transação.
                "data": datetime.strftime("%d-%m-%Y %H:%M:%S"),  # Obtém a data e hora atual formatada.
            }
        )  # Adiciona um dicionário com informações da transação à lista de transações.

    def gerar_relatorio(self, tipo_transacao=None):
        """
        Gera um relatório de transações filtrado por tipo.

        Args:
            tipo_transacao (str, optional): O tipo de transação a ser filtrado. Defaults to None.

        Yields:
            dict: Um dicionário com informações da transação.
        """
        for transacao in self._transacoes:  # Itera sobre a lista de transações.
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():  # Verifica se o tipo da transação corresponde ao filtro.
                yield transacao  # Retorna a transação se corresponder ao filtro (usa yield para ser um gerador).

    def transacoes_do_dia(self):
        """
        Retorna uma lista de transações realizadas no dia atual (UTC).

        Returns:
            list: Uma lista de dicionários com informações das transações do dia.
        """
        data_atual = datetime.utcnow().date()  # Obtém a data atual (UTC).
        transacoes = []  # Inicializa uma lista vazia para armazenar as transações do dia.
        for transacao in self._transacoes:  # Itera sobre a lista de transações.
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()  # Converte a string da data da transação para um objeto date.
            if data_atual == data_transacao:  # Verifica se a data da transação é igual à data atual.
                transacoes.append(transacao)  # Adiciona a transação à lista de transações do dia.
        return transacoes  # Retorna a lista de transações do dia.


class Transacao(ABC):
    """
    Classe abstrata para transações bancárias.
    """
    @property
    @abstractproperty
    def valor(self):
        """
        Método abstrato para retornar o valor da transação.
        """
        pass  # Método abstrato, deve ser implementado nas subclasses.

    @abstractclassmethod
    def registrar(self, conta):
        """
        Método abstrato para registrar a transação em uma conta.
        """
        pass  # Método abstrato, deve ser implementado nas subclasses.


class Saque(Transacao):
    """
    Classe para representar saques, herda de Transacao.
    """
    def __init__(self, valor):
        """
        Inicializa um saque com um valor.

        Args:
            valor (float): O valor do saque.
        """
        self._valor = valor  # Armazena o valor do saque.

    @property
    def valor(self):
        """
        Retorna o valor do saque.
        """
        return self._valor  # Retorna o valor do saque.

    def registrar(self, conta):
        """
        Registra o saque em uma conta.

        Args:
            conta (Conta): A conta onde o saque será registrado.
        """
        sucesso_transacao = conta.sacar(self.valor)  # Realiza o saque na conta.

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona a transação ao histórico da conta se o saque for bem-sucedido.


class Deposito(Transacao):
    """
    Classe para representar depósitos, herda de Transacao.
    """
    def __init__(self, valor):
        """
        Inicializa um depósito com um valor.

        Args:
            valor (float): O valor do depósito.
        """
        self._valor = valor  # Armazena o valor do depósito.

    @property
    def valor(self):
        """
        Retorna o valor do depósito.
        """
        return self._valor  # Retorna o valor do depósito.

    def registrar(self, conta):
        """
        Registra o depósito em uma conta.

        Args:
            conta (Conta): A conta onde o depósito será registrado.
        """
        sucesso_transacao = conta.depositar(self.valor)  # Realiza o depósito na conta.

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona a transação ao histórico da conta se o depósito for bem-sucedido.


def log_transacao(func):
    """
    Decorador para registrar o início e fim de uma transação em um arquivo de log.

    Args:
        func (function): A função a ser decorada.

    Returns:
        function: A função decorada.
    """
    def envelope(*args, **kwargs):
        """
        Função interna que registra o início e fim da transação em um arquivo de log.

        Args:
            *args: Argumentos posicionais da função original.
            **kwargs: Argumentos nomeados da função original.

        Returns:
            any: O resultado da função original.
        """
        resultado = func(*args, **kwargs)  # Chama a função original.
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtém a data e hora atual formatada.
        
        with open(ROOT_PATH / "log.txt", "a") as arquivo:  # Abre o arquivo de log em modo de adição.
            arquivo.write(
                f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. "
                f"Retornou {resultado}\n"  # Escreve informações sobre a execução da função no arquivo de log.
            )
        return resultado  # Retorna o resultado da função original.

    return envelope  # Retorna a função interna (envelope).


def menu():
    """
    Exibe o menu de opções para o usuário.

    Returns:
        str: A opção selecionada pelo usuário.
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
    => """  # Define a string com o menu de opções.
    return input(textwrap.dedent(menu))  # Exibe o menu e retorna a entrada do usuário.


def filtrar_cliente(cpf, clientes):
    """
    Filtra a lista de clientes pelo CPF.

    Args:
        cpf (str): O CPF do cliente a ser filtrado.
        clientes (list): A lista de clientes.

    Returns:
        Cliente: O cliente com o CPF especificado, ou None se não encontrado.
    """
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]  # Filtra a lista de clientes pelo CPF.
    return clientes_filtrados[0] if clientes_filtrados else None  # Retorna o primeiro cliente encontrado ou None se não houver correspondência.


def recuperar_conta_cliente(cliente):
    """
    Recupera a primeira conta de um cliente.

    Args:
        cliente (Cliente): O cliente do qual a conta será recuperada.

    Returns:
        Conta: A primeira conta do cliente, ou None se o cliente não tiver contas.
    """
    if not cliente.contas:  # Verifica se o cliente não tem contas.
        print("\n@@@ Cliente não possui conta! @@@")  # Imprime mensagem de erro se o cliente não tiver contas.
        return  # Retorna se o cliente não tiver contas.

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]  # Retorna a primeira conta do cliente.


@log_transacao
def depositar(clientes):
    """
    Realiza um depósito em uma conta.

    Args:
        clientes (list): A lista de clientes.
    """
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente.
    cliente = filtrar_cliente(cpf, clientes)  # Filtra a lista de clientes pelo CPF.

    if not cliente:  # Verifica se o cliente foi encontrado.
        print("\n@@@ Cliente não encontrado! @@@")  # Imprime mensagem de erro se o cliente não for encontrado.
        return  # Retorna se o cliente não for encontrado.

    valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito.
    transacao = Deposito(valor)  # Cria um objeto Deposito com o valor informado.

    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente.
    if not conta:  # Verifica se a conta foi encontrada.
        return  # Retorna se a conta não for encontrada.

    cliente.realizar_transacao(conta, transacao)  # Realiza a transação de depósito na conta.


@log_transacao
def sacar(clientes):
    """
    Realiza um saque em uma conta.

    Args:
        clientes (list): A lista de clientes.
    """
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente.
    cliente = filtrar_cliente(cpf, clientes)  # Filtra a lista de clientes pelo CPF.

    if not cliente:  # Verifica se o cliente foi encontrado.
        print("\n@@@ Cliente não encontrado! @@@")  # Imprime mensagem de erro se o cliente não for encontrado.
        return  # Retorna se o cliente não for encontrado.

    valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque.
    transacao = Saque(valor)  # Cria um objeto Saque com o valor informado.

    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente.
    if not conta:  # Verifica se a conta foi encontrada.
        return  # Retorna se a conta não for encontrada.

    cliente.realizar_transacao(conta, transacao)  # Realiza a transação de saque na conta.


@log_transacao
def exibir_extrato(clientes):
    """
    Exibe o extrato de uma conta.

    Args:
        clientes (list): A lista de clientes.
    """
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente.
    cliente = filtrar_cliente(cpf, clientes)  # Filtra a lista de clientes pelo CPF.

    if not cliente:  # Verifica se o cliente foi encontrado.
        print("\n@@@ Cliente não encontrado! @@@")  # Imprime mensagem de erro se o cliente não for encontrado.
        return  # Retorna se o cliente não for encontrado.

    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente.
    if not conta:  # Verifica se a conta foi encontrada.
        return  # Retorna se a conta não for encontrada.

    print("\n================ EXTRATO ================")  # Imprime cabeçalho do extrato.
    extrato = ""  # Inicializa a string do extrato.
    tem_transacao = False  # Inicializa a variável para verificar se há transações.
    for transacao in conta.historico.gerar_relatorio():  # Itera sobre as transações utilizando um gerador.
        tem_transacao = True  # Define a variável como True se houver transações.
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"  # Formata e adiciona a transação à string do extrato.

    if not tem_transacao:  # Verifica se não há transações.
        extrato = "Não foram realizadas movimentações"  # Define a mensagem do extrato se não houver transações.

    print(extrato)  # Imprime o extrato.
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")  # Imprime o saldo da conta.
    print("==========================================")  # Imprime o rodapé do extrato.


@log_transacao
def criar_cliente(clientes):
    """
    Cria um novo cliente.

    Args:
        clientes (list): A lista de clientes.
    """
    cpf = input("Informe o CPF (somente número): ")  # Solicita o CPF do cliente.
    cliente = filtrar_cliente(cpf, clientes)  # Filtra a lista de clientes pelo CPF.

    if cliente:  # Verifica se já existe um cliente com o mesmo CPF.
        print("\n@@@ Já existe cliente com esse CPF! @@@")  # Imprime mensagem de erro se já existir um cliente com o mesmo CPF.
        return  # Retorna se já existir um cliente com o mesmo CPF.

    nome = input("Informe o nome completo: ")  # Solicita o nome completo do cliente.
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")  # Solicita a data de nascimento do cliente.
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")  # Solicita o endereço do cliente.

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)  # Cria um objeto PessoaFisica com os dados informados.

    clientes.append(cliente)  # Adiciona o cliente à lista de clientes.

    print("\n=== Cliente criado com sucesso! ===")  # Imprime mensagem de sucesso.


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    """
    Cria uma nova conta corrente para um cliente.

    Args:
        numero_conta (int): O número da conta a ser criada.
        clientes (list): A lista de clientes.
        contas (list): A lista de contas.
    """
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente.
    cliente = filtrar_cliente(cpf, clientes)  # Filtra a lista de clientes pelo CPF.

    if not cliente:  # Verifica se o cliente foi encontrado.
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")  # Imprime mensagem de erro se o cliente não for encontrado.
        return  # Retorna se o cliente não for encontrado.

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)  # Cria uma nova conta corrente para o cliente.
    contas.append(conta)  # Adiciona a conta à lista de contas.
    cliente.contas.append(conta)  # Adiciona a conta à lista de contas do cliente.

    print("\n=== Conta criada com sucesso! ===")  # Imprime mensagem de sucesso.


def listar_contas(contas):
    """
    Lista as contas utilizando o iterador ContasIterador.

    Args:
        contas (list): A lista de contas a serem listadas.
    """
    for conta_str in ContasIterador(contas):  # Itera sobre as contas utilizando o iterador ContasIterador.
        print("=" * 100)  # Imprime uma linha de separação.
        print(textwrap.dedent(conta_str))  # Imprime as informações da conta removendo o recuo.


def main():
    """
    Função principal que executa o sistema bancário.
    """
    clientes = []  # Inicializa uma lista vazia para armazenar os clientes.
    contas = []  # Inicializa uma lista vazia para armazenar as contas.

    while True:  # Inicia um loop infinito.
        opcao = menu()  # Exibe o menu e obtém a opção selecionada pelo usuário.

        if opcao == "d":  # Verifica se a opção selecionada é "d" (depositar).
            depositar(clientes)  # Chama a função depositar.

        elif opcao == "s":  # Verifica se a opção selecionada é "s" (sacar).
            sacar(clientes)  # Chama a função sacar.

        elif opcao == "e":  # Verifica se a opção selecionada é "e" (extrato).
            exibir_extrato(clientes)  # Chama a função exibir_extrato.

        elif opcao == "nu":  # Verifica se a opção selecionada é "nu" (novo usuário).
            criar_cliente(clientes)  # Chama a função criar_cliente.

        elif opcao == "nc":  # Verifica se a opção selecionada é "nc" (nova conta).
            numero_conta = len(contas) + 1  # Calcula o número da nova conta.
            criar_conta(numero_conta, clientes, contas)  # Chama a função criar_conta.

        elif opcao == "lc":  # Verifica se a opção selecionada é "lc" (listar contas).
            listar_contas(contas)  # Chama a função listar_contas.

        elif opcao == "q":  # Verifica se a opção selecionada é "q" (sair).
            break  # Sai do loop infinito.

        else:  # Se a opção selecionada não for válida.
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")  # Imprime mensagem de erro.


main()  # Chama a função principal para iniciar o sistema.