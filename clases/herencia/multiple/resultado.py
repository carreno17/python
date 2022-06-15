
from calendario import Calendario
from relog import Relog

class Resultado(Calendario, Relog):

    def __init__(self, dia, mes, año, hora, minutos, segundos):
        Calendario.__init__(self, dia, mes, año)
        Relog.__init__(self, hora, minutos, segundos)
    
    def calendario(self):
        return Calendario.__str__(self)

    def relog(self):
        return Relog.__str__(self)

    def __str__(self):
        return  self.relog() + " " + self.calendario()



