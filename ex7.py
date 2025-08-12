# 7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista= []

for i in range(5):
    n = int(input(f"Digite o {i+1}º numero: "))
    lista.append(n)

soma = sum(lista)
multi = lista[0] * lista[1] * lista[2] * lista[3] * lista[4]
print(f"{lista}\nA Soma total: {soma}\nMultiplicação: {multi}")