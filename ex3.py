# 3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista= []

for i in range(4):
    n = float(input("Digite um numero: "))
    lista.append(n)

soma = sum(lista)
media = soma / 4
print(f"{lista}\nA Soma total é {soma} e a média é {media}")