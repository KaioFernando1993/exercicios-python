divida = int(input())
mensalidade = int(input())
contador = 1

while divida > 0:
      print(f'pagamento: {contador}')
      print(f'antes = {divida}')
      contador += 1
      if divida <= mensalidade :
         divida = 0
      else:
         divida = divida - mensalidade
print(f'depois = {divida}')
print('-----')

