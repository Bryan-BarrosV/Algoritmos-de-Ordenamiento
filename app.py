import matplotlib.pyplot as plt
import copy


from benchmarking import Benchmarking
from metodos_de_ordenamiento import MetodoOrdenamiento

if __name__ == "__main__":
    print("Iniciando comparación de métodos de ordenamiento")

    metodos = MetodoOrdenamiento()
    benchmark = Benchmarking()

    tamanios = [5000, 10000, 30000, 50000, 100000]
    resultados = []

    metodos_dict = {
        "Burbuja": metodos.metodo_burbuja,
        "Burbuja Optimizada": metodos.metodo_burbuja_optimizado,
        "Selección": metodos.metodo_seleccion,
        "Inserción": metodos.metodo_insercion,
        "Shell": metodos.metodo_shell,
    }

    for tam in tamanios:
        arreglo_base = benchmark.build_arreglo(tam)
        print(f"\nEvaluando tamaño de arreglo: {tam}")

        for nombre, metodo in metodos_dict.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)
            print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

    print("\n--- Resumen de Resultados ---")
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

    tiempos_by_metodo = {nombre: [] for nombre in metodos_dict.keys()}
    tamanios_unicos = sorted(list(set([res[0] for res in resultados])))

    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize=(12, 7))

    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios_unicos, tiempos, label=nombre, marker='o')

    plt.title("Comparativa de Métodos de Ordenamiento por Tiempo de Ejecución")
    plt.xlabel("Tamaño del Arreglo")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.xticks(tamanios_unicos)

    plt.show()
