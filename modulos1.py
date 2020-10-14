
from datetime import date

dia = date(2020,10,14)

fin_de_año = date(2020,12,31)
restan = (fin_de_año - dia).days
print('para fin de año restan',restan,'días')