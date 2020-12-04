# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def calcula_salario(horas_mensais, valor_hora):
    return horas_mensais * valor_hora


horas_mensais = float(input('Digite quantas horas você trabalhou no mês: '))

valor_hora = float(input('Digite quanto você ganha por hora: '))

salario = calcula_salario(horas_mensais, valor_hora)

print(f'Você trabalhou {horas_mensais} horas, preço por hora R${valor_hora}')

print(f'Salario: R${salario}')
