def meu_decorador(funcao):
    """
    Um decorador que adiciona comportamento antes e depois da execução de uma função.

    Args:
        funcao: A função a ser decorada.

    Returns:
        Uma nova função (o "envelope") que envolve a função original.
    """
    def envelope():
        """
        A função interna (envelope) que executa o comportamento adicional e a função original.
        """
        print("faz algo antes de executar")  # Executa algo antes da função original
        funcao()  # Chama a função original
        print("faz algo depois de executar")  # Executa algo depois da função original

    return envelope  # Retorna a função 'envelope'


def ola_mundo():
    """
    Uma função simples que imprime "Olá mundo!".
    """
    print("Olá mundo!")  # Imprime "Olá mundo!"


ola_mundo = meu_decorador(ola_mundo)  # Aplica o decorador 'meu_decorador' à função 'ola_mundo'.
ola_mundo()  # Chama a função 'ola_mundo', que agora está decorada.