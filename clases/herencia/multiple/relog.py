class Relog:
    
    def __init__(self, hora, minutos, segundos ):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos
    
    def __str__(self):
        return "{}:{}:{}".format(self.hora, self.minutos , self.segundos)
