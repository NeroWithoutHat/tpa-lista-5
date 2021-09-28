n1= 0
calculator= 1
total= 0
while calculator <= 10:
    calculator += 1
    n1= int(input('Em que ano você nasceu: '))
    maior= 2021 - n1
    if maior >= 18:
        total += 1
print ('{} São maiores de idade'.format (total))
