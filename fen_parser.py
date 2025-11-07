"""
Analizador sintáctico (parser) de cadenas FEN (Forsyth-Edwards Notation)
para posiciones de ajedrez.
"""


class FENParser:
    """Parser para cadenas FEN que describe posiciones de ajedrez."""
    
    # Mapeo de caracteres FEN a nombres de piezas
    PIECE_MAP = {
        'K': 'white_king', 'Q': 'white_queen', 'R': 'white_rook',
        'B': 'white_bishop', 'N': 'white_knight', 'P': 'white_pawn',
        'k': 'black_king', 'q': 'black_queen', 'r': 'black_rook',
        'b': 'black_bishop', 'n': 'black_knight', 'p': 'black_pawn'
    }
    
    def __init__(self, fen_string=None):
        """
        Inicializa el parser FEN.
        
        Args:
            fen_string: Cadena FEN opcional para parsear inmediatamente
        """
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.active_color = 'white'
        self.castling_rights = {'K': False, 'Q': False, 'k': False, 'q': False}
        self.en_passant = None
        self.halfmove_clock = 0
        self.fullmove_number = 1
        
        if fen_string:
            self.parse(fen_string)
    
    def parse(self, fen_string):
        """
        Parsea una cadena FEN completa.
        
        Formato FEN: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        
        Args:
            fen_string: Cadena FEN a parsear
        """
        parts = fen_string.strip().split()
        
        if len(parts) < 1:
            raise ValueError("FEN string debe contener al menos la posición del tablero")
        
        # Parte 1: Posición del tablero
        self._parse_board(parts[0])
        
        # Parte 2: Color activo (opcional)
        if len(parts) > 1:
            self.active_color = 'white' if parts[1] == 'w' else 'black'
        
        # Parte 3: Derechos de enroque (opcional)
        if len(parts) > 2:
            self._parse_castling(parts[2])
        
        # Parte 4: En passant (opcional)
        if len(parts) > 3:
            self._parse_en_passant(parts[3])
        
        # Parte 5: Contador de medio movimiento (opcional)
        if len(parts) > 4:
            self.halfmove_clock = int(parts[4]) if parts[4] != '-' else 0
        
        # Parte 6: Número de movimiento completo (opcional)
        if len(parts) > 5:
            self.fullmove_number = int(parts[5]) if parts[5] != '-' else 1
    
    def _parse_board(self, board_string):
        """
        Parsea la parte del tablero de la cadena FEN.
        
        Args:
            board_string: Parte del tablero (ej: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        """
        rows = board_string.split('/')
        
        if len(rows) != 8:
            raise ValueError(f"FEN debe tener 8 filas, se encontraron {len(rows)}")
        
        for row_idx, row in enumerate(rows):
            col_idx = 0
            for char in row:
                if char.isdigit():
                    # Número indica casillas vacías
                    col_idx += int(char)
                elif char in self.PIECE_MAP:
                    # Pieza encontrada
                    if col_idx < 8:
                        self.board[row_idx][col_idx] = self.PIECE_MAP[char]
                        col_idx += 1
                    else:
                        raise ValueError(f"Fila {row_idx} tiene más de 8 columnas")
                else:
                    raise ValueError(f"Carácter inválido en FEN: {char}")
            
            if col_idx != 8:
                raise ValueError(f"Fila {row_idx} no tiene exactamente 8 columnas")
    
    def _parse_castling(self, castling_string):
        """
        Parsea los derechos de enroque.
        
        Args:
            castling_string: String de enroque (ej: "KQkq" o "-")
        """
        self.castling_rights = {'K': False, 'Q': False, 'k': False, 'q': False}
        
        if castling_string != '-':
            for char in castling_string:
                if char in self.castling_rights:
                    self.castling_rights[char] = True
    
    def _parse_en_passant(self, en_passant_string):
        """
        Parsea la casilla de captura al paso.
        
        Args:
            en_passant_string: Casilla en passant (ej: "e3" o "-")
        """
        if en_passant_string == '-':
            self.en_passant = None
        else:
            if len(en_passant_string) == 2:
                self.en_passant = en_passant_string.lower()
            else:
                raise ValueError(f"En passant inválido: {en_passant_string}")
    
    def get_board(self):
        """
        Retorna el tablero como una matriz 8x8.
        
        Returns:
            Lista de listas con las piezas (None para casillas vacías)
        """
        return self.board
    
    def get_piece_at(self, row, col):
        """
        Obtiene la pieza en una posición específica.
        
        Args:
            row: Fila (0-7)
            col: Columna (0-7)
        
        Returns:
            Nombre de la pieza o None
        """
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def to_fen(self):
        """
        Convierte el estado actual a una cadena FEN.
        
        Returns:
            Cadena FEN representando el estado actual
        """
        # Construir parte del tablero
        board_parts = []
        for row in self.board:
            row_str = ""
            empty_count = 0
            for piece in row:
                if piece is None:
                    empty_count += 1
                else:
                    if empty_count > 0:
                        row_str += str(empty_count)
                        empty_count = 0
                    # Encontrar el carácter FEN correspondiente
                    for fen_char, piece_name in self.PIECE_MAP.items():
                        if piece_name == piece:
                            row_str += fen_char
                            break
            if empty_count > 0:
                row_str += str(empty_count)
            board_parts.append(row_str)
        
        fen = '/'.join(board_parts)
        
        # Agregar color activo
        fen += f" {'w' if self.active_color == 'white' else 'b'}"
        
        # Agregar enroque
        castling = ''.join([k for k, v in self.castling_rights.items() if v])
        fen += f" {castling if castling else '-'}"
        
        # Agregar en passant
        fen += f" {self.en_passant if self.en_passant else '-'}"
        
        # Agregar contadores
        fen += f" {self.halfmove_clock} {self.fullmove_number}"
        
        return fen

