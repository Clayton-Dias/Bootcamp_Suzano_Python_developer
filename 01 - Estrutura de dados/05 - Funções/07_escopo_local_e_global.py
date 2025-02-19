salario = 2000  # Definição da variável global salário


def salario_bonus(bonus):
    global salario  # Indica que estamos modificando a variável global salario
    salario += bonus  # Adiciona o bônus ao salário
    return salario  # Retorna o novo valor do salário


# Chamando a função e adicionando um bônus de 500 ao salário
# salario_bonus(500)  # 2500
print(salario_bonus(500))
print(salario_bonus(500))
print(salario_bonus(500))
print(salario_bonus(500))
print(salario)