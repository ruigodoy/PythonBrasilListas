# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


def calcular_peso(altura, sexo):
    if sexo.upper() == 'M':
        return (72.7 * altura) - 58
    elif sexo.upper() == 'F':
        return (62.1 * altura) - 44.7
    else:
        raise ValueError('Sexo Inválido')


altura = float(input('Digite sua altura: '))
sexo = input('Digite o seu Sexo(M/F): ')

peso_ideal = calcular_peso(altura, sexo)

print(f'O Seu peso ideal é: {peso_ideal}')
