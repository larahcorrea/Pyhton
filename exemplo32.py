#Entrar com dois valores via teclado, onde o segundo deverá ser maior
#  que o primeiro. Caso contrário solicitar novamente apenas o segundo
#  valor.


v1 = int(input("Digite o primeiro número   ")) 
v2 = int(input("Digite o segundo número   ")) 


while (v2 < v1):
    num = int(input("Digite outro número para obter a tabuada   "))
    if (v2 > v1):
        print
    break
i = 1
i = i + 1