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
        self.operacoes = []

    def __str__(self):
         return(f"Titular {self.titular} possui um saldo de: R${self.saldo}.")
    
    def deposito(self, valor):
         self.saldo += valor
         self.operacoes.append(f"Deposito")
         return(f"Foi depositado um valor de: R${valor} na sua conta. Saldo atual: R${self.saldo}")

    def saque(self, valor):
         self.saldo -= valor
         self.operacoes.append(f"Saque")
         return(f"Foi sacado um valor de R${valor} da sua conta. Saldo atual: R${self.saldo}")
    
b = ContaBancaria("Ane", 100)    
print(b)

print(b.deposito(500))
print(b.saque(150))

#6. Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.operacoes = []

    def __str__(self):
         return(f"Titular {self.titular} possui um saldo de: R${self.saldo}.")
    
    def deposito(self, valor):
         self.saldo += valor
         self.operacoes.append(f"Deposito")
         return(f"Operação de deposito bem sucedida. Saldo atual: R${self.saldo}")

    def saque(self, valor):
        if self.saldo >= valor:
         self.saldo -= valor
         self.operacoes.append(f"Saque")
         return True
        else:
            print("Operação de saque inválida. O valor solicitado é menor que o saldo.")
            return False
        
    
b = ContaBancaria("Ane", 100)    
print(b)

print(b.deposito(500))
print(b.saque(700))

#7. Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.

class Alunos:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

a1 = Alunos("Ane", 9.5)
a2 = Alunos("Tamara", 10)
a3 = Alunos("Frederico", 10)
a4 = Alunos("Leandro", 6)
a5 = Alunos("Calinão", 10)

turma1 = Turma()
turma1.adicionar_aluno(a1)
turma1.adicionar_aluno(a2)

turma2 = Turma()
turma2.adicionar_aluno(a3)
turma2.adicionar_aluno(a4)
turma2.adicionar_aluno(a5)

for aluno in turma1.alunos:
    print(f"Nome: {aluno.nome}, Nota: {aluno.nota}")

for aluno in turma2.alunos:    
    print(f"Nome: {aluno.nome}, Nota: {aluno.nota}")

#8. Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.

class Alunos:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome}, Nota: {self.nota}"    

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

a1 = Alunos("Ane", 9.5)
a2 = Alunos("Tamara", 10)
a3 = Alunos("Frederico", 10)
a4 = Alunos("Leandro", 6)
a5 = Alunos("Calinão", 10)

turma1 = Turma()
turma1.adicionar_aluno(a1)
turma1.adicionar_aluno(a2)

turma2 = Turma()
turma2.adicionar_aluno(a3)
turma2.adicionar_aluno(a4)
turma2.adicionar_aluno(a5)

for aluno in turma1.alunos:
    print(aluno)

for aluno in turma2.alunos:    
    print(aluno)

#9. Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.

class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Acessando pela classe:
print(Cachorro.especie)

# Acessando pelo objeto:

c = Cachorro("Bico de Pato", 2)
print(c.especie)