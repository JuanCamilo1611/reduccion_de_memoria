import numpy as np
import time


"""Monte Carlo Simulation for Random Bit Activation"""
class MonteCarlo:
   
    def __init__(self, state_length, num_samples):
        self.state_length = state_length
        self.num_samples = num_samples

    # Genera ejemplos aleatorios de bits y calcula el promedio de bits activados
    def run(self):
        from src.utils import medir_tiempo_y_memoria

        """
        Función para medir el tiempo y la memoria de una función dada. 
        """
        def procesar():
            samples = np.random.randint(0, 2, size=(self.num_samples, self.state_length), dtype=np.int8)
            return np.mean(samples), samples.nbytes / 1024

        # Medir el tiempo y la memoria de la función procesar
        # y obtener el promedio de bits activados
        (promedio, memoria_kb), tiempo, _ = medir_tiempo_y_memoria(procesar)

        return {
            "estrategia": "Monte Carlo",
            "longitud_estado": self.state_length,
            "numero_muestras": self.num_samples,
            "promedio_bits_activados": promedio,
            "tiempo_segundos": tiempo,
            "memoria_kb": memoria_kb
        }
