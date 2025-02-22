# Función para calcular la frecuencia cardíaca máxima
def maxHR(age):
    return 200 - 0.7 * age

# Función para determinar la zona de trabajo
def determinar_zona(Fcardiacas, edad):
    hr_max = maxHR(edad)
    
    if 0.5 * hr_max <= Fcardiacas < 0.6 * hr_max:
        return "Zona 1 (Muy ligera)"
    elif 0.6 * hr_max <= Fcardiacas < 0.7 * hr_max:
        return "Zona 2 (Ligera)"
    elif 0.7 * hr_max <= Fcardiacas < 0.8 * hr_max:
        return "Zona 3 (Moderada)"
    elif 0.8 * hr_max <= Fcardiacas < 0.9 * hr_max:
        return "Zona 4 (Intensa)"
    elif 0.9 * hr_max <= Fcardiacas <= hr_max:
        return "Zona 5 (Máxima)"
    elif Fcardiacas < 0.5 * hr_max:
        return "No hizo nada de ejercicio"
    else:
        return "¡Peligro! Posible sobreesfuerzo, acuda al médico."

# Solicitar edad del usuario
edad = int(input("Ingrese su edad: "))

# Solicitar número de entrenamientos
num_entrenamientos = int(input("Ingrese el número de entrenamientos realizados: "))

# Lista para almacenar las zonas de cada entrenamiento
zonas_entrenamiento = []

# Iterar para cada entrenamiento
for i in range(num_entrenamientos):
    Fcardiacas = float(input(f"Ingrese la frecuencia cardíaca promedio del entrenamiento {i+1}: "))
    zona = determinar_zona(Fcardiacas, edad)
    zonas_entrenamiento.append(zona)
    print(f"Entrenamiento {i+1}: {zona}")

# Imprimir resumen de zonas
print("\nResumen de entrenamientos:")
for i, zona in enumerate(zonas_entrenamiento, start=1):
    print(f"- Entrenamiento {i}: {zona}")
