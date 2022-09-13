sexo = input("Informe o seu gênero: ").upper()

while(sexo != "F" and sexo != "M"):
    print("A entrada deve ser no formato F ou M")
    sexo = input("Informe novamente seu gênero: ").upper()

print(f'Gênero: {sexo}')