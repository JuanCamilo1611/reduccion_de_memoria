
from src.montecarlo import MonteCarlo
import numpy as np

# Parámetros
longitud_estado = 20
num_muestras = 1000

# Crear el objeto y ejecutar muestreo
mc = MonteCarlo(longitud_estado, num_muestras)

# Ejecutar
promedio, tiempo, memoria = mc.ejecutar()


# Mostrar resultados
print("\n--- Prueba Monte Carlo ---")
print(f"Longitud del estado: {longitud_estado}")
print(f"Número de muestras: {num_muestras}")
print(f"Promedio de bits activados: {promedio:.2f}")
print(f"Tiempo de ejecución: {tiempo:.4f} segundos")
print(f"Memoria usada: {memoria:.2f} KB")
