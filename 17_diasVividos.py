"""
HAZ UNA FUNCION QUE TE DIGA CUANTOS DIAS
LLEVAS VIVIDO A PARTIR DE TU FECHA DE NACIMIENTO
"""
from datetime import datetime

def dias_vividos(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_nacimiento
    return diferencia.days

fecha_nacimiento = "2000-01-01"  # Cambia esto por tu fecha de nacimiento en formato AAAA-MM-DD
print(f"Has vivido {dias_vividos(fecha_nacimiento)} días.")
