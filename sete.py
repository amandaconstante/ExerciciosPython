# que leia um valor em metros e o exiba convertido em centímetros e milímetros;

valor = input('Informe o tamanho em metros: ')

cm = (int(valor) * 100)
ml = (int(valor) * 1000)

print(f'{valor} metros\n{cm} centímetros\n{ml} milímetros')