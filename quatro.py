#desafio === Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis (isnumeric, isalpha..)

algo = input("digite algo: ")

print('numero: ', algo.isnumeric())
print('tem letras: ', algo.isalpha())
print('tem letras OU numeros: ', algo.isalnum())
print('tudo em minúsculo: ', algo.islower())
print('tudo em maiúsculo: ', algo.isupper())
print('é apenas espaço: ', algo.isspace())
print('da de imprimir: ', algo.isprintable())
