from datetime import datetime
from datetime import date

horaAtual = datetime.now()

def hora():
    return "{}:{}:{}".format(horaAtual.hour, horaAtual.minute, horaAtual.second)

def dia():
    dias = [
        'segunda-feira',
        'terça-feira',
        'quarta-feira',
        'quinta-Feira',
        'sexta-feira',
        'sábado',
        'domingo'
    ]
    data = date(horaAtual.year, horaAtual.month, horaAtual.day) 
    indice_da_semana = data.weekday()
    dia_da_semana = dias[indice_da_semana]
    return dia_da_semana

def data():
    return "{}/{}/{}".format(horaAtual.day, horaAtual.month, horaAtual.year)
