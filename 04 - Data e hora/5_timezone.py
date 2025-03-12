from datetime import datetime, timedelta, timezone  # Importa as classes necessárias

# Cria um objeto de data e hora no fuso horário de Oslo (UTC+2)
data_oslo = datetime.now(timezone(timedelta(hours=2)))

# Cria um objeto de data e hora no fuso horário de São Paulo (UTC-3)
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

# Exibe a data e hora em Oslo
print(data_oslo)

# Exibe a data e hora em São Paulo
print(data_sao_paulo)
