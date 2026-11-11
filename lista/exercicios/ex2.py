def filtrar_palavras(palavras, tamanho):
    nova = []

    for i in palavras:
        if len(i) > tamanho:
            nova.append(i)

    return nova


lista = []

tamanho = int(input("Digite o tamanho: "))

palavra = ""

while palavra != "fim":
    palavra = input("Digite uma palavra: ")

    lista.append(palavra)

print(filtrar_palavras(lista, tamanho))