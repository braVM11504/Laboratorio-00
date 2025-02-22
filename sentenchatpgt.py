# Función para calcular la frecuencia cardíaca máxima
def maxHR(age):
    return 200 - 0.7 * age

# Pedir datos al usuario
age = int(input("Ingrese su edad: "))
Fcardiacas = float(input("Ingrese su frecuencia cardíaca: "))

# Calcular frecuencia cardíaca máxima
HRmax = maxHR(age)

# Determinar la zona de entrenamiento
if Fcardiacas >= HRmax * 0.5 and Fcardiacas < HRmax * 0.6:
    print("Estás en la zona 1")
elif Fcardiacas >= HRmax * 0.6 and Fcardiacas < HRmax * 0.7:
    print("Estás en la zona 2")
elif Fcardiacas >= HRmax * 0.7 and Fcardiacas < HRmax * 0.8:
    print("Estás en la zona 3")
elif Fcardiacas >= HRmax * 0.8 and Fcardiacas < HRmax * 0.9:
    print("Estás en la zona 4")
elif Fcardiacas >= HRmax * 0.9 and Fcardiacas <= HRmax:
    print("Estás en la zona 5")
elif Fcardiacas < HRmax * 0.5:
    print("No hizo nada de ejercicio")
else:
    print("Tírese para el hospital")
