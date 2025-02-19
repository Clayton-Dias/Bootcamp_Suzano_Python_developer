nome = "gUIlherME"

print(nome.upper()) # GUILHERME
print(nome.lower()) # guilherme
print(nome.title()) # Guilherme
print(nome.capitalize()) # Guilherme
print(nome.swapcase()) # GuiLHERme

texto = "  Olá mundo!    "

print(texto + ".") # "  Olá mundo!    ."
print(texto.strip() + ".")  # "Olá mundo!."
print(texto.rstrip() + ".") # "  Olá mundo!."
print(texto.lstrip() + ".") # "Olá mundo!    ."

menu = "Python"

print("####" + menu + "####") # ####Python####
print(menu.center(14)) # "   Python    "
print(menu.center(14, "#")) # "###Python####"
print(menu.ljust(14, "-")) # "Python-------"
print(menu.rjust(14, "-")) # "-------Python"
print("-".join(menu)) # "P-y-t-h-o-n"
print(menu.split("t")) # ['Py', 'hon']
print(menu.partition("t")) # ('Py', 't', 'hon')
print(menu.replace("t", "T")) # PyThon
print(menu.replace("t", "T", 1)) # PyThon
print(menu.find("t")) # 2
print(menu.find("T")) # -1
print(menu.index("t")) # 2
# print(menu.index("T")) # ValueError: substring not found
print(menu.count("t")) # 1
