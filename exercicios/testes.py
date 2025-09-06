#9. Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

def soma(a, b): 
    return a + b

def sub(a, b):
     return a - b

def mult(a, b):
     return a * b

def div(a, b):
     return a / b

def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

print(f"Resultado da operação de soma: {aplicar_operacao(a, b, soma)}.")    
print(f"Resultado da operação de subtração: {aplicar_operacao(a, b, sub)}.")    
print(f"Resultado da operação de multiplicação: {aplicar_operacao(a, b, mult)}.") 
print(f"Resultado da operação de divisão: {aplicar_operacao(a, b, div)}.")       