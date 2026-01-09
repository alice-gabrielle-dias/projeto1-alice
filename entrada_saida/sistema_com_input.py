def calcular_imc(peso, altura):
    return peso / (altura * altura)
imc = calcular_imc(float(input("Digite seu peso: ")), float(input("Digite sua altura: ")))
print(f"{imc:.2f}")
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc >= 30:
        return "Obesidade"
print(classificar_imc(imc))