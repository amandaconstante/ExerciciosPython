#   que leia um número inteiro qualquer e mostre na tela sua tabuada;

nro = input('Informe um valor: ')
nro = int(nro)
for i in range(0, 11):
  print(f'{nro} x {i} = {nro*i}', )