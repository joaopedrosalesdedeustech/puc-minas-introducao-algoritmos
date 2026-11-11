def sem_repeticao(valores):
    nova = []

    for i in range(len(valores)):
        if valores[i] not in nova:
            nova.append(valores[i])

    return nova

lista = [4, 7, 4, 2, 7, 7, 9, 2]

print(sem_repeticao(lista))