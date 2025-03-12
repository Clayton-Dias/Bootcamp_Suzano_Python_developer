def mensagem(nome):
    """
    Função que retorna uma mensagem de "Oi" com o nome fornecido.
    """
    print("executando mensagem")  # Imprime uma mensagem indicando que a função está sendo executada.
    return f"Oi {nome}"  # Retorna uma string formatada com a mensagem de saudação e o nome.


def mensagem_longa(nome):
    """
    Função que retorna uma mensagem de saudação mais longa com o nome fornecido.
    """
    print("executando mensagem longa")  # Imprime uma mensagem indicando que a função está sendo executada.
    return f"Olá tudo bem com você {nome}?"  # Retorna uma string formatada com a mensagem de saudação longa e o nome.


def executar(funcao, nome):
    """
    Função que recebe uma função e um nome como argumentos e executa a função com o nome.
    """
    print("executando executar")  # Imprime uma mensagem indicando que a função está sendo executada.
    return funcao(nome)  # Chama a função recebida como argumento, passando o nome, e retorna o resultado.


print(executar(mensagem, "Joao"))  # Chama a função 'executar' passando a função 'mensagem' e o nome "Joao". O resultado é impresso.
print(executar(mensagem_longa, "Joao")) # Chama a função 'executar' passando a função 'mensagem_longa' e o nome "Joao". O resultado é impresso.