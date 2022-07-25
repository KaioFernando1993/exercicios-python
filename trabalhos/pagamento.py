conta = float(input())
pagamento = float(input())
contador = 0
total = 0

while conta > 0:
    total = conta - pagamento
    print(f'ainda deve{total:.2f}')
    if conta <= 0:
        print(f'nao deve mais nada')
    
    
