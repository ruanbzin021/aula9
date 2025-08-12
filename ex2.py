# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range(10):
    n = int(input(f"Digite o {i+1}º numero da lista: "))
    lista.append(n)

lista.sort(reverse=True)
#print(list(reversed(lista)))    
print(lista)