inicio = int(input()) 
fim = int(input())
ab = 0

for ano in range(inicio,fim+1,1):
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f"{ano}")
    ab +=1

print(f'bissextos: {ab}')
