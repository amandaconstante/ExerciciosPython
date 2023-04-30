# que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar;
# dólar hoje 14.02.2023: 5,21
# dólar turismo para Jaraguá do sul hoje: 5,47 (melhorcambio.com)

dim = input('Quanto reais você tem: ')
dim = float(dim)

print(f'\nSeus R$ {dim} equivalem a: $ {dim/5.47:.2f} dólares\n(Cotação em 14.02.2022, compra em Jaraguá do Sul)\n\n')
print(f'Seus R$ {dim} equivalem a: $ {dim/5.48:.2f} dólares\n(Cotação em 14.02.2022, compra em Joinville)\n')