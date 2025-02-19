nome = "Guilherme Arthur de Carvalho"

# Exibe o primeiro caractere da string, índice 0
print(nome[0])  # 'G'

# Exibe o penúltimo caractere da string, índice -2
print(nome[-2])  # 'o'

# Exibe os primeiros 9 caracteres da string (do início até o índice 9, excluindo ele)
print(nome[:9])  # 'Guilherme'

# Exibe a partir do índice 10 até o final da string
print(nome[10:])  # 'Arthur de Carvalho'

# Exibe da posição 10 até a posição 16 (excluindo a posição 16)
print(nome[10:16])  # 'Arthur'

# Exibe da posição 10 até a posição 16, mas pegando um caractere sim, outro não (passo 2)
print(nome[10:16:2])  # 'Atu'

# Exibe todos os caracteres da string (do início ao fim)
print(nome[:])  # 'Guilherme Arthur de Carvalho'

# Exibe a string invertida (passo -1 no índice)
print(nome[::-1])  # 'olavraC ed ruhA emreliug'

