def eh_espelhada(valores):
    n = len(valores)
    meio = n // 2

    esq = meio - 1
    if n % 2 == 0:
        dir = meio
    else:
        dir = meio + 1

    while esq >= 0:
        if valores[esq] != valores[dir]:
            return False
        esq -= 1
        dir += 1

    return True


print(eh_espelhada([1, 4, 9, 4, 1]))
print(eh_espelhada([7, 2, 2, 7])) 
print(eh_espelhada([3, 5, 8, 3]))
print(eh_espelhada([6]))
print(eh_espelhada([]))                  