# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


def calcula_area_circulo(raio):
    return 3.14 * pow(raio, 2)


raio = float(input('Digite o Raio de um Círculo: '))

area = calcula_area_circulo(raio)

print(f' A Área do Círculo é: {area}')
