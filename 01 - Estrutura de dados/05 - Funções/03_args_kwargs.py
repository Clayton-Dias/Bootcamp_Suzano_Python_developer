def exibir_poema(data_extenso, *args, **kwargs):
    # Junta todas as linhas do poema em um único texto, separando por quebras de linha
    texto = "\n".join(args)

    # Formata os metadados (kwargs) para exibição, transformando a chave em título e juntando com o valor
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    # Monta a mensagem final combinando a data, o texto do poema e os metadados
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    # Exibe a mensagem formatada
    print(mensagem)


# Chamando a função e passando os versos do poema como argumentos variáveis (*args)
# e os metadados como argumentos nomeados (**kwargs)
exibir_poema(
    "Domingo, 16 de Fevereiro de 2025",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

