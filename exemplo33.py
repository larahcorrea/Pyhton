#Entrar via teclado com o sexo de determinado usuário, aceitar somente
#  “F” ou “M” como respostas válidas


r = str(input("Qual seu sexo? [F/M]   ")).upper() 
i = 1
while(r != 'M' or r != 'F' ):
    r = str(input(" Apenas responda [F/M]   ")).upper()
    if ( r == 'M'or r == 'F'):
        print
    break
i = 1
i = i + 1