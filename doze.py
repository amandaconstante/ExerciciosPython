# que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento;

salario = input('Informe seu salário atual: ')
salario = float(salario)
aumento = salario*0,15
novoSal = salario + aumento
print(f'Seu salário foi de R${salario} para R${novoSal}\n')