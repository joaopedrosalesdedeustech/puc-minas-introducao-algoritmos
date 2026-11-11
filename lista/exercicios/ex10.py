nomes = []
tempos = []

quantidade = int(input("Quantidade de atletas: "))

for i in range(quantidade):
    nome = input(f"Nome do atleta {i + 1}: ")
    tempo = float(input(f"Tempo de {nome} (s): "))
    nomes.append(nome)
    tempos.append(tempo)

soma = 0
for i in range(len(tempos)):
    soma = soma + tempos[i]

media = soma / len(tempos)
print(f"\nTempo médio: {media:.2f}")

print("Atletas abaixo da média:")
for i in range(len(tempos)):
    if tempos[i] < media:
        print(nomes[i])

usados = []

print("Pódio:")
for colocacao in range(3):
    menor = -1

    for i in range(len(tempos)):
        if i not in usados:
            if menor == -1 or tempos[i] < tempos[menor]:
                menor = i

    usados.append(menor)
    print(f"{colocacao + 1}° lugar: {nomes[menor]} - {tempos[menor]}")
