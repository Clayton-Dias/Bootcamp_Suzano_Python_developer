def principal():
    """
    Função principal que demonstra o uso de funções internas.
    """
    print("executando a funcao principal")  # Imprime uma mensagem indicando que a função principal está sendo executada.

    def funcao_interna():
        """
        Função interna que só pode ser acessada dentro da função principal.
        """
        print("executando a funcao interna")  # Imprime uma mensagem indicando que a função interna está sendo executada.

    def funcao_2():
        """
        Outra função interna que só pode ser acessada dentro da função principal.
        """
        print("executando a funcao 2")  # Imprime uma mensagem indicando que a função 2 está sendo executada.

    funcao_interna()  # Chama a função interna 'funcao_interna'.
    funcao_2()  # Chama a função interna 'funcao_2'.


principal()  # Chama a função principal para iniciar a execução do programa.