# print(list(["casa", "predio"]))

# class Gato:
#     raca = "Sem raça definida"
#     nome = "Frederico" 
#     idade = 5

# miau = Gato()

# print(f"Dados do animal: \n Nome: {miau.nome}, Raça: {miau.raca}, Idade: {miau.idade} anos.")

print("A seguir, digite as informações do veículo que você procura.")
marca = input("Marca: ")
modelo = input("Modelo: ")
ano = int(input("Ano: "))
km = int(input("Quilometragem máxima: "))

class Carro:
    tipo = "SUV"
    def __init__(self, marca, modelo, ano, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def apresentacao (self):
        print(f"Os dados digitados foram: {self.marca} {self.modelo} {self.ano} com até {self.km}km.\n")    


c = Carro(marca, modelo, ano, km)       
c.apresentacao()

print("Agora, informe a forma de pagamento que você procura.")
forma_pagamento = input("Para pagamento à vista digite [A] e para financiamento digite [F]: ").strip().upper()

class Pagamento:
    def __init__(self, forma_pagamento):
        if forma_pagamento.lower() == "a":
            print("A forma de pagamento selecionada foi à vista.")
        elif forma_pagamento.lower() == "f":
            print("A forma de pagameanto seleciona foi financiamento.")
            try:
                self.entrada = float(input("Informe o valor da entrada R$: "))    
                self.parcelas = int(input("Informe a quantidade de parcelas: "))
                print(f"Os valores informados para o financiamento foram: Entrada de R${self.entrada} e {self.parcelas} parcelas.")   
            except ValueError:
                print("Valor inválido para entrada ou parcelas. Tente novamente.") 
        else:
            print("Opção de pagamento inválida. Verifique se digitou corretamente.")    
      
p = Pagamento(forma_pagamento)
print("Em breve retornaremos o contato com as fotos, informações e a melhor condição de pagamento para veículo preenchido.")

