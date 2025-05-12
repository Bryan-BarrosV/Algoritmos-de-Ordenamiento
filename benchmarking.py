import time
import random
import copy

class Benchmarking:
    def __init__(self):
        print("Benchmarking inicializando")

    def build_arreglo(self, size):
        return [random.randint(0, 99999) for _ in range(size)]

    def medir_tiempo(self, tarea, array):
        array_copy = copy.copy(array)
        inicio = time.perf_counter()
        tarea(array_copy)
        fin = time.perf_counter()
        return fin - inicio

