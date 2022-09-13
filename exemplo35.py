#Entrar via teclado com um valor qualquer. Travar a digitação, no 
# sentido de aceitar somente valores positivos. Após a digitação, 
# exibir a tabuada do valor solicitado, no intervalo de um a dez.


num = int(input("Digite um número  "))

while (num <= 0 ):
    print("O número precisa ser positivo! Digite outro número  ")
    num = int(input("Digite um número  "))
i= 1

while (i <=10 ):
    t = num * i
    print(f'{num} * {i} = {t}')
    i = i + 1

    