#1. Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.

def saudacao ():
    return("Olá! Seja bem-vindo ao Python")

print(saudacao())    

#2. Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.

def dobro(num):
    return (num *2)

dobro = (4)
print(dobro())

#3. Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.

def soma(num1, num2):
    return num1 + num2

soma = (10, 20)
print(soma())

#4. Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

def mensagem(nome):
    return nome

if mensagem != "":
    print(f"Olá, {mensagem()}")

else:
    print("Olá, visitante!")

#5. Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.

def operacoes ():
    def soma(num1, num2):
        return (num1 + num2)

    def sub(num1, num2):
        return (num1 - num2)    
    
    def mult (num1, num2):
        return (num1 * num2)
    ############################### Verificar essa função, se vai calcular todas ou é necessário um if para ir validando cada um.
