"""
5.	Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

lista = []
pares = []
impares = []
for i in range(20):
    num = int(input(f'Digite o {i+1}º número inteiro da lista: '))
    lista.append(num)

    if num % 2 == 0:
        pares.append(num)

    else:
        impares.append(num)
        
print("\nVetor com todos os números:")
print(lista)

print("\nVetor com números pares:")
print(pares)

print("\nVetor com números ímpares:")
print(impares)

