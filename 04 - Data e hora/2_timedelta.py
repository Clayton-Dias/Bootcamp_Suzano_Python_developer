from datetime import date, datetime, timedelta  # Importa classes para manipulação de datas e horas

# Tipo do carro a ser reparado (P = Pequeno, M = Médio, G = Grande)
tipo_carro = "M"  

# Tempo estimado de reparo em dias para cada tipo de carro
tempo_pequeno = 30  
tempo_medio = 45  
tempo_grande = 60  

# Obtém a data e hora atuais
data_atual = datetime.now()  

# Verifica o tipo do carro e calcula a data estimada para conclusão do serviço
if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_pequeno)  # Adiciona 30 dias à data atual
    print(f"O carro chegou em: {data_atual} e ficará pronto em: {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)  # Adiciona 45 dias à data atual
    print(f"O carro chegou em: {data_atual} e ficará pronto em: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)  # Adiciona 60 dias à data atual
    print(f"O carro chegou em: {data_atual} e ficará pronto em: {data_estimada}")

# Calcula a data de ontem subtraindo um dia da data atual
print(date.today() - timedelta(days=1))  

# Cria um objeto datetime específico e subtrai 1 hora dele
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())  # Exibe somente o horário resultante

# Exibe a data atual sem a informação de horário
print(datetime.now().date())  

