"""
Lógica del tablero de ajedrez y representación de piezas.
"""

from fen_parser import FENParser


class ChessBoard:
    """Representa un tablero de ajedrez con soporte FEN."""
    
    # Posición inicial estándar
    STARTING_POSITION = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    
    def __init__(self, fen_string=None):
        """
        Inicializa el tablero de ajedrez.
        
        Args:
            fen_string: Cadena FEN opcional (usa posición inicial si es None)
        """
        if fen_string is None:
            fen_string = self.STARTING_POSITION
        
        self.parser = FENParser(fen_string)
        self.board = self.parser.get_board()
    
    def get_board(self):
        """Retorna el tablero actual."""
        return self.board
    
    def get_piece_at(self, row, col):
        """
        Obtiene la pieza en una posición específica.
        
        Args:
            row: Fila (0-7, donde 0 es la fila superior)
            col: Columna (0-7, donde 0 es la columna izquierda)
        
        Returns:
            Nombre de la pieza o None
        """
        return self.parser.get_piece_at(row, col)
    
    def load_fen(self, fen_string):
        """
        Carga una posición desde una cadena FEN.
        
        Args:
            fen_string: Cadena FEN a cargar
        """
        self.parser.parse(fen_string)
        self.board = self.parser.get_board()
    
    def get_fen(self):
        """
        Obtiene la representación FEN del tablero actual.
        
        Returns:
            Cadena FEN
        """
        return self.parser.to_fen()
    
    def is_white_square(self, row, col):
        """
        Determina si una casilla es blanca o negra.
        En ajedrez, a1 (0,0) es negra.
        
        Args:
            row: Fila (0-7)
            col: Columna (0-7)
        
        Returns:
            True si es casilla blanca, False si es negra
        """
        return (row + col) % 2 == 1

