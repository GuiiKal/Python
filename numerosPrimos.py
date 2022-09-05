primos=[]

for i in range(1,10000):
    cont=0

    for x in range(1, i+1):
        if i%x==0:
            cont+=1
    
    if cont <=2:
        primos.append(i)

print(primos)            
print("Total de números primos encontrados:", len(primos))