main
class Asiento:
    def _init_(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        cambiarColor = color
        if cambiarColor == "rojo" or "verde" or "amarillo" or "negro" or "blanco":
            color = cambiarColor


class Auto:
    cantidadCreados = 0
    def _init_(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self, Auto.asientos):
        cantidad = 0
        for i in self.asientos:
            if isinstance(i,asiento):
            cantidad +=1
        return cantidad


    def verificarIntegridad(self, Auto.asientos):
        if  :
            return "Las piezas no son originales"
        else:
            return "Auto original"


class Motor:
    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, ):

    def asignarTipo(self, ):
        

