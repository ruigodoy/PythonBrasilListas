# Faça um Programa para uma loja de tintas. O programa
# deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 6 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00 ou
# em galões de 3,6 litros, que custam R$ 25,00. Informe
# ao usuário as quantidades de tinta a serem compradas
# e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o preço seja
#     o menor. Acrescente 10% de folga e sempre arredonde
#     os valores para cima, isto é, considere latas cheias.

from math import ceil


def calcule_litros(area):
    return (area / 6) * 1.1


area = float(input('Digite o tamanho da área para ser pintada: '))

litros_tinta = calcule_litros(area)

latas_tintas = ceil(litros_tinta / 18)

galoes_tintas = ceil(litros_tinta / 3.6)

preco_latas = latas_tintas * 80.0

preco_galoes = galoes_tintas * 25.00

mix_latas = int(litros_tinta / 18.0)

mix_galoes = int((litros_tinta - (mix_latas * 18.0)) / 3.6)

if ((litros_tinta - (mix_latas * 18.0) % 3.6 != 0)):
    mix_galoes += 1

print(f'Preço apenas usando Latas de 18L: R${preco_latas}')

print(f'Preço apenas usando Galões de 3,6L: R${preco_galoes}')

print(f'Usando: {mix_latas} Latas e {mix_galoes} Galoes')
print(f'Preço usando os dois: R${(mix_latas * 80) + (mix_galoes * 25)}')
