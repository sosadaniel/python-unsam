
from datetime import  datetime

#8.1: segundos vividos
def vida_en_segundos(fecha_na):
    fecha_na = datetime.strptime(fecha_na, '%d/%m/%Y')
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_na
    return float(diferencia.total_seconds())

print(vida_en_segundos('05/06/1999'))