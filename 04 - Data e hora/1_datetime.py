from datetime import date, datetime, time  # Importa as classes date, datetime e time do módulo datetime

# Criando uma data específica (10 de julho de 2023)
data = date(2023, 7, 10)
print(data)  # Saída: 2023-07-10

# Obtendo a data atual do sistema
print(date.today())  # Exibe a data atual no formato YYYY-MM-DD

# Criando um objeto datetime com uma data específica (10 de julho de 2023, sem horário definido)
data_hora = datetime(2023, 7, 10)
print(data_hora)  # Saída: 2023-07-10 00:00:00 (O horário padrão é meia-noite)

# Obtendo a data e hora atuais do sistema
print(datetime.today())  # Exibe a data e hora atuais no formato YYYY-MM-DD HH:MM:SS

# Criando um horário específico (10 horas e 20 minutos)
hora = time(10, 20, 0)
print(hora)  # Saída: 10:20:00
