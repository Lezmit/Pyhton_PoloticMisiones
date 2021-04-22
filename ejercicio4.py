"""Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales"""
from datetime import datetime,date,time,timedelta
hoy=datetime.now()
hora_actual=time(hoy.hour,hoy.minute,hoy.second)
masHoras=hoy+timedelta(hours=2)
print("hora actual es: ",hora_actual)
print("2 horas mas de la hora actual es:" , masHoras)
