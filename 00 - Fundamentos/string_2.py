nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

# Dicionário com dados do nome e idade
dados = {"nome": "Guilherme", "idade": 28}

# Usando a formatação clássica com % para inserir as variáveis na string
print("Nome: %s Idade: %d" % (nome, idade))  # Nome: Guilherme Idade: 28

# Usando o método format() para inserir as variáveis na string
print("Nome: {} Idade: {}".format(nome, idade))  # Nome: Guilherme Idade: 28

# Especificando a ordem dos parâmetros usando o índice dentro do format
print("Nome: {1} Idade: {0}".format(idade, nome))  # Nome: Guilherme Idade: 28

# Repetindo e reordenando as variáveis dentro da string usando format
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))  # Nome: Guilherme Idade: 28 Nome: Guilherme Guilherme

# Usando os nomes das variáveis explicitamente dentro do format
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))  # Nome: Guilherme Idade: 28

# Usando dicionário e referenciando as chaves diretamente no format
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))  # Nome: Guilherme Idade: 28 Guilherme Guilherme 28

# Usando um dicionário com a sintaxe ** para descompactar as chaves diretamente no format
print("Nome: {nome} Idade: {idade}".format(**dados))  # Nome: Guilherme Idade: 28

# Usando f-strings (Python 3.6+) para formatação direta e simples de variáveis na string
print(f"Nome: {nome} Idade: {idade}")  # Nome: Guilherme Idade: 28

# Usando f-strings e formatando o saldo para exibir duas casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")  # Nome: Guilherme Idade: 28 Saldo: 45.44

# Usando f-strings e formatando o saldo para ter um total de 10 caracteres e uma casa decimal
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")  # Nome: Guilherme Idade: 28 Saldo:      45.4

