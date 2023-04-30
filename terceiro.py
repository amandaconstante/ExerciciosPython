#feito em 02.02.2023
#003 código que leia 2 números e mostre a soma entre eles

nr1 = float(input('1o nro: '))
nr2 = input('2o nro: ')
resultado = nr1 + float(nr2)
print("A sua soma é: ", resultado)

print(f'A soma de {nr1} e {nr2} é {resultado}') # novo formato de interpolação a partir do python 3.6, f-string;

print(type(nr1))
print(type(nr2))
print(type(resultado))