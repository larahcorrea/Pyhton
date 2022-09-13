#Fazer um programa para receber um número e validar 
# se esse número é positivo.
#  Após isso, exibir a tabuada de 1 a 10 desse número.

num = int(input("Digite um número   ")) 

while(num <= 0):
    print("Não pode número negativo!")
    num = int(input("Digite outro número para obter a tabuada   ")) 
i = 1

while (i < 11):
    r = num * i
    print(f" {num} * {i} = {r}")
    i = i + 1

    

