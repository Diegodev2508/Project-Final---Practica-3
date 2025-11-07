# 🎮 Ajedrez - Analizador FEN
Esta es una alternativa mucho mejor del ajedrez
Un juego de ajedrez con un analizador sintáctico (parser) de cadenas FEN con una interfaz gráfica 

## ✨ Características

- **Parser FEN completo**: Analiza y carga posiciones de ajedrez desde cadenas FEN
- **Interfaz gráfica moderna**: Tablero visual con colores tradicionales (blanco y negro)
- **Símbolos Unicode**: Piezas representadas con símbolos Unicode elegantes
- **Información en tiempo real**: Muestra el FEN actual y estadísticas del tablero
- **Fácil de usar**: Interfaz intuitiva para cargar y visualizar posiciones

## 📋 Requisitos

- Python 3.6 o superior
- tkinter (incluido en la mayoría de instalaciones de Python)

## 🚀 Instalación

1. Clona o descarga este repositorio


## 💻 Uso

Ejecuta la aplicación con:

```bash
python main.py
```

O directamente:

```bash
python chess_gui.py
```

## 📖 Formato FEN

FEN (Forsyth-Edwards Notation) es un formato estándar para describir posiciones de ajedrez.

**Ejemplo de posición inicial:**
```
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

**Componentes de una cadena FEN:**
1. **Posición del tablero**: `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR`
   - Letras mayúsculas = piezas blancas
   - Letras minúsculas = piezas negras
   - Números = casillas vacías consecutivas
   - `/` = separador de filas

2. **Color activo**: `w` (blanco) o `b` (negro)

3. **Derechos de enroque**: `KQkq` (todos), `-` (ninguno)

4. **Captura al paso**: Casilla o `-`

5. **Contador de medio movimiento**: Número

6. **Número de movimiento completo**: Número

## 🎯 Ejemplos de FEN

**Posición inicial:**
```
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

**Posición después de 1.e4:**
```
rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1
```

**Jaque mate (Fool's Mate):**
```
rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 1 3
```

## 📁 Estructura del Proyecto

```
Ajedrez/
├── main.py           # Punto de entrada principal
├── chess_gui.py      # Interfaz gráfica
├── chess_board.py    # Lógica del tablero
├── fen_parser.py     # Parser FEN
├── requirements.txt  # Dependencias (vacío - usa stdlib)
└── README.md         # Este archivo
```

## 🎨 Características de la Interfaz

- **Colores tradicionales**: Tablero con casillas beige claro (#F0D9B5) y marrón (#B58863)
- **Tema oscuro**: Interfaz con fondo oscuro para mejor experiencia visual
- **Símbolos Unicode**: Piezas representadas con símbolos Unicode elegantes
- **Etiquetas**: Filas (1-8) y columnas (a-h) para referencia
- **Panel de información**: Muestra FEN actual y estadísticas de piezas

## 🔧 Desarrollo

El proyecto está organizado en módulos:

- `fen_parser.py`: Parser completo de cadenas FEN
- `chess_board.py`: Lógica del tablero y gestión de posiciones
- `chess_gui.py`: Interfaz gráfica con tkinter
- `main.py`: Punto de entrada de la aplicación

## 📝 Notas

- Las piezas se representan con símbolos Unicode que pueden variar según la fuente
- El tablero sigue la convención estándar: a1 es negra, h8 es negra
- El parser FEN es completo y soporta todos los componentes del formato estándar

## 🎮 Controles

- **Cargar FEN**: Ingresa una cadena FEN y presiona "Cargar FEN" o Enter
- **Posición Inicial**: Restablece el tablero a la posición inicial
- **FEN Actual**: Se actualiza automáticamente al cargar nuevas posiciones



---
Muchas Gracias 
Y
¡Disfruta del ajedrez! ♟️

