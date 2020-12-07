# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.


def calcular_salario_bruto(horas, valor_hora):
    return horas * valor_hora


def calcular_descontos(salario_bruto):
    imposto_renda = salario_bruto * 0.15
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    return imposto_renda, inss, sindicato


horas = int(input('Digite quantas Horas você Trabalhou: '))
valor_hora = float(input('Digite quantos você recebe por Hora: '))


salario_bruto = calcular_salario_bruto(horas, valor_hora)
imposto, inss, sindicato = calcular_descontos(salario_bruto)
salario_liquido = salario_bruto - (imposto + inss + sindicato)

print(f'Salário Bruto: {salario_bruto}')
print(f'IR: {imposto}')
print(f'INSS: {inss}')
print(f'Sindicato: {sindicato}')
print(f'Salário Liquido: {salario_liquido}')
