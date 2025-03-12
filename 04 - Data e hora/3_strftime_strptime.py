from datetime import datetime  # Importa a classe datetime para manipulação de data e hora

# Obtém a data e hora atuais
data_hora_atual = datetime.now()

# Define uma string representando uma data e hora em formato específico
data_hora_str = "2023-10-20 10:20"

# Define um formato de data para exibição no padrão brasileiro (dia/mês/ano e abreviação do dia da semana)
mascara_ptbr = "%d/%m/%Y %a"  

# Define um formato de data para leitura no padrão internacional (ano-mês-dia hora:minuto)
mascara_en = "%Y-%m-%d %H:%M"  

# Converte a data e hora atuais para string formatada no padrão brasileiro
print(data_hora_atual.strftime(mascara_ptbr))  

# Converte a string da data para um objeto datetime usando o formato definido (máscara_en)
data_convertida = datetime.strptime(data_hora_str, mascara_en)  

# Exibe o objeto datetime convertido
print(data_convertida)  

# Mostra o tipo do objeto para confirmar que é um datetime
print(type(data_convertida))  

