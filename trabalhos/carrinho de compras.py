from math import trunc

n = int(input())
l = []

for i in range (n):
    e = input()
    l1 = [x for x in e.split(';')]
    l.append(l1)    

x = float(input())
y = float(input())


for j in range(n):
    if l[j][3] == 'sim':
        b = int(l[j][1])
        if b >= 1000:
            l[j].append(((trunc(b/1000)*x)))
        else:
            l[j].append(0)
    
    elif l[j][3] == 'não':
        b = int(l[j][1])
        if b >= 1000:
            l[j].append(((trunc(b/1000)*y)))
        else:
            l[j].append(0)

print('-----')
print('BÔNUS')
print('-----')

for j in range(n):
    print(f'{l[j][0]}: R$ {float(l[j][4])+float(l[j][2]):.2f}')   
