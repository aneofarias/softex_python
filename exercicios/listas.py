#1. Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ["As vantagens de ser invisível", "O dilema do porco-espinho", "O caçador de pipas"]

#2. 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
print(f"O primeiro livro da lista é: {livros[0]}.")
print(f"O último livro da lista é: {livros[-1]}.")

#3. Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append("O assassinato no Expresso oriente")
livros.append("Um corpo na biblioteca")
print(livros)

#4. Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1, "Duna")
print(livros)

#5. Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print(livros)
else:
    print("Livro não encontrado.")        

#6. Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.

numeros = [1, 2, 3, 2, 4, 2, 5]
print(f"O número 2 aparece {(numeros.count(2))} vezes.")

#7. Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
lista_livros = []
for livro in livros:
    print(f"O livro {livro} é interessante.")

#8. Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
lista_idades = []
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print(f"As idades iguais ou superiores a 18 são: {idade}.")

#9. Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.  
lista_valores = []
valores = [10, 20, 30, 40]
soma = 0
for valor in valores:
    soma = soma + valor
print(f"A soma de todos os valores é: {soma}.")

#10. Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas.
notas = []

notas_aluno1 = []
nota1_aluno1 = float(input("Digite a 1ª nota do primeiro aluno: "))
nota2_aluno1 = float(input("Digite a 2ª nota do primeiro aluno: "))
nota3_aluno1 = float(input("Digite a 3ª nota do primeiro aluno: "))

notas_aluno1.append(nota1_aluno1)
notas_aluno1.append(nota2_aluno1)
notas_aluno1.append(nota3_aluno1)

soma_aluno1 = nota1_aluno1 + nota2_aluno1 + nota3_aluno1
media_aluno1 = (soma_aluno1 / 3)
print(f"As notas do primeiro aluno foram {notas_aluno1}.\nA média desse aluno ficou: {media_aluno1:.2f}.")

notas_aluno2 = []
nota1_aluno2 = float(input("Digite a 1ª nota do segundo aluno: "))
nota2_aluno2 = float(input("Digite a 2ª nota do segundo aluno: "))
nota3_aluno2 = float(input("Digite a 3ª nota do segundo aluno: "))

notas_aluno2.append(nota1_aluno2)
notas_aluno2.append(nota2_aluno2)
notas_aluno2.append(nota3_aluno2)

soma_aluno2 = nota1_aluno2 + nota2_aluno2 + nota3_aluno2
media_aluno2 = (soma_aluno2 / 3)
print(f"As notas do segundo aluno foram {notas_aluno2}.\nA média desse aluno ficou: {media_aluno2:.2f}.")


#11. Questão tabuleiro usando list comprehension. (Questão resolvida em sala)

lista_peoes= ["pea"]*8
lista_pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"] 
tabuleiro = [["[ ]" for casa in range(8)] for linha in range(8)]
tabuleiro[0] = lista_pecas.copy()
tabuleiro[1] = lista_peoes.copy()
tabuleiro[-1] = lista_pecas[::-1]
tabuleiro[-2] = lista_peoes.copy()

tabuleiro[2][4] = tabuleiro [1][4]
tabuleiro[1][4]= "[ ]"

for linha in tabuleiro:
    print(linha)


