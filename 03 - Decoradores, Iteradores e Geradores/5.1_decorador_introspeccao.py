import functools


def meu_decorador(funcao):
    """
    Um decorador que usa functools.wraps para preservar metadados da função original.

    Args:
        funcao: A função a ser decorada.

    Returns:
        Uma nova função (o "envelope") que envolve a função original.
    """
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        """
        A função interna (envelope) que executa a função original e preserva seus metadados.
        """
        funcao(*args, **kwargs)  # Chama a função original com os argumentos recebidos

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


print(ola_mundo.__name__)  # Imprime o nome da função 'ola_mundo' (que será "ola_mundo" devido ao uso de @functools.wraps)
