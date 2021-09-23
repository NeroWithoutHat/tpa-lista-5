calculator=1
resultado=1
fator= int(input('Digite um número e mostraremos o fatorial:  ') )
while calculator <= fator:
    resultado *= calculator
    calculator += 1
print('resultado do fatorial de {} é {}'.format (fator, resultado))