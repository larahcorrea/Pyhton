v1 = int(input("Digitar primeiro valor  "))
v2 = int(input("Digitar segundo valor  "))
v3 = int(input("Digitar terceiro valor  "))

if v1 > v2 and v1>3:
    print("Primeiro número é o maior")
elif v1 == v2 == v3: 
    print("São Iguais!")
elif v1<v2 and v2>v3:
    print("O segundo número é o maior")
else:
    print("O terceiro número é o maior")
