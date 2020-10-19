

import datetime
average_lifespan = 80
smoke_penalization = 10
drinker_penalization = 10
sedentary_penalization = 20

def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + " [S/N]")
    return response == "S"

print_with_underscores("Averigua cuanto te queda de vida")
print("Completa esta encuesta para saber cuanto tiempo de vida te queda")

birth_date = input("Cuál es tu fecha de nacimiento? (formato: dd/mm/yyyy ?) ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
years_lost = 0

if ask_yes_or_not("Fumas?"):
    years_lost += smoke_penalization

if ask_yes_or_not("Bebes? "):
    years_lost += drinker_penalization

if not ask_yes_or_not("Hacés deporte? "):
    years_lost += sedentary_penalization

lifespan = average_lifespan - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("La fecha de tu muerte es {} te quedan {} días para morir".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))