import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from exhaustive import exhaustive_processing
from montecarlo import MonteCarlo

def comparar_enfoques(state_length, num_samples):
    print("\n--- COMPARACIÓN DE ENFOQUES ---")

    # Enfoque exhaustivo
    print("\n[Enfoque Exhaustivo]")
    ex = exhaustive_processing(state_length)
    promedio_ex = ex["promedio_unos"]
    tiempo_ex = ex["tiempo"]
    memoria_ex = (2 ** ex["bits"]) * ex["bits"] / 8 / 1024  # memoria aproximada en KB
    print(f"Promedio de bits activados: {promedio_ex:.2f}")
    print(f"Tiempo: {tiempo_ex:.4f} segundos")
    print(f"Memoria usada: {memoria_ex:.2f} KB")

    # Enfoque Monte Carlo
    print("\n[Enfoque Monte Carlo]")
    mc = MonteCarlo(state_length, num_samples)
    result_mc = mc.run()
    promedio_mc = result_mc["promedio_bits_activados"]
    tiempo_mc = result_mc["tiempo_segundos"]
    memoria_mc = result_mc["memoria_kb"]
    print(f"Promedio de bits activados: {promedio_mc:.2f}")
    print(f"Tiempo: {tiempo_mc:.4f} segundos")
    print(f"Memoria usada: {memoria_mc:.2f} KB")

    # Comparación rápida
    print("\n--- RESUMEN ---")
    print(f"Diferencia de tiempo: {(tiempo_ex - tiempo_mc):.4f} segundos")
    print(f"Diferencia de memoria: {(memoria_ex - memoria_mc):.2f} KB")

# Ejemplo de uso
# Cambia la longitud del estado y el número de muestras según sea necesario
if __name__ == "__main__":
    longitud_estado = 4
    num_muestras = 20
    comparar_enfoques(longitud_estado, num_muestras)
