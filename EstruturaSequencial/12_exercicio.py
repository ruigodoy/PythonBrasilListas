# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
#  que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def calcular_peso(altura):
    return (72.7 * altura) - 58


altura = float(input('Digite o sua Altura: '))

peso_ideal = calcular_peso(altura)

print(f'O Seu peso ideal é: {peso_ideal}')
