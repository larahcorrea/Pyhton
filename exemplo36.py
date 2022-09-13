#Entrar via teclado com um valor (X) qualquer. Travar a digitação, 
# no sentido de aceitar somente valores positivos. Solicitar o 
# intervalo que o programa que deverá calcular a tabuada do valor
#  digitado, sendo que o segundo valor (B), deverá ser maior que o 
# primeiro (A), caso contrário, digitar novamente somente o segundo.
#  Após a validação dos dados, exibir a tabuada do valor digitado, no
#  intervalo decrescente, ou seja, a tabuada de X no intervalo de B
#  para A.



num = int(input("Digite um número  "))


while (num <= 0 ):
    print("O número precisa ser positivo! Digite outro número  ")
   
a = int(input("Digite o ínicio do intervalo  "))
b = int(input("Digite o fim do intervalo  "))

while (b < a ):
    print("O b precisa ser maior que a!")
    b = int(input("Digite o fim do intervalo  "))
3
for i in range ( b , a -1 , -1):
    t = num * i
    print( num,'x' , i, '=', t )



    