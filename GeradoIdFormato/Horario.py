import datetime

class Horario:
    @staticmethod   
    def obter():
        return str(datetime.datetime.utcnow())