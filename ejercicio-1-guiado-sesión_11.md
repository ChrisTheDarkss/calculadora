# Ejercicio 1 — Guiado — Sesión 11
## Diseño y Construcción de Interfaces Gráficas con Layouts

---

### **Consigna del Ejercicio**

El propósito de esta actividad es aplicar los principios de diseño de interfaces gráficas mediante el desarrollo de una aplicación funcional de **Calculadora**. Para ello, se deberá implementar una distribución principal basada en un **`GridLayout` de 4 columnas por 5 filas**, complementada con un componente **`Label`** encargado de la visualización en tiempo real del número ingresado y los resultados obtenidos.

Además, con el objetivo de comparar y evaluar el comportamiento de distintas estrategias de maquetación, se solicita incorporar una **vista o pantalla adicional** estructurada mediante un **`BoxLayout` de orientación vertical**, la cual debe integrar un título, un campo de entrada de texto y un botón de acción.

---

### **Especificaciones Técnicas de la Calculadora**

#### **1. Estructura del `GridLayout` (4 columnas × 5 filas)**
La matriz de la calculadora debe organizar de forma clara y funcional los siguientes componentes:
* **Visualizador (`Label`):** Área dedicada a mostrar el último número digitado, la operación en curso y el resultado calculado.
* **Teclado Numérico:** Botones para los dígitos del `0` al `9` y el separador decimal (punto o coma `.`).
* **Operaciones Aritméticas Fundamentales:** Botones para:
  * Suma (`+`)
  * Resta (`-`)
  * Multiplicación (`*`)
  * División (`/`)
* **Operador de Asignación / Resultado:** Botón (`=`).
* **Control y Limpieza:** Botón de borrado / reinicio de pantalla (`C` / `AC`).

#### **2. Estructura del `BoxLayout` Secundario**
La vista secundaria destinada a la comparación de gestores de diseño debe cumplir con:
* **Orientación:** Estrictamente `vertical`.
* **Propiedades de Espaciado:** Configuración explícita de `spacing` (espacio entre elementos) y `padding` (márgenes internos del contenedor).
* **Componentes Integrados:**
  1. Etiqueta de Título.
  2. Campo de entrada de texto (`TextInput` / `Entry`).
  3. Botón de acción o confirmación.

---

### **Instrucciones de Entrega y Bonificación**

* **Plataforma Única de Entrega:** La recepción del trabajo se realizará exclusivamente a través de **Educa (Blackboard)**.
* **Formato:** Se debe adjuntar únicamente el enlace (URL) a un **repositorio público de GitHub** que contenga el código fuente y las capturas solicitadas.
* **Horarios Límite e Incentivo de Bonificación:**
  * **Bonificación (+0.2 décimas):** Aquellas entregas realizadas **hasta las 11:00 hrs** que cumplan con la totalidad de los requerimientos solicitados obtendrán una bonificación de **2 décimas** en la nota de la actividad.
  * **Cierre Definitivo:** El plazo máximo e improrrogable para subir la entrega a Educa finaliza a las **11:10 hrs**.
* **Condición de Evaluación:** Para optar a la evaluación y a la bonificación, el proyecto entregado debe cumplir rigurosamente con el 100% de lo solicitado.

---

### **Entregables**

1. **Código Fuente:** Archivos de código completo, estructurado y documentado dentro del repositorio público.
2. **Evidencia de Ejecución:** Captura de pantalla (*screenshot*) subida al repositorio que demuestre el correcto funcionamiento de la calculadora y la vista secundaria.
3. **Enlace en Educa:** URL del repositorio público de GitHub registrada en Educa (Blackboard) dentro del horario habilitado.

---

### **Criterios de Logro**

- [ ] **Estructuración de Grid:** `GridLayout` definido explícitamente en una matriz de 4 columnas por 5 filas.
- [ ] **Configuración de `BoxLayout`:** Implementación del layout secundario con definición explícita de `orientation` (vertical), `spacing` y `padding`.
- [ ] **Lógica Aritmética Completa:** Procesamiento funcional de suma, resta, multiplicación, división, decimales y borrado.
- [ ] **Renderizado Dinámico:** Actualización correcta de valores y resultados dentro del `Label`.
- [ ] **Entrega en Regla:** Registro oportuno del repositorio público de GitHub en Educa antes de las 11:10 hrs (bonificación aplicable si se entrega antes de las 11:00 hrs cumpliendo todo lo solicitado).

---

*TINF1119 · Sesión 11 · GA v3.0 · Cristian Iglesias Vera — Instituto Tecnológico UC Temuco*