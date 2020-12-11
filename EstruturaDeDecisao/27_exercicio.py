# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
# quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo
# cliente.

def calcule_valor(fruta, quantidade_kg):
    if fruta.upper() == 'MAÇA':
        if quantidade_kg <= 5:
            return quantidade_kg * 2.50
        elif quantidade_kg > 5 and quantidade_kg <= 8:
            return quantidade_kg * 2.20
        elif quantidade_kg > 8:
            valor = quantidade_kg * 2.20
            return valor - (valor * 0.10)
    elif fruta.upper() == 'MORANGO':
        if quantidade_kg <= 5:
            return quantidade_kg * 1.80
        elif quantidade_kg > 5 and quantidade_kg <= 8:
            return quantidade_kg * 1.50
        elif quantidade_kg > 8:
            valor = quantidade_kg * 1.50
            return valor - (valor * 0.10)
    else:
        raise ValueError('Fruta não Encontrada!')


fruta = input('Digite a Fruta que deseja Comprar(Maça/Morango): ')

quantidade_kg = float(input('Digite a quantiade(kg) que deseja: '))

valor = calcule_valor(fruta, quantidade_kg)

print(f'O Valor a ser pago é: R${valor}')
