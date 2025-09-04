#6. Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

idade_usuario = input("Digite sua idade: ")

def cadastrar_idade(idade_usuario):
    idade_usuario = int(idade_usuario)
    class IdadeInvalidaError(Exception):
        pass
    if idade_usuario <= 0:
        raise IdadeInvalidaError("Idade inválida. Digite novamente.")
    return idade_usuario

try: 
    idade_usuario != 0
    print(f"A idade digitada: {idade_usuario} é válida.")

except IdadeInvalidaError:
    print("Idade inválida. Digite novamente.")  

except ValueError:
    print(f"Erro! A idade digitada é inválido.")