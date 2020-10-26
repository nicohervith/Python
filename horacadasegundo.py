from time import sleep
import datetime

night_starts = 19
day_starts = 7
hour_duration = 1


#  TODO LO QUE SE ESTÁ IMPRIMIENDO EN ESTE CÓDIGO SE ESCRIBE TAMBIEN EN EL HORAS.TXT
#  FILE_NAME,'a'       open for writing, appending to the end of the file if it exists


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{} {}".format(text, "\n"))
        print(text)

def main():
    current_time = datetime.datetime.now()
    is_night = False

    while True:
        sleep(hour_duration)
        current_time += datetime.timedelta(hours=1)
        light_chaged = False

        if (current_time.hour >= night_starts or current_time.hour <= day_starts) and not is_night:
            is_night = True
            light_chaged = True

        elif (current_time.hour > day_starts and current_time.hour < night_starts) and is_night:
            is_night = False
            light_chaged = True

        if light_chaged:
            if is_night:
                write_file_and_screen ("Se hizo de noche","horas.txt")
            else:
                write_file_and_screen("Se hizo de día","horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time),"horas.txt")


if __name__ == "__main__":
    main()


