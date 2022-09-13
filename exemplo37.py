# Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez.
#  Entre as tabuadas, solicitar que o usuário pressione uma tecla.


num = int(input("Digite um número  "))
i = 1

while (i <= 10):
    t = num * i
    print(f'{num} * {i} = {t}')
    i = i + 1

    