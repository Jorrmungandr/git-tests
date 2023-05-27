class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def __str__(self):
        return f'Esse é um carro da marca {self.marca} e do ano {self.ano}'

gol = Carro('Volkswagen', 2012)
camaro = Carro('Gm', 2012)

print(camaro)
