palavras = []
arquivo = open("doces.txt", "r")
for linha in arquivo:
    palavras.append(linha.strip())

print(palavras)