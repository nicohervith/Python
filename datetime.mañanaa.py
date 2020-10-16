
import datetime

manana = datetime.datetime.now() + datetime.timedelta(days=1)
manana_medianoche = datetime.datetime(year=manana.year , month=manana.month , day=manana.day)
hoy = datetime.datetime.now()

faltante_para_manana = manana_medianoche - hoy

print("mañana es {} ".format(manana.strftime("%d / %m / %Y")))
print("Faltan para mañana {} horas ".format(int(faltante_para_manana.total_seconds() / 3600)))