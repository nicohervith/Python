import datetime


year = int(input("Decime el año: "))
month = int(input("Decime el mes: "))
day = int(input("Decime el día: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print("Para tu cumpleaños faltan {} días y {} horas".format(time_remaining.days, int(time_remaining.seconds / 3600)))