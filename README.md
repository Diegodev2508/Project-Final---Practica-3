♟️ **FEN Parser con Interfaz Gráfica en Python / FEN Parser with Graphical Interface in Python**
🧩 **Descripción del Proyecto / Project Description**
LINK DEL VIDEO: https://www.youtube.com/watch?v=VkwmqZ1_VWA&t=2s

Este proyecto implementa un **analizador de cadenas FEN (Forsyth–Edwards Notation)** en **Python**, con una **interfaz gráfica desarrollada en Tkinter**, capaz de:

- Validar y procesar cadenas FEN.  
- Mostrar visualmente un **tablero de ajedrez** a partir de la notación ingresada.  
- Permitir cambiar **temas** (simple / imágenes PNG) y **tamaños de las piezas**.  
- Generar íconos de piezas de forma programática o cargar imágenes desde la carpeta `assets/`.

---

This project implements a **FEN (Forsyth–Edwards Notation) string parser** in **Python**, with a **graphical interface built using Tkinter**, capable of:

- Validating and processing FEN strings.  
- Visually displaying a **chessboard** based on the input notation.  
- Allowing theme changes (simple / image-based) and adjustable piece sizes.  
- Generating chess piece icons programmatically or loading them from the `assets/` folder.

---

🧠 **Objetivos / Objectives**

✅ Analizar cadenas FEN con validaciones rigurosas.  
✅ Visualizar el tablero de ajedrez dinámicamente.  
✅ Aplicar conceptos de estructuras, clases, excepciones y GUI.  
✅ Fortalecer la comprensión del formato FEN y la manipulación de gráficos en Python.

✅ Parse FEN strings with strong validation.  
✅ Dynamically visualize the chessboard.  
✅ Apply concepts of data structures, classes, exceptions, and GUI.  
✅ Strengthen understanding of FEN format and graphical rendering in Python.

---

💻 **Lenguaje y Entorno / Language and Environment**

- 🐍 **Lenguaje / Language:** Python 3.14
- 🧰 **Entorno / IDE:** IntelliJ IDEA (Python Plugin)  
- 🎨 **Interfaz / GUI:** Tkinter + Pillow (PIL)  

 📂 **Estructura del Proyecto / Project Structure**
```
├── src/
│   └── fen_parser.py        # Analizador FEN con validaciones / FEN parser with validations
├── assets/
│   ├── wK.png ... bP.png    # Imágenes opcionales / Optional piece images
├── main.py                  # Interfaz gráfica principal / Main GUI
├── README.md
└── requirements.txt
```

---

⚙️ **Requisitos mínimos / Minimum Requirements**

- 🖥️ **SO / OS:** Windows, Linux, or macOS  
- **Python 3.11+**  
- **Dependencias / Dependencies:**
  ```bash
  pip install pillow
  ```

---

🧩 **Archivos principales / Main Files**

🧠 `src/fen_parser.py`
Analiza y valida la cadena FEN, detectando errores y lanzando excepciones personalizadas:  
Parses and validates FEN strings, detecting errors and raising custom exceptions such as:

- `FieldCountError`  
- `PiecePlacementError`  
- `SideToMoveError`  
- `CastlingError`  
- `EnPassantError`  
- `HalfmoveError`  
- `FullmoveError`

---

🎨 `main.py`
Interfaz gráfica Tkinter que:  
Tkinter graphical interface that:

- Muestra el tablero a partir de la cadena FEN / Displays the board from a FEN string.  
- Permite cambiar el tema y el tamaño de las piezas / Allows changing theme and piece size.  
- Maneja errores con ventanas emergentes / Handles errors via pop-up messages.  
- Genera piezas simples mediante gráficos o carga imágenes / Generates or loads chess pieces.

---

🖼️ **Ejemplo / Example**

FEN de inicio clásico / Classic starting position:
```
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

Resultado visual (modo *simple*) / Visual result (*simple* mode):  
![Ejemplo Tablero / Board Example](tablero_excel_fen.png)

---

🧑‍💻 **Integrantes / Team Members**

| Nombre / Name | Rol / Role | Programa / Program |
|----------------|-------------|--------------------|
| DIEGO CABALLERO| | Ingeniería de Sistemas / Systems Engineering |  EAFIT UNIVERSITY 

---

🎥 **Presentación del Proyecto / Project Presentation (70%)**

> El video de presentación se realizo en **inglés**, mostrando el propósito, ejecución y validación del programa.  
> The project presentation video is in **English**, explaining the purpose, execution, and validation of the program.

---

🧾 **Evaluación / Evaluation**

| Criterio / Criterion | Porcentaje / Percentage | Descripción / Description |
|-----------------------|--------------------------|----------------------------|
| 💡 Programa funcionando / Working program | **30%** | Analizador FEN y GUI operativa / Parser and GUI functional |
| 🎬 Video presentación / Presentation video | **70%** | Explicación completa y clara / Full clear demonstration |

---

📚 **Material de apoyo / Support Material**

- Archivo Excel para procesar cadenas FEN / Excel file for FEN processing.  
- Ejemplos de código y expresiones regulares del profesor / Teacher’s regex and code samples.  
- Repositorios y ejercicios vistos en clase / Class repositories and exercises.
- PDF y tutoriales para investigar

---

🕹️ **Ejecución / Run Instructions**

1. **Clona el repositorio / Clone the repository**
   ```bash
   git clone https://github.com/usuario/FEN-Parser.git
   cd FEN-Parser
   ```

2. **Instala dependencias / Install dependencies**
   ```bash
   pip install pillow
   ```

3. **Ejecuta el programa / Run the program**
   ```bash
   python main.py
   ```

---

🏁 **Créditos / Credits**

Diego caballero estudiante de **Ingeniería de Sistemas**  
Created **Systems Engineering** students.  
📅 *Entrega / Submission:* Semana 16 del curso / Week 16 of the course.

---
````
