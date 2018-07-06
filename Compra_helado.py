


tenes_ganas_de_helado_input= input("tenes ganas de comer helado ( si / no ):")

if tenes_ganas_de_helado_input == "si":
    tenes_ganas_de_helado = True
elif tenes_ganas_de_helado_input == "no":
    tenes_ganas_de_helado = False
else:
    print("no se que dijiste, pero hagamos de cuenta que no")
tenes_plata_input = input("¿Tenes plata para comprarlo? ( si / no ):")


if tenes_plata_input == "si":
    tenes_plata = True
elif tenes_plata_input == "no":
    tenes_plata = False
else:
    print("jaja, pobre")

esta_tu_tia_input = input("¿esta tu tia? ( si / no):")
esta_abierta_heladeria_input= input("esta abierta la heladeria? ( si / no ):")

tenes_ganas_de_helado = tenes_ganas_de_helado_input == "si"
tenes_plata = tenes_ganas_de_helado_input == "si"
esta_tu_tia = esta_abierta_heladeria_input == "si"
esta_abierta_heladeria = esta_abierta_heladeria_input == "si    "

if tenes_ganas_de_helado or tenes_plata or esta_tu_tia or esta_abierta_heladeria:
    print("entonces come helado")
else:
    print("lastima")