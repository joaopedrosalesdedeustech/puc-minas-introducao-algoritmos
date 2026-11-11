def segundo_maior(valores):
    maior = valores[0]
    segundo = None

    for v in valores:
        if v > maior:
            segundo = maior
            maior = v
        elif v < maior and (segundo is None or v > segundo):
            segundo = v

    return segundo


print(segundo_maior([12, 7, 25, 3, 18]))
print(segundo_maior([9, 9, 4, 9]))        
print(segundo_maior([1, 2]))              