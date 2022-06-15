class Calendario:
    
    def __init__(self, dia, mes, año ):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    def __str__(self):
        return "{}/{}/{}".format(self.dia, self.mes , self.año)

    
