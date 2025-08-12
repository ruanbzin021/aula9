 # 4.	Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

nome = input("Digite um nome: ").strip().lower()
nome = list(nome)

vogais = ['a', 'e', 'i', 'o', 'u']

while len(nome) < 11:
    letras = [letra for letra in nome if letra not in vogais]
    print(letras)
    break
