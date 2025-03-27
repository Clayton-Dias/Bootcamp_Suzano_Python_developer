# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open(r"E:\Cursos\Dio\Bootcamps\Suzano - Python Developer\Python\05 - Manipulação de arquivos\lorem.txt", "r")

print(arquivo.read())

print(arquivo.readline())

print(arquivo.readlines())

# tip
"""
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
"""