#1. Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.

def saudacao():
    return("Olá! Seja bem-vindo ao Python!")

print(saudacao())    

#2. Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.

def dobro(num):
    return (num *2)

print(dobro(8))

#3. Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.

def soma(num1, num2):
    return num1 + num2

print(soma(10, 20))

#4. Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

nome = input("Digite seu nome: ")

def mensagem(nome):
    return nome

if mensagem(nome) != "":
    print(f"Olá, {mensagem(nome)}!")

else:
    print("Olá, visitante!")

#5. Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

def operacoes(num1, num2):
    soma_1 = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    return soma_1, sub, mult

soma_1, sub, mult = operacoes(num1, num2)

print(f"Soma: {soma_1}, Subtração: {sub}, Multiplicação: {mult}.")

#6. Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.

def media(*numeros):
    soma_media = sum(numeros)
    quantidade_numeros = len(numeros)
    return soma_media / quantidade_numeros

media1 = media(3, 7, 10)
media2 = media(3, 7, 10, 5, 9)
media3 = media(3, 7, 10, 5, 9, 4, 5)

print(f"O resultado da média é: {media1:.2f}")
print(f"O resultado da média é: {media2:.2f}")
print(f"O resultado da média é: {media3:.2f}")

#7. Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:

def dados_pessoais(**kwargs):
	for chave, valor in kwargs.items():
		print(chave, valor)

dados_pessoais(nome="Ane", idade=26, cidade="Camaragibe")


#8. Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.
try:
    opcao = int(input("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\nDigite a opção desejada: "))
    if opcao < 1 or opcao > 4:
        print("Erro! Digite uma opção válida.")
        exit()
        
except ValueError:
     print(f"Erro. A opção digitada não é válida.")   
     exit()

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))    

def calculadora(num1, num2):
     soma = num1 + num2
     sub = num1 - num2
     mult = num1 * num2
     div = num1 / num2
     return soma, sub, mult, div

soma, sub, mult, div = calculadora(num1, num2)

if opcao == 1:
     print(f"A soma dos números digitados é: {soma}")
elif opcao == 2:
     print(f"A subtração dos números digitados é: {sub}") 
elif opcao == 3:
    print(f"A multiplicação dos números digitados é: {mult}")         
elif opcao == 4: 
     print(f"A divisão dos números digitados é: {div}")

     