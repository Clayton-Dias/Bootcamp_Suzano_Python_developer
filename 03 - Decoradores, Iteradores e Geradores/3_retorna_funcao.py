def calculadora(operacao):
    """
    Retorna uma função que realiza a operação especificada (+, -, *, /) entre dois números.

    Args:
        operacao: Uma string representando a operação desejada (+, -, *, /).

    Returns:
        Uma função que recebe dois números como argumentos e retorna o resultado da operação.
    """

    def soma(a, b):
        """
        Retorna a soma de a e b.
        """
        return a + b

    def sub(a, b):
        """
        Retorna a subtração de a por b.
        """
        return a - b

    def mul(a, b):
        """
        Retorna a multiplicação de a por b.
        """
        return a * b

    def div(a, b):
        """
        Retorna a divisão de a por b.
        """
        return a / b

    match operacao:
        case "+":
            return soma  # Retorna a função 'soma'
        case "-":
            return sub  # Retorna a função 'sub'
        case "*":
            return mul  # Retorna a função 'mul'
        case "/":
            return div  # Retorna a função 'div'


op = calculadora("+")  # 'op' agora se refere à função 'soma'
print(op(2, 2))  # Chama a função 'soma' com os argumentos 2 e 2, imprimindo o resultado (4).
op = calculadora("-")  # 'op' agora se refere à função 'sub'
print(op(2, 2))  # Chama a função 'sub' com os argumentos 2 e 2, imprimindo o resultado (0).
op = calculadora("*")  # 'op' agora se refere à função 'mul'
print(op(2, 2))  # Chama a função 'mul' com os argumentos 2 e 2, imprimindo o resultado (4).
op = calculadora("/")  # 'op' agora se refere à função 'div'
print(op(2, 2))  # Chama a função 'div' com os argumentos 2 e 2, imprimindo o resultado (1.0).