# Função positivo ou negativo

numerosPositivos = []
numerosNegativos = []

def eh_positivo(n):
    if n > 0:
        return True
    else:
        return False


while True:
    n = int(input("Digite um número inteiro : "))

    if n == 0:
        break

    if eh_positivo(n):
        numerosPositivos.append(n)
    else:
        numerosNegativos.append(n)

print("\n--- Resultados ---")
print("Números positivos:", numerosPositivos)
print("Números negativos:", numerosNegativos)
print("Quantidade de positivos:", len(numerosPositivos))
print("Quantidade de negativos:", len(numerosNegativos))
