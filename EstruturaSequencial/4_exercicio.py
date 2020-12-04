# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
soma_notas = 0

for i in range(4):
    print(f'Digite a {i+1} Nota: ')
    nota = int(input())
    notas.append(nota)
    soma_notas += nota

media = soma_notas / len(notas)

print(f'a Média das 4 notas é: {media}')
