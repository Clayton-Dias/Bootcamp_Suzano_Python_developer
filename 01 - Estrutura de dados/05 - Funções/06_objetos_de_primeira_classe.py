def somar(a, b):
    # Função que retorna a soma de dois números
    return a + b


def exibir_resultado(a, b, funcao):
    # Chama a função passada como argumento e armazena o resultado
    resultado = funcao(a, b)
    
    # Exibe o resultado da operação
    print(f"O resultado da operação {a} + {b} = {resultado}")


# Chamando a função exibir_resultado, passando a função somar como argumento
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20



# Atribuindo a função 'somar' a uma variável 'op'
op = somar
# Chamando a função através da variável 'op'
print(op(1, 36))  # Saída: 37
