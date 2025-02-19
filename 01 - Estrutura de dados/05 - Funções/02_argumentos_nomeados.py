def salvar_carro(marca, modelo, ano, placa):
    # Função que simula o salvamento de um carro no banco de dados
    # e imprime uma mensagem de sucesso.
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Chamando a função com argumentos posicionais
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Chamando a função com argumentos nomeados (keyword arguments)
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Chamando a função utilizando desempacotamento de dicionário (**kwargs)
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

