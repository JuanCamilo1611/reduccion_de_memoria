# src/utils.py
import random
import time
import tracemalloc

def generar_estado_aleatorio(longitud):
    """
    Genera un estado binario aleatorio de longitud dada.
    """
    return [random.randint(0, 1) for _ in range(longitud)]

def medir_tiempo_y_memoria(funcion):
    """
    Mide el tiempo y la memoria de ejecución de una función.
    
    Retorna una tupla: (resultado, tiempo, memoria_kb)
    """
    tracemalloc.start()
    inicio = time.perf_counter()
    
    resultado = funcion()
    
    fin = time.perf_counter()
    memoria_actual, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    tiempo = fin - inicio
    memoria_kb = memoria_actual / 1024
    
    return resultado, tiempo, memoria_kb
