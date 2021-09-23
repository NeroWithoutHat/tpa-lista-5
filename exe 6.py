n1= int(input('Digite o preço do primeiro produto: '))
n2 = int(input('Digite o preço do segundo número: '))
pr1= ((n1 * 8) / 100) -n1
pr2= ((n1 * 11) / 100) -n2
resultado= (pr1+pr2) *-1
print ('Com o desconto de 8% e  11%  o total vai ser de {}'.format (resultado))