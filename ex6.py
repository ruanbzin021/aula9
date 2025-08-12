"""
6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""

lista = []

for i in range(5):
    print(f"\nDigite as 4 notas do {i+1}º aluno:")
    notas_do_aluno = []
    
    for n in range(4):
        nota = float(input(f"Digite a {n+1}ª nota: "))
        notas_do_aluno.append(nota)
    
    lista.append(notas_do_aluno)

print("\nNotas e médias de todos os alunos:")

contador = 1
for notas in lista:
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Aluno {contador}: Notas = {notas} | Média = {media:.2f}")
    contador += 1
