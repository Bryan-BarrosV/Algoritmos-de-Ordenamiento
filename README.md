# 🧠 Algoritmos de Ordenamiento – Práctica 4.2

**Carrera:** Computación  
**Asignatura:** Estructura de Datos  
**Práctica:** 4.2 – Algoritmos de Ordenamiento  
**Autores:** *Bryan Barros y Erika Collaguazo*  
**Docente:** Ing. Pablo Torres

---

## 🎯 Objetivos

- Comprender y comparar distintas técnicas de ordenamiento.
- Desarrollar módulos que emplean los algoritmos: Burbuja, Burbuja con ajuste, Selección, Inserción y Shell.
- Medir y analizar el tiempo de ejecución de cada algoritmo según el tamaño del arreglo.

---

## 🧪 Instrucciones principales

- Se generan arreglos con los siguientes tamaños:  
  **5.000, 10.000, 30.000, 50.000 y 100.000 elementos.**
- Se utiliza el **mismo arreglo base** para todos los métodos de ordenamiento (usando `.clone()`).
- No se deben imprimir los arreglos, solo los **tiempos de ejecución**.
- Se debe tomar el tiempo antes y después de ejecutar cada algoritmo.
- El informe debe incluir:
    - Tabla de resultados.
    - Gráfica comparativa.
    - Conclusiones utilizando terminología de notación y complejidad.
    - Enlace al repositorio del proyecto.

---

### 📋 Tabla de Resultados: Tiempos de Ejecución (en segundos)

| Tamaño del Arreglo | Burbuja     | Burbuja Optimizada | Selección   | Inserción   | Shell       |
|--------------------|-------------|---------------------|-------------|-------------|-------------|
| 5,000              | 1.424351    | 1.512157            | 0.607775    | 0.703033    | 0.013431    |
| 10,000             | 5.376367    | 5.561193            | 2.464302    | 3.942533    | 0.048947    |
| 30,000             | 78.855838   | 52.032036           | 22.398148   | 25.070052   | 0.113490    |
| 50,000             | 145.820069  | 154.655319          | 83.372915   | 101.146991  | 0.226128    |
| 100,000            | 968.118029  | 747.601211          | 342.697463  | 376.266798  | 0.581103    |

---
## 📊 Gráfica comparativa

![Gráfica de métodos de ordenamiento](grafica_comparativa.jpeg)

---

## 📌 Conclusiones (con terminología de notación)

- El **algoritmo de burbuja** y su versión mejorada tienen una complejidad de \(O(n^2)\), lo que significa que su tiempo de ejecución crece muy rápido al aumentar la cantidad de datos.
- **Shell sort** demostró ser el más eficiente, con tiempos muy bajos incluso para 100.000 elementos. Su complejidad está entre \(O(n)\) y \(O(n \log n)\), dependiendo de la secuencia usada.
- **Selección e inserción** también tienen \(O(n^2)\), pero su rendimiento varía ligeramente por cómo trabajan internamente.
- Esta práctica evidencia la importancia de **elegir algoritmos adecuados** según el tamaño de los datos, y por qué se analiza la complejidad con **notación Big O**.
- En general, a mayor complejidad algorítmica, mayor será el tiempo de ejecución con listas grandes.
 
---
### Conclucion por estudiante 
1. Durante esta práctica pude observar claramente cómo influye la complejidad algorítmica en el rendimiento real de un programa. Los métodos como burbuja y selección, aunque fáciles de entender, resultan ineficientes para listas grandes, ya que su tiempo de ejecución crece de forma cuadrática. En cambio, algoritmos como Shell demostraron una gran ventaja en tiempos, incluso con arreglos de 100.000 elementos. Me pareció interesante ver cómo la teoría de la complejidad, especialmente la notación Big O, se refleja en pruebas prácticas. Aprendí que no basta con que un algoritmo funcione; también importa qué tan bien lo hace con grandes volúmenes de datos.
2. Esta práctica me ayudó a entender por qué es tan importante saber elegir el algoritmo adecuado según la situación. Antes solo veía los métodos de ordenamiento como formas distintas de organizar datos, pero ahora comprendo que algunos pueden ser muy lentos cuando la cantidad de datos es grande. Me llamó la atención lo eficiente que fue Shell comparado con los otros métodos. También entendí mejor cómo la teoría de la complejidad nos ayuda a pensar de forma lógica y a predecir el rendimiento de nuestros programas. En resumen, fue una experiencia útil y práctica que me servirá mucho para escribir código más optimizado.
