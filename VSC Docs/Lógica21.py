numeros = int(input("Qual o número do funcionário?"))
horas = int(input("Quantas horas trabalhadas?"))
valorH = float(input("QUal o valor que recebe por hora?"))

salario = horas * valorH

print(f"numeros = {numeros}")
print(f"SALARIO = R$ {salario:.2f}")