def mesclar(lista1, lista2):
    nova = []

    for i in range(len(lista1)):
        nova.append(lista1[i])

    for j in range(len(lista2)):
        nova.append(lista2[j])

    temp = 0

    for k in range(len(nova)):
        for l in range(k + 1, len(nova)):
            if nova[k] > nova[l]:
                temp = nova[l]
                nova[l] = nova[k]
                nova[k] = temp

    return nova

lista1 = [2, 5, 9, 14]
lista2 = [1, 5, 6]

print(mesclar(lista1, lista2))
