n= 0
calculator= 1
maior= 0
while calculator <= 10:
    n= int(input('Digite 10 números: '))
    if maior < n:
        maior = n
    calculator +=1
    
print (maior)