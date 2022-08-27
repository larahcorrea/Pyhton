peso = float(input("Digite o seu peso "))
altura = float(input("digite a sua altura "))
imc = peso/(altura * altura)
if imc < 20:
    print("Voce não esta com o peso ideial ")
elif imc < 25 :
    print("Seu peso é ideial! ")
else :
    print("Voce não esta com o peso ideial ")


