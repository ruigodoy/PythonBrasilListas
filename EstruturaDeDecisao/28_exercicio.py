# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
# Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos
# tipos de carne da promoção, porém não há limites para a quantidade de carne
# por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
# um desconto de 5% sobre o total da compra. Escreva um programa que peça o
# tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.

def calcule_preco(carne, quantidade):
    if carne.upper() == 'FILE DUPLO':
        if quantidade <= 5:
            return quantidade * 4.9, carne
        elif quantidade > 5:
            return quantidade * 5.80, carne
    elif carne.upper() == 'ALCATRA':
        if quantidade <= 5:
            return quantidade * 5.9, carne
        elif quantidade > 5:
            return quantidade * 6.80, carne
    elif carne.upper() == 'PICANHA':
        if quantidade <= 5:
            return quantidade * 6.9, carne
        elif quantidade > 5:
            return quantidade * 7.80, carne
    else:
        raise ValueError('Fruta não Encontrada!')


carne = input(
    'Digite a Carne que deseja Comprar(File Duplo/Alcatra/Picanha): ')

quantidade_kg = float(input('Digite a quantiade(kg) que deseja: '))

preco_total, tipo_carne = calcule_preco(carne, quantidade_kg)

desconto_cartao_tabajara = preco_total * 0.05

valor_a_pagar = preco_total - desconto_cartao_tabajara

print(f'Carne Escolhida: {tipo_carne}')
print(f'Preço Total: {preco_total}')
print(f'Quantidade KG: {quantidade_kg}')
print(f'Desconto Cartão Tabajara: {desconto_cartao_tabajara}')
print(f'Valor a Pagar: {valor_a_pagar}')
