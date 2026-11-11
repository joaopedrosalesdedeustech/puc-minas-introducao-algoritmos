def maior_diferenca(valores):
    maior = 0
    
    for k in range(1, len(valores)):
        diferenca = valores[k] - valores[k - 1]
        
        if diferenca < 0:
            diferenca = diferenca * (-1)
        
        if diferenca > maior:
            maior = diferenca
    
    return maior

print(maior_diferenca([10, 4, 7, 15, 13]))
print(maior_diferenca([5, 5, 5]))
print(maior_diferenca([20, 3]))        