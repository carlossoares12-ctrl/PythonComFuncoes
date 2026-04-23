numerosPares = []
numerosImpares = []

def ehPar(n):
    if n%2==0:
        return True
    else:
        return False

while True:
    n=int(input("insira um valor: "))
    if n==0:
        break
    else:
        if ehPar(n):
            numerosPares.append(n)
        else:
            numerosImpares.append(n)

print("Numero Pares: ", numerosPares)
print("Quantidade de Números Pares: ", len(numerosPares))
print("Números Ímpares: ", numerosImpares)
print("Quantidade de Números Ímpares: ", len(numerosImpares))