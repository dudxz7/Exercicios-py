class pessoa:
    def __init__(self, nome, idade, altura, peso, anos):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.anos = anos
    
    def envelhecer(self, anos):
        self.idade += anos
    def crescer(self, anos):
        if self.idade < 21:
            self.altura += 0.05*anos
    def dados(self):
        print(self.nome, self.idade, self.altura, self.peso)

humano = pessoa(nome = input("Digite seu nome: "), idade = int(input("Informe sua idade: ")), altura = float(input("Informe sua altura: ")), peso = float(input("Informe seu peso: ")), anos = int(input("Informe os anos: ")))
humano.envelhecer(humano.anos)
humano.crescer(humano.anos)
humano.dados()