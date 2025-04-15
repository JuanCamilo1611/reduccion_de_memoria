import numpy as np
import time


def exhaustive_processing(num_bits):
    from src.utils import medir_tiempo_y_memoria

    """
    Procesa la cantidad de unos en todos los estados posibles de un número binario de n bits.
    Utiliza una estrategia exhaustiva para contar los unos en todos los estados posibles."""
    def procesar():
        total_states = 2 ** num_bits
        total_ones = 0

        # Iterar sobre todos los estados posibles
        # y contar los unos en su representación binaria
        for i in range(total_states):
            binary = format(i, f"0{num_bits}b")
            total_ones += binary.count("1")

        # Calcular el promedio de unos por estado
        return total_ones / total_states

    # Medir el tiempo y la memoria de la función procesar

    promedio, tiempo, memoria = medir_tiempo_y_memoria(procesar)

    # Devolver los resultados en un diccionario
    return {
        "estrategia": "Exhaustiva",
        "bits": num_bits,
        "promedio_unos": promedio,
        "total_estados": 2 ** num_bits,
        "tiempo": tiempo,
        "memoria_kb": memoria,
    }
