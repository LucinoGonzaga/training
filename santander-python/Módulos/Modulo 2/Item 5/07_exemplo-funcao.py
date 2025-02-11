def calcular_media(*numeros):
    soma = sum(numeros)
    cantidated = len(numeros)
    media = soma / cantidated
    return media

print("Media:", calcular_media(10, 20, 30, 40))

def somar_3(x):
    return x + 3

somar = lambda x: x + 3

print("Somar 3 a um número: ", somar(6))