soma = 0
positivos = 0
negativos = 0
resposta = "S"

while(resposta == "S"):
    quant = int(input('Quantidade de números que serão digitados: '))

    while(quant < 0 or quant >=20):
        print('Opa! Não pode números negativos e quantidade deve ser menor que 20')
        quant = int(input('Quantidade de números que serão digitados: '))


    for quant in range(1, quant + 1, 1):
        num = int(input('Digite um número: '))

        #while(num < 0):
        #    print('Opa! Não pode números negativos!')
        #    num = int(input('Digite outro número: '))
    
        if(quant == 1):
            maior = num
        else:
            if(num > maior):
                maior = num

        if(quant == 1):
            menor = num
        else:
            if(num < menor):
                menor = num

        if(num > 0):
            positivos = positivos + 1
        else:
            negativos = negativos + 1

        soma = soma + num

    media = soma / quant

    porcentagemPositivo = (positivos * 100) / quant
    porcentagemNegativo = (negativos * 100) / quant

    print('O maior valor: ', maior)
    print('O menor valor: ', menor)
    print('Soma dos valores: ', soma)
    print('Média: ', media)
    print('Porcentagem dos valores positivos: ', porcentagemPositivo)
    print('Porcentagem dos valores : ', porcentagemNegativo)

    resposta = input('Deseja uma nova execução do programa?(S/N) ').upper()

    while(resposta != 'S' and resposta != 'N'):
        print('Seguir padrão de resposta S/N')
        resposta = input('Deseja uma nova execução do programa?(S/N) ').upper()
