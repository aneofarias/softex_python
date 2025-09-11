# Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.

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
