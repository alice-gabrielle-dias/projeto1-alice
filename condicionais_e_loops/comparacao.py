nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 12:
    print (f"{nome}, você tem direito a 50% de desconto")
elif idade >= 60:
    print(f"{nome}, você tem direito a 30% de desconto")
else:
    print(f"{nome}, hoje não tem desconto para você")
    