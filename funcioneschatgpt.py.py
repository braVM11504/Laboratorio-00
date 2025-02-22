def maxHR(age):
    return 208 - (0.7 * age)

def get_Z2_HR_range(age):
    """Calcula el rango de frecuencia cardíaca necesario para entrenar en Z2"""
    hr_min = maxHR(age) * 0.6
    hr_max = maxHR(age) * 0.7
    return hr_min, hr_max

# Solicitar la cantidad de entrenamientos
Nentrenamientos = int(input("Ingrese la cantidad de entrenamientos realizados en la semana: "))

# Lista para almacenar las frecuencias cardiacas
promedios = []

# Solicitar la edad del usuario
age = int(input("Ingrese su edad: "))

# Calcular y mostrar el rango de frecuencia cardíaca para Z2
hr_min, hr_max = get_Z2_HR_range(age)
print(f"\nPara entrenar en la Zona 2, su frecuencia cardíaca debe estar entre {hr_min:.2f} y {hr_max:.2f} pulsaciones por minuto.\n")

# Pedir frecuencias cardiacas para cada entrenamiento
for i in range(1, Nentrenamientos + 1):
    f = float(input(f"Ingrese el promedio de pulsaciones por día {i}: "))
    promedios.append(f)

# Inicializar contadores de zonas
z1 = z2 = z3 = z4 = z5 = 0

# Analizar cada entrenamiento y clasificarlo en una zona
for i in range(Nentrenamientos):
    if maxHR(age) * 0.5 <= promedios[i] < maxHR(age) * 0.6:
        print(f"En el entrenamiento {i + 1} te encuentras en Zona 1")
        z1 += 1
    elif maxHR(age) * 0.6 <= promedios[i] < maxHR(age) * 0.7:
        print(f"En el entrenamiento {i + 1} te encuentras en Zona 2")
        z2 += 1
    elif maxHR(age) * 0.7 <= promedios[i] < maxHR(age) * 0.8:
        print(f"En el entrenamiento {i + 1} te encuentras en Zona 3")
        z3 += 1
    elif maxHR(age) * 0.8 <= promedios[i] < maxHR(age) * 0.9:
        print(f"En el entrenamiento {i + 1} te encuentras en Zona 4")
        z4 += 1
    elif maxHR(age) * 0.9 <= promedios[i] <= maxHR(age):
        print(f"En el entrenamiento {i + 1} te encuentras en Zona 5")
        z5 += 1
    elif promedios[i] < maxHR(age) * 0.5:
        print(f"En el entrenamiento {i + 1} no realizaste ejercicio suficiente.")
    else:
        print(f"En el entrenamiento {i + 1} superaste la frecuencia cardíaca máxima.")

# Calcular porcentajes de entrenamientos en cada zona
pZ1 = int(100 * (z1 / Nentrenamientos))
pZ2 = int(100 * (z2 / Nentrenamientos))
pZ3 = int(100 * (z3 / Nentrenamientos))
pZ4 = int(100 * (z4 / Nentrenamientos))
pZ5 = int(100 * (z5 / Nentrenamientos))

# Imprimir los porcentajes de entrenamiento en cada zona
print(f"\nEl porcentaje de entrenamientos en la Zona 1 es {pZ1}%")
print(f"El porcentaje de entrenamientos en la Zona 2 es {pZ2}%")
print(f"El porcentaje de entrenamientos en la Zona 3 es {pZ3}%")
print(f"El porcentaje de entrenamientos en la Zona 4 es {pZ4}%")
print(f"El porcentaje de entrenamientos en la Zona 5 es {pZ5}%")