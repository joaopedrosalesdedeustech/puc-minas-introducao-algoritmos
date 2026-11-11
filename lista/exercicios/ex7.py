n = int(input("Digite um número inteiro: "))

lista = []

for i in range(n):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    lista.append(nota)

media = 0
acima = []
abaixo = []

soma = 0
pos = 0
maior = lista[0]

for l in range(1, len(lista)):
    if lista[l] > maior:
        maior = lista[l]
        pos = l

for k in range(len(lista)):
    soma += lista[k]

media = soma / len(lista)

for j in lista:
    if j > media:
        acima.append(j)
    elif j < media:
        abaixo.append(j)

print("Média: ", media)
print("Acima: ", acima)
print("Abaixo: ", abaixo)
print("Posição da maior: ", pos)