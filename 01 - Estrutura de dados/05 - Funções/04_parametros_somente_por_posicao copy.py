def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # Função que exibe as informações de um carro
    # Os três primeiros parâmetros (modelo, ano, placa) devem ser passados apenas por posição
    print(modelo, ano, placa, marca, motor, combustivel)


# Chamando a função corretamente, passando os três primeiros argumentos por posição
# e os demais por nome (keyword arguments)
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Tentativa de chamada inválida: modelo, ano e placa devem ser passados por posição,
# mas aqui estão sendo passados como argumentos nomeados, o que resulta em erro.
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

