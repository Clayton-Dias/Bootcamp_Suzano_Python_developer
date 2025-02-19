# Menu de opções para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# Inicialização das variáveis do sistema bancário
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo para saque por operação
extrato = ""  # Histórico das transações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Número máximo de saques permitidos por dia

# Loop principal para interação com o usuário
while True:

    opcao = input(menu)  # Exibe o menu e captura a opção escolhida pelo usuário

    if opcao == "d":  # Opção de depósito
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:  # Verifica se o valor informado é válido
            saldo += valor  # Atualiza o saldo com o valor depositado
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra o depósito no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro para valor inválido

    elif opcao == "s":  # Opção de saque
        valor = float(input("Informe o valor do saque: "))

        # Verificações para garantir que o saque pode ser realizado
        excedeu_saldo = valor > saldo  # Verifica se o saldo é suficiente
        excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite permitido
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número máximo de saques foi atingido

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")  # Mensagem caso o saldo seja insuficiente

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")  # Mensagem caso o saque ultrapasse o limite

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")  # Mensagem caso o usuário tenha atingido o limite de saques

        elif valor > 0:  # Verifica se o valor do saque é válido
            saldo -= valor  # Deduz o valor do saque do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra o saque no extrato
            numero_saques += 1  # Incrementa o contador de saques
        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro para valor inválido

    elif opcao == "e":  # Opção de extrato
        print("\n================ EXTRATO ================")
        # Exibe as movimentações se houver, caso contrário, informa que não houve movimentações
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("==========================================")

    elif opcao == "q":  # Opção para sair do programa
        break  # Sai do loop encerrando o programa

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro para opção inválida
