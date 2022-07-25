inicio = int(input()) 
fim = int(input())
primos = 0

for numero in range(inicio,fim+1,1):
  divisoes = 0
  cont = 1

  while cont <= numero:
    if numero % cont == 0 and numero != 1:
      divisoes +=1
    cont +=1
    
  if divisoes == 2:
    print(f'{numero}')
    primos +=1  

print(f'primos: {primos}')
