"""
HAZ UNA FUNCION QUE PASE DE 
SEGUNDOS  A DIAS, HORAS, MINUTOS
"""

def convertir_segundos(segundos):
    dias = segundos // 86400  # 86400 segundos en un día
    segundos %= 86400
    horas = segundos // 3600  # 3600 segundos en una hora
    segundos %= 3600
    minutos = segundos // 60   # 60 segundos en un minuto
    segundos %= 60

    return dias, horas, minutos, segundos


total_segundos = 100000
dias, horas, minutos, segundos = convertir_segundos(total_segundos)
print(f"{total_segundos} segundos son {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")
