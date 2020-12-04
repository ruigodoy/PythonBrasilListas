# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


# o produto do dobro do primeiro com metade do segundo .
def produto(primeiro_numero, segundo_numero):
    return (primeiro_numero * 2) * (segundo_numero / 2)


# a soma do triplo do primeiro com o terceiro.
def soma(primeiro_numero, terceiro_numero):
    return (primeiro_numero * 3) + terceiro_numero


# o terceiro elevado ao cubo.
def cubo(terceiro_numero):
    return terceiro_numero ** 3


primeiro_numero = int(input('Digite um Numero Inteiro: '))

segundo_numero = int(input('Digite um Segundo Numero Inteiro: '))

terceiro_numero = float(input('Digite um Terceiro Numero Real: '))

print(f'Produto: {produto(primeiro_numero, segundo_numero )}')

print(f'Soma: {soma(primeiro_numero, terceiro_numero)}')

print(f'Cubo: {cubo(terceiro_numero)}')
