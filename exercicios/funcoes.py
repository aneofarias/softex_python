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
    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    return soma, sub, mult

print(f"A soma, a subtração e a multiplicação do número digitado são, respectivamente: {operacoes(num1, num2)} ")

