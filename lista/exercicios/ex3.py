def alterna_paridade(valores):

    for i in range(1, len(valores)):
        if valores[i] % 2 == 0 and valores[i - 1] % 2 == 0 or valores[i] % 2 == 1 and valores[i - 1] % 2 == 1:
            return False

    return True

print(alterna_paridade([2, 7, 4, 9, 6]))
print(alterna_paridade([5, 8, 3, 10]))
print(alterna_paridade([2, 7, 9, 4]))
print(alterna_paridade([6]))