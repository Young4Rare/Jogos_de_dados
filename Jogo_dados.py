import random

while True:
    entrada = input("Informe o número de vezes que deseja lançar os dados: ")

    if entrada.isdigit():
        n = int(entrada)
        break
    else:
        print("Por favor, insira um número válido.")

frequencias = [0] * 11

for _ in range(n):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    frequencias[soma - 2] += 1

print("\nResultados:")
for soma, frequencia in enumerate(frequencias, start=2):
    print(f'Ganho {soma}: {frequencia} vezes')
