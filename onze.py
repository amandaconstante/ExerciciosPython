# que leia o preço de um produto e mostre seu novo preço, com 5% de desconto;

print('='*50)
preco = input('Informe o preço do produto: ')
preco = float(preco)
desconto = preco*0.05
print(f'\nO produto tem 5% de desconto\n\nDE R${preco} POR {preco-desconto:.2f}')
print('='*50)