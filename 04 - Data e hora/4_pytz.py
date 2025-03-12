from datetime import datetime  # Importa a classe datetime para manipulação de data e hora
import pytz  # Biblioteca para manipulação de fusos horários
# pip install pytz


# Obtém a data e hora atuais no fuso horário de Oslo (Europa)
data = datetime.now(pytz.timezone("Europe/Oslo"))

# Obtém a data e hora atuais no fuso horário de São Paulo (Brasil)
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Exibe a data e hora em Oslo
print(data)

# Exibe a data e hora em São Paulo
print(data2)

