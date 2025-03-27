arquivo = open(
    r"E:\Cursos\Dio\Bootcamps\Suzano - Python Developer\Python\05 - Manipulação de arquivos\teste.txt", "w"
)
arquivo.write("1 - Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()
