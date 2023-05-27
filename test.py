# class Carro:
#     def __init__(self, marca, ano):
#         self.marca = marca
#         self.ano = ano

#     def __str__(self):
#         return f'Esse é um carro da marca {self.marca} e do ano {self.ano}'

# class Pessoa:
#     def __init__(self, nome, altura):
#         self.nome = nome
#         self.altura = altura

#         uno = Carro(marca='Fiat', ano=2012)

#         self.carro = uno

# edgar = Pessoa(nome='Edgar', altura=2)

# print(edgar.carro.marca)

def dormir(horas):
    if horas < 4:
        print('Você vai ficar cansado o dia todo')
        raise Exception('Você vai ficar cansado o dia todo')
    elif horas <= 8:
        print('tô dormindo')
    else:
        print('dormiu demais')

try:
    dormir(1)
    print('Normal')
except:
    print('Erro')
