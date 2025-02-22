def maxHR(age):
    HR = 208 - 0.7 * age
    return HR
def promz2(maxHR):
   return print(f"la frecuencia cardiaca para la zona 2 deberia estar en un rango de {maxHR(age)*0.6} y {maxHR(age)*0.7}")
Nentrenamientos = int(input("Ingrese la cantidad de entrenamientos realizados en la semana: "))
promdias = []
age = int(input("Ingrese su edad: "))
Rangoz2 = promz2(maxHR)
dia = 1
for i in range(1,Nentrenamientos + 1):
    f = float(input(f"Ingrese el promedio de pulsasiones por dia {dia}: "))
    dia += 1
    promdias.append(f)
print(f" {promdias}")
diaN = 0
z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0
for i in range(1,Nentrenamientos + 1):
    if promdias[diaN] >= maxHR(age) * 0.5 and promdias[diaN] < maxHR(age) * 0.6:
        print(f"En el dia {i} te encuentras zona 1")
        z1 += 1
    elif promdias[diaN] >= maxHR(age) * 0.6 and promdias[diaN] < maxHR(age) * 0.7:
        print(f"En el dia {i} te encuentras zona 2 ")
        z2 += 1
    elif promdias[diaN] >= maxHR(age) * 0.7 and promdias[diaN] < maxHR(age) * 0.8:
        print(f"En el dia {i} te encuentras zona 3")
        z3 += 1
    elif promdias[diaN] >= maxHR(age) * 0.8 and promdias[diaN] < maxHR(age) * 0.9:
        print(f"En el dia {i} te encuentras zona 4 ")
        z4 += 1
    elif promdias[diaN] >= maxHR(age) * 0.9 and promdias[diaN] < maxHR(age) * 1:
        print(f"En el dia {i} te encuentras zona 5 ")
        z5 += 1
    elif promdias [diaN] < maxHR(age) * 0.5:
        print(f"En el dia {i} no reañizo ejercicio")
    else:
        print(f"En el dia {i} Supero la frecuencia cardiaca maxima")
    diaN += 1
pz1 = int(100 * (z1/Nentrenamientos)) 
pz2 = int(100 * (z2 /Nentrenamientos))
pz3 = int(100 * (z3 /Nentrenamientos))
pz4 = int(100 * (z4 /Nentrenamientos))
pz5 = int(100 * (z5 /Nentrenamientos) )
print(f"El porcentaje de la zona 1 es  {pz1}%\nEl porcentaje de la zona 2 es  {pz2}%\nEl porcentaje de la zona 3 es {pz3}%\nEl porcentaje de la zona  4 es {pz4}%\nEl porcentaje de la zona 5 es  {pz5}%")


        