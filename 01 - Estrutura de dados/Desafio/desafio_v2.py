import textwrap  # Importa o módulo textwrap para formatar textos

def menu():
    """
    Exibe o menu principal do sistema e retorna a opção escolhida pelo usuário.
    """
    menu = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))  # Remove espaços desnecessários do início do menu usando textwrap.dedent


def depositar(saldo, valor, extrato, /):
    """
    Realiza um depósito na conta.
    """
    if valor <= 0:  # Verifica se o valor é inválido (negativo ou zero)
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return saldo, extrato  # Retorna sem modificar os valores

    saldo += valor  # Adiciona o valor ao saldo
    extrato.append(f"Depósito: R$ {valor:.2f}")  # Registra a transação no extrato formatando o valor com duas casas decimais
    print("\n=== Depósito realizado com sucesso! ===")
    return saldo, extrato  # Retorna os valores atualizados


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque da conta, respeitando saldo, limite e número de saques permitidos.
    * indica que todos os argumentos após ele devem ser nomeados (keyword-only arguments).
    """
    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    elif valor > saldo:  # Se o valor do saque for maior que o saldo disponível
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:  # Se o valor do saque for maior que o limite permitido
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif numero_saques >= limite_saques:  # Se o usuário já atingiu o limite de saques diários
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    else:
        saldo -= valor  # Subtrai o valor do saldo
        extrato.append(f"Saque: R$ {valor:.2f}")  # Registra a transação no extrato
        numero_saques += 1  # Incrementa o número de saques realizados
        print("\n=== Saque realizado com sucesso! ===")

    return saldo, extrato, numero_saques  # Retorna os valores atualizados


def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    / indica que todos os argumentos antes dele devem ser posicionais (positional-only arguments).
    * indica que todos os argumentos após ele devem ser nomeados (keyword-only arguments).
    """
    print("\n================ EXTRATO ================")
    print("\n".join(extrato) if extrato else "Não foram realizadas movimentações.")  
    # Se houver transações, exibe todas unidas por "\n"; caso contrário, exibe uma mensagem padrão
    print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual formatando o valor com duas casas decimais
    print("==========================================")


def criar_usuario(usuarios):
    """
    Cria um novo usuário no sistema.
    """
    cpf = input("Informe o CPF (somente números): ")

    # Verifica se o CPF já está cadastrado na lista de usuários
    if any(usuario["cpf"] == cpf for usuario in usuarios):  # Utiliza any() para verificar se algum usuário possui o mesmo CPF
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    # Solicita os dados do novo usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Adiciona o usuário à lista
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  # Cria um dicionário com os dados do usuário e adiciona à lista
    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma nova conta bancária associada a um usuário existente.
    """
    cpf = input("Informe o CPF do usuário: ")
    
    # Busca o usuário pelo CPF usando `next()` e um generator expression
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None) # Usa next() para obter o primeiro usuário que corresponde ao CPF ou None se não encontrar

    if not usuario:  # Se o usuário não for encontrado
        print("\n@@@ Usuário não encontrado, criação de conta cancelada! @@@")
        return None

    print("\n=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} # Retorna um dicionário contendo os dados da nova conta


def listar_contas(contas):
    """
    Lista todas as contas cadastradas no sistema.
    """
    if not contas:  # Se a lista de contas estiver vazia
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    for conta in contas:  # Percorre a lista de contas e exibe os dados de cada uma
        print("=" * 50)
        print(f"Agência: {conta['agencia']}")  # Exibe a agência da conta
        print(f"C/C: {conta['numero_conta']}")  # Exibe o número da conta
        print(f"Titular: {conta['usuario']['nome']}")  # Exibe o nome do titular da conta
        print("=" * 50)


def main():
    """
    Função principal do sistema bancário. Gerencia o fluxo de operações e interações com o usuário.
    """
    LIMITE_SAQUES = 3  # Limite de saques diários
    AGENCIA = "0001"  # Número da agência padrão

    saldo = 0  # Saldo inicial da conta
    limite = 500  # Limite máximo por saque
    extrato = []  # Lista para armazenar as transações
    numero_saques = 0  # Contador de saques realizados
    usuarios = []  # Lista de usuários cadastrados
    contas = []  # Lista de contas cadastradas

    while True:  # Loop principal do sistema
        opcao = menu()  # Exibe o menu e recebe a opção do usuário

        if opcao == "d":  # Se a opção for "d" (depositar)
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)  # Chama a função depositar e atualiza saldo e extrato

        elif opcao == "s":  # Se a opção for "s" (sacar)
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(  # Chama a função sacar e atualiza saldo, extrato e numero_saques
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":  # Se a opção for "e" (extrato)
            exibir_extrato(saldo, extrato=extrato)  # Chama a função exibir_extrato

        elif opcao == "nu":  # Se a opção for "nu" (novo usuário)
            criar_usuario(usuarios)  # Chama a função criar_usuario

        elif opcao == "nc":  # Se a opção for "nc" (nova conta)
            numero_conta = len(contas) + 1  # Gera um novo número de conta sequencial
            conta = criar_conta(AGENCIA, numero_conta, usuarios)  # Chama a função criar_conta
            if conta:  # Se a conta foi criada com sucesso, adiciona à lista de contas
                contas.append(conta)

        elif opcao == "lc":  # Se a opção for "lc" (listar contas)
            listar_contas(contas)  # Chama a função listar_contas

        elif opcao == "q":  # Se a opção for "q" (sair)
            print("\n=== Obrigado por utilizar o sistema bancário! ===")
            break  # Sai do loop encerrando o programa

        else:  # Se a opção for inválida
            print("\n@@@ Operação inválida! Tente novamente. @@@")


# Inicia o programa
main()