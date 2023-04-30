# que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

h = input('Informe a altura do muro em metros: ')
h = float(h)
base = input('Informe a largura do muro em metros: ')
base = float(base)
area = base*h

print(f'Para a area de {area:.2f} metros, será necessário {area/2:.2f} litros de tinta')