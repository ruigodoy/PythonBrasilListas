# João Papo-de-Pescador, homem de bem, comprou um microcomputador para
# controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso
# de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso de peixes e
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que João deverá pagar. Imprima
# os dados do programa com as mensagens adequadas.

def calcular_excesso(peso_peixes):
    if peso_peixes > 50:
        return peso_peixes - 50
    else:
        return 0


def calcular_multa(peso_peixes):
    return calcular_excesso(peso_peixes) * 4


peso_peixes = float(input('Digite o peso dos peixes: '))

multa = calcular_multa(peso_peixes)
excesso = calcular_excesso(peso_peixes)

print(f'Peso total dos peixes: {peso_peixes}')

if peso_peixes > 50.0:
    print(f'Quilos Excedidos: {excesso}, Multa: {multa}')
