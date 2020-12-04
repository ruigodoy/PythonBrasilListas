# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.
# (0 °C × 9/5) + 32 = F

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


celsius = float(input('Digite a Temperatura em Celsius: '))

fahrenheit = celsius_para_fahrenheit(celsius)

print(f'{celsius} Celsius são {fahrenheit} Fahrenheit  ')
