n = int(input("Digite um número n: "))

lista = []

for i in range(n):
    num = int(input(f"Digite o {i + 1}° número: "))
    lista.append(num)

soma_pares = 0
soma_impares = 0

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])

for i in range(len(lista)):
    if i % 2 == 0:
        soma_pares += lista[i]
    else:
        soma_impares += lista[i]

print(f"A soma dos números pares são: {soma_pares}")
print(f"A soma dos números ímpares são: {soma_impares}")    