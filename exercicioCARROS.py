class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    
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

class Motor:
    def __init__(self,nome):
        self.nome = nome
class Fabricante:
    def __init__(self,nome):
        self.nome = nome



carro_1 = Carro('Fusca')
fabricante_1 = Fabricante('Volkswagen')
motor_1 = Motor('1.0')
carro_1.fabricante = fabricante_1
carro_1.motor = motor_1

carro_2 = Carro('Nivus')
motor_2 = Motor('200 TSI')
carro_2.fabricante = fabricante_1
carro_2.motor = motor_2

carro_3 = Carro('Uno')
fabricante_2 = Fabricante('Fiat')
motor_3 = Motor('1.4')
carro_3.fabricante = fabricante_2
carro_3.motor = motor_3

print(carro_1.nome, carro_1.fabricante.nome, carro_1.motor.nome)
print(carro_2.nome, carro_2.fabricante.nome, carro_2.motor.nome)
print(carro_3.nome, carro_3.fabricante.nome, carro_3.motor.nome)

