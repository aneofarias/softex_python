#1. Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

numero = input("Digite um número: ")

try:
    numero = int(numero)
    print(f"O número informado foi: {numero}")

except ValueError: 
    print(f"{numero} não é um número.")


#2. Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

print("Informe dois números para multiplicação")
num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    mult = num1 * num2
    print(f"O resultado da multiplicação dos números informados é: {mult}")

except ValueError:
    print(f"{num1} ou {num2} não é um número válido para multiplicar.")    

#3. Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

numero = input("Digite um número inteiro: ")

try: 
    numero = int(numero)

except ValueError:
    print(f"Erro! O {numero} não é um número inteiro.")

else:
    print(f"Conversão bem sucedida! O {numero} é um número inteiro.") 

#4. Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

iniciar = input('Aperte [E] para abrir o arquivo "dados.txt" ou qualquer tecla para encerrar o programa: ') 

try:
    iniciar == "E"
    print("O arquivo foi aberto com sucesso.")

except ValueError:
    print("O programa será encerrado.")

finally:
    print("Encerrando o programa.")    


#5. Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

a = input("Digite um número: ")
b = input("Digite outro número: ")

def divisao(a, b):
    a = float(a)
    b = float(b)
    if b == 0:
        raise ZeroDivisionError(f"Erro! Digite um número diferente de 0.")
    return a / b

try:
    resultado = divisao(a, b)
    print(f"O resultado da divisão é: {resultado}.")

except ZeroDivisionError:
    print(f"Erro! Digite um número diferente de 0.")

except ValueError:
    print(f"Erro! O valor digitado é inválido.")

