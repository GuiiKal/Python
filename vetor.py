import random

# GERAR DUAS MATRIZES ALEATORIAS E DEPOIS FAZER A SOMA DELAS
#A função randrange é usada para realizar a tarefa de gerar os números aleatórios. 
#randrange(start, stop, step) - inicio, pare, quantidade de casas que pula
val1 = [random.randrange(1, 50, 1) for i in range(4)]
print ("Lista 3 : ", val1)

val2 = [random.randrange(1, 50, 1) for i in range(4)]
print ("Lista 2 : ", val2)

final=[0,0,0,0]
for i in range(4):
    final[i]=val1[i]+val2[i]
    i=i+1
print(final)    

#--------------------------------------------------------------------------
# vet1 = [0,0,0,0]
# vet2 = [0,0,0,0]
# res = [0,0,0,0]
# i=0

# for i in range(4):
#     x=random.randint(1,9)
#     vet1[i]=x
#     i=i+1
# i=0

# for i in range(4):
#     x=random.randint(1,9)
#     vet2[i]=x
#     i=i+1   
# i=0

# for i in range(4):
#     res[i]=vet1[i]+vet2[i]
#     i=i+1

# print(vet1)
# print(vet2)
# print(res)
#---------------------------------------------------------------------------
# x = 5
# saida = []
# for _ in range(x):
#     saida.append(random.choice(range(100)))
# print (saida)
#---------------------------------------------------------------------------

