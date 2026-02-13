numeros = []

for i in range(6):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(num)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

print("\n--- Resultados ---")

soma = sum(numeros)
print(f"A soma de todos os números é: {soma}")

menor_numero = min(numeros)
maior_numero = max(numeros)
print(f"O menor número digitado foi: {menor_numero}")
print(f"O maior número digitado foi: {maior_numero}")

media = soma / len(numeros)
print(f"A média dos valores é: {media:.2f}")
