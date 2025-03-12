# Title: Decoradores com argumentos

def meu_decorador(funcao):
    """
    Um decorador que adiciona comportamento antes e depois da execução de uma função.

    Args:
        funcao: A função a ser decorada.

    Returns:
        Uma nova função (o "envelope") que envolve a função original.
    """
    def envelope(*args, **kwargs):
        """
        A função interna (envelope) que executa o comportamento adicional e a função original,
        passando os argumentos recebidos para a função original.
        """
        print("faz algo antes de executar")  # Executa algo antes da função original
        funcao(*args, **kwargs)  # Chama a função original com os argumentos recebidos
        print("faz algo depois de executar")  # Executa algo depois da função original

    return envelope  # Retorna a função 'envelope'


@meu_decorador  # Aplica o decorador 'meu_decorador' à função 'ola_mundo'
def ola_mundo(nome, outro_argumento):
    """
    Uma função que imprime "Olá mundo {nome}!".

    Args:
        nome: O nome a ser incluído na saudação.
        outro_argumento: Um outro argumento (não utilizado diretamente, apenas para demonstrar a passagem de múltiplos argumentos)
    """
    print(f"Olá mundo {nome}!")  # Imprime "Olá mundo {nome}!"


ola_mundo("João", 1000)  # Chama a função 'ola_mundo' (que agora está decorada) com os argumentos "João" e 1000
