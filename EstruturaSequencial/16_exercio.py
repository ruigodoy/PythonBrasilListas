# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da
# tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
# de latas de tinta a serem compradas e o preço total.

from math import ceil


def calcula_litros(area):
    return area / 3


area = float(input('Digite o tamanho da área para ser pintada: '))

litros_tintas = calcula_litros(area)

latas_tintas = ceil(litros_tintas / 18)

preco_total = latas_tintas * 80.0

print(f'Quantidade de Latas: {latas_tintas}; Preço Total: {preco_total}')
