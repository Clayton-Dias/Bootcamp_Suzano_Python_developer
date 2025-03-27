import os # Importa o módulo os
import shutil # Importa o módulo shutil
from pathlib import Path # Importa a classe Path do módulo pathlib

ROOT_PATH = Path(__file__).parent # Obtém o diretório do arquivo atual

os.mkdir(ROOT_PATH / "novo-diretorio") # Cria um novo diretório

arquivo = open(ROOT_PATH / "novo.txt", "w") # Abre o arquivo novo.txt em modo de escrita
arquivo.write("Olá, mundo!") # Escreve no arquivo
arquivo.close() 

#os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") # Renomeia o arquivo novo.txt para alterado.txt

#os.remove(ROOT_PATH / "alterado.txt") # Remove o arquivo alterado.txt


shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt") # Move o arquivo novo.txt para o diretório novo-diretório
