#1. Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Ane", 26)
p2 = Pessoa("Caline", 30)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

#2. Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Ane", 26)
p2 = Pessoa("Caline", 30)

p1.apresentacao()
p2.apresentacao()

#3. Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def apresentacao (self):
        print(f"{self.marca} {self.modelo} {self.ano}.")    


c1 = Carro("Volkswagen", "T-Cross", 2025)       
c2 = Carro("Fiat", "Uno", 2000)
c3 = Carro("Honda", "Civic", 2019)

c1.apresentacao()
c2.apresentacao()
c3.apresentacao()

#4. Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def edit(self, novo_ano):
        self.ano = novo_ano    

c = Carro("Volkswagen", "Gol", 2010)
print(c.marca, c.modelo, c.ano)
c.edit(2013)
print(c.marca, c.modelo, c.ano)

#5. Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, novo_saldo):
        self.saldo = novo_saldo            

    def sacar(self, novo_saldo):
       # if - fazer a comparação com o saldo
        self.saldo = novo_saldo    

b = ContaBancaria("Ane", -99)        
print(b.titular, b.saldo)
