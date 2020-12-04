# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

def fahrenheit_para_celsius(fahrenheit):
    return 5 * ((fahrenheit - 32) / 9)


fahrenheit = float(input('Digite a Temperatura em Fahrenheit: '))

celsius = fahrenheit_para_celsius(fahrenheit)

print(f'{fahrenheit} Fahrenheit são {celsius} Celsius')
