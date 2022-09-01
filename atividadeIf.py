from datetime import date
from datetime import datetime

#Através do ano em que o usuario nasceu, imprimir se ele pode votar e dirigir

anoNascimento = input("Digite o ano em que você nasceu: ")

#transforma a string digitada em tipo data
date = datetime.strptime(anoNascimento, '%Y').date()
#pega o ano atual através do sistema
anoAtual = date.today()

if date<anoAtual:  
    #subtrai os anos para saber a idade
    idade = anoAtual.year-date.year
    #Para usar uma f-string você escreve o f antes de string entre as aspas.
    #Todos os espaços dentro das aspas serão considerados, e você pode passar variáveis dentro de {} chaves.
    print(f"Sua idade é: {idade}") # = print("Sua idade é: ", idade)
    #idade = int(input("Digite a sua idade:"))
    if idade<16:
        print("Você NÃO pode dirigir e nem votar")
    elif idade >=16 and idade <18: 
        print("Você pode votar, mas não pode dirigir")
    elif idade >=75:
        print("Você pode dirigir e votar")
    else:
        print("Você pode dirigir e DEVE votar")
else:
    print("Digite um ano válido. Você não pode digitar um ano do futuro")

    
# programa para saber se pode dirigir ou não e se deve votar 
# idade = int(input("Digite a sua idade:"))
# if idade<16:
#     print("Você NÃO pode dirigir e nem votar")
# elif idade >=16 and idade <18: 
#         print("Você pode votar, mas não pode dirigir")
# elif idade >=75:
#         print("Você pode dirigir e votar")
# else:
#     print("Você pode dirigir e DEVE votar")
