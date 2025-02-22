 #Funcion to compute maximun heart rate
 
def maxHR (age):
     HR = 200 - 0.7 * age
     return HR
#ASk user for age
age = int(input("Ingrese su edad: "))
Fcardiacas = float(input("Ingrese su frecuencia cardiaca: "))
if Fcardiacas >= maxHR(age) * 0.5 and Fcardiacas < maxHR(age) * 0.6:
    print("Estas en la zona 1")
elif Fcardiacas >= maxHR(age) * 0.6 and Fcardiacas < maxHR(age)* 0.7:
    print("Estas en la zona 2")
elif Fcardiacas >= maxHR(age) * 0.6 and Fcardiacas < maxHR(age)* 0.8:
    print("Estas en la zona 3")
elif Fcardiacas >= maxHR(age) * 0.6 and Fcardiacas < maxHR(age)* 0.9:
    print("Estas en la zona 4")
elif Fcardiacas >= maxHR(age) * 0.6 and Fcardiacas < maxHR(age)* 1:
    print("Estas en la zona 5")
elif Fcardiacas < maxHR(age) * 0.5:
    print("No hizo nada de ejercicio")
else:
    print("Tirese para el hospital")
    