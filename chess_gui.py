"""
Interfaz gráfica bonita para el juego de ajedrez con parser FEN.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from chess_board import ChessBoard


class ChessGUI:
    """Interfaz gráfica para el tablero de ajedrez."""
    
    # Símbolos Unicode para las piezas de ajedrez
    PIECE_SYMBOLS = {
        'white_king': '♔', 'white_queen': '♕', 'white_rook': '♖',
        'white_bishop': '♗', 'white_knight': '♘', 'white_pawn': '♙',
        'black_king': '♚', 'black_queen': '♛', 'black_rook': '♜',
        'black_bishop': '♝', 'black_knight': '♞', 'black_pawn': '♟'
    }
    
    # Colores del tablero
    LIGHT_SQUARE = '#F0D9B5'  # Beige claro
    DARK_SQUARE = '#B58863'   # Marrón
    
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica.
        
        Args:
            root: Ventana principal de tkinter
        """
        self.root = root
        self.root.title("Ajedrez - Analizador FEN")
        self.root.geometry("900x700")
        self.root.configure(bg='#2C2C2C')
        
        # Inicializar tablero
        self.chess_board = ChessBoard()
        
        # Variables
        self.square_size = 60
        self.board_offset_x = 20
        self.board_offset_y = 20
        
        # Crear interfaz
        self._create_widgets()
        self._draw_board()
    
    def _create_widgets(self):
        """Crea todos los widgets de la interfaz."""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2C2C2C')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame del tablero
        board_frame = tk.Frame(main_frame, bg='#2C2C2C')
        board_frame.pack(side=tk.LEFT, padx=10)
        
        # Canvas para el tablero
        canvas_size = self.square_size * 8 + 40
        self.canvas = tk.Canvas(
            board_frame,
            width=canvas_size,
            height=canvas_size,
            bg='#1E1E1E',
            highlightthickness=2,
            highlightbackground='#4A4A4A'
        )
        self.canvas.pack()
        
        # Frame de controles
        control_frame = tk.Frame(main_frame, bg='#2C2C2C')
        control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        # Título
        title_label = tk.Label(
            control_frame,
            text="Analizador FEN",
            font=('Arial', 18, 'bold'),
            bg='#2C2C2C',
            fg='#FFFFFF'
        )
        title_label.pack(pady=(0, 20))
        
        # Entrada FEN
        fen_label = tk.Label(
            control_frame,
            text="Cadena FEN:",
            font=('Arial', 11, 'bold'),
            bg='#2C2C2C',
            fg='#FFFFFF',
            anchor='w'
        )
        fen_label.pack(fill=tk.X, pady=(0, 5))
        
        self.fen_entry = tk.Entry(
            control_frame,
            font=('Courier', 10),
            bg='#1E1E1E',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            relief=tk.FLAT,
            bd=5
        )
        self.fen_entry.pack(fill=tk.X, pady=(0, 10))
        self.fen_entry.insert(0, ChessBoard.STARTING_POSITION)
        self.fen_entry.bind('<Return>', lambda e: self.load_fen())
        
        # Botones
        button_frame = tk.Frame(control_frame, bg='#2C2C2C')
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        load_button = tk.Button(
            button_frame,
            text="Cargar FEN",
            command=self.load_fen,
            font=('Arial', 11, 'bold'),
            bg='#4A90E2',
            fg='#FFFFFF',
            activebackground='#357ABD',
            activeforeground='#FFFFFF',
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        load_button.pack(side=tk.LEFT, padx=(0, 10))
        
        reset_button = tk.Button(
            button_frame,
            text="Posición Inicial",
            command=self.reset_board,
            font=('Arial', 11, 'bold'),
            bg='#50C878',
            fg='#FFFFFF',
            activebackground='#3FA068',
            activeforeground='#FFFFFF',
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        reset_button.pack(side=tk.LEFT)
        
        # FEN actual
        current_fen_label = tk.Label(
            control_frame,
            text="FEN Actual:",
            font=('Arial', 11, 'bold'),
            bg='#2C2C2C',
            fg='#FFFFFF',
            anchor='w'
        )
        current_fen_label.pack(fill=tk.X, pady=(20, 5))
        
        self.current_fen_text = scrolledtext.ScrolledText(
            control_frame,
            height=3,
            font=('Courier', 9),
            bg='#1E1E1E',
            fg='#FFFFFF',
            wrap=tk.WORD,
            relief=tk.FLAT,
            bd=5
        )
        self.current_fen_text.pack(fill=tk.X, pady=(0, 20))
        self.current_fen_text.config(state=tk.DISABLED)
        
        # Información del tablero
        info_label = tk.Label(
            control_frame,
            text="Información:",
            font=('Arial', 11, 'bold'),
            bg='#2C2C2C',
            fg='#FFFFFF',
            anchor='w'
        )
        info_label.pack(fill=tk.X, pady=(0, 5))
        
        info_frame = tk.Frame(control_frame, bg='#1E1E1E', relief=tk.FLAT, bd=5)
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        self.info_text = tk.Text(
            info_frame,
            font=('Arial', 10),
            bg='#1E1E1E',
            fg='#FFFFFF',
            wrap=tk.WORD,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.info_text.pack(fill=tk.BOTH, expand=True)
        self.info_text.config(state=tk.DISABLED)
        
        # Actualizar información inicial
        self.update_info()
    
    def _draw_board(self):
        """Dibuja el tablero de ajedrez y las piezas."""
        self.canvas.delete("all")
        
        # Dibujar casillas
        for row in range(8):
            for col in range(8):
                x1 = self.board_offset_x + col * self.square_size
                y1 = self.board_offset_y + row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                # Determinar color de la casilla
                is_light = self.chess_board.is_white_square(row, col)
                color = self.LIGHT_SQUARE if is_light else self.DARK_SQUARE
                
                # Dibujar casilla
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline=color,
                    tags='square'
                )
                
                # Dibujar pieza si existe
                piece = self.chess_board.get_piece_at(row, col)
                if piece:
                    symbol = self.PIECE_SYMBOLS.get(piece, '')
                    if symbol:
                        # Color del texto (negro para piezas blancas, blanco para piezas negras)
                        text_color = '#000000' if piece.startswith('white') else '#FFFFFF'
                        
                        # Centrar el símbolo en la casilla
                        center_x = x1 + self.square_size // 2
                        center_y = y1 + self.square_size // 2
                        
                        self.canvas.create_text(
                            center_x, center_y,
                            text=symbol,
                            font=('Arial', int(self.square_size * 0.7), 'bold'),
                            fill=text_color,
                            tags='piece'
                        )
        
        # Dibujar etiquetas de filas y columnas
        self._draw_labels()
    
    def _draw_labels(self):
        """Dibuja las etiquetas de filas (1-8) y columnas (a-h)."""
        # Etiquetas de columnas (a-h) en la parte inferior
        for col in range(8):
            x = self.board_offset_x + col * self.square_size + self.square_size // 2
            y = self.board_offset_y + 8 * self.square_size + 15
            label = chr(ord('a') + col)
            self.canvas.create_text(
                x, y,
                text=label,
                font=('Arial', 12, 'bold'),
                fill='#FFFFFF',
                tags='label'
            )
        
        # Etiquetas de filas (1-8) en el lado izquierdo
        for row in range(8):
            x = self.board_offset_x - 10
            y = self.board_offset_y + row * self.square_size + self.square_size // 2
            label = str(8 - row)
            self.canvas.create_text(
                x, y,
                text=label,
                font=('Arial', 12, 'bold'),
                fill='#FFFFFF',
                tags='label'
            )
    
    def load_fen(self):
        """Carga una posición desde la cadena FEN ingresada."""
        fen_string = self.fen_entry.get().strip()
        
        if not fen_string:
            messagebox.showerror("Error", "Por favor ingresa una cadena FEN válida.")
            return
        
        try:
            self.chess_board.load_fen(fen_string)
            self._draw_board()
            self.update_info()
            messagebox.showinfo("Éxito", "Posición FEN cargada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar FEN:\n{str(e)}")
    
    def reset_board(self):
        """Resetea el tablero a la posición inicial."""
        self.chess_board = ChessBoard()
        self.fen_entry.delete(0, tk.END)
        self.fen_entry.insert(0, ChessBoard.STARTING_POSITION)
        self._draw_board()
        self.update_info()
    
    def update_info(self):
        """Actualiza la información mostrada sobre el tablero."""
        # Actualizar FEN actual
        self.current_fen_text.config(state=tk.NORMAL)
        self.current_fen_text.delete(1.0, tk.END)
        self.current_fen_text.insert(1.0, self.chess_board.get_fen())
        self.current_fen_text.config(state=tk.DISABLED)
        
        # Actualizar información
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        
        info = []
        info.append("═" * 40)
        info.append("INFORMACIÓN DEL TABLERO")
        info.append("═" * 40)
        info.append("")
        
        # Contar piezas
        piece_count = {}
        for row in range(8):
            for col in range(8):
                piece = self.chess_board.get_piece_at(row, col)
                if piece:
                    piece_count[piece] = piece_count.get(piece, 0) + 1
        
        info.append("Piezas en el tablero:")
        info.append("")
        
        # Piezas blancas
        white_pieces = {k: v for k, v in piece_count.items() if k.startswith('white')}
        if white_pieces:
            info.append("  Blancas:")
            for piece, count in sorted(white_pieces.items()):
                piece_name = piece.replace('white_', '').capitalize()
                symbol = self.PIECE_SYMBOLS.get(piece, '')
                info.append(f"    {symbol} {piece_name}: {count}")
        
        info.append("")
        
        # Piezas negras
        black_pieces = {k: v for k, v in piece_count.items() if k.startswith('black')}
        if black_pieces:
            info.append("  Negras:")
            for piece, count in sorted(black_pieces.items()):
                piece_name = piece.replace('black_', '').capitalize()
                symbol = self.PIECE_SYMBOLS.get(piece, '')
                info.append(f"    {symbol} {piece_name}: {count}")
        
        info.append("")
        info.append("═" * 40)
        
        self.info_text.insert(1.0, '\n'.join(info))
        self.info_text.config(state=tk.DISABLED)


def main():
    """Función principal para ejecutar la aplicación."""
    root = tk.Tk()
    app = ChessGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

