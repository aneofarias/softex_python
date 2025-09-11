

class ContaBancaria:
    def __init__(self, conta, titular, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        self.operacoes = []
    
    # def depositar(self, novo_saldo):
    #     self.saldo = novo_saldo            

    # def sacar(self, novo_saldo):
    #     self.saldo = novo_saldo    

    def __str__ (self):
        return(f"Conta nº {b.conta!r} do titular {b.titular!r} possui {b.saldo!r} de saldo.")
        
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Deposito", {valor})
        return (f"Foi depositado um valor de R${valor} em sua conta.")

    def saque(self, valor):
        self.saldo -= valor
        self.operacoes.append(f"Saque", {valor})
        return (f"Foi sacado um valor de R${valor} da sua conta.")

    def extrato(self, consulta):


#adicionar horário, data no append

b = ContaBancaria("Ane", 312443, -99)        
print(b)

b.deposito(100)
print(b)

b.saque(1)
print(b)
