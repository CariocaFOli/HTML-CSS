print('{:=^40}'.format(' LOJAS GUANABARA '))

valor = float(input('Qual é o valor da compra: R$ '))
print('''Escolha uma opção de pagamento:
[ 1 ] À vista (Dinheiro/Cheque) - 10% de desconto
[ 2 ] À vista no cartão - 5% de desconto
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão - Juros de 20%''')
forma = input('Digite a opção escolhida: ')

if forma == 1:
    total = valor - (valor * 10/100)
elif forma == 2:
    total = valor - (valor * 5/100)

print('O valor da compra é de R$ {}, e com a forma de pagamento escolhida o valor pago será de R$ {}.'.format(valor, total))

