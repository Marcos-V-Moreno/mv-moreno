class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome       

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = Motor
        self._fabricante = Fabricante

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)

logan = Carro('Logan 2019')
renoalt = Fabricante('Renoalt')
motor_1_0 = Motor('1.0')
renoalt.fabricante = renoalt
renoalt.motor = motor_1_0
print(logan.nome, renoalt.fabricante.nome, renoalt.motor.nome)

caravan = Carro('Caravan')
volkswagen = Fabricante('Volkswagen')
motor_1_8 = Motor('1.8')
caravan.fabricante = volkswagen
caravan.motor = motor_1_8
print(caravan.nome, caravan.fabricante.nome, caravan.motor.nome)