import random
from cell import Cell

class Board:
    def __init__(self, maxRows, maxColumns):
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.cells = []
        self.create_board()
    
    def create_board(self):
        self.cells = [[Cell(row, column) for column in range(self.maxColumns)] for row in range(self.maxRows)]

    def assign_all_neighbors(self):
        for row in range(self.maxRows):
            for col in range(self.maxColumns):
                cell = self.cells[row][col]
                neighbors = []
                # Percorre os 8 possíveis vizinhos ao redor
                for row_offset in [-1, 0, 1]:         # linha acima, mesma linha, linha abaixo
                    for col_offset in [-1, 0, 1]:     # coluna à esquerda, mesma coluna, coluna à direita
                        if row_offset == 0 and col_offset == 0:
                            continue  # ignora a própria célula
                        neighbor_row = row + row_offset
                        neighbor_col = col + col_offset
                        # Verifica se está dentro dos limites do tabuleiro
                        if 0 <= neighbor_row < self.maxRows and 0 <= neighbor_col < self.maxColumns:
                            neighbor_cell = self.cells[neighbor_row][neighbor_col]
                            neighbors.append(neighbor_cell)
                # Atribui os vizinhos à célula atual
                cell.neighbors = neighbors

    def validate_bomb_limit(self, bombs):
        maxBombs = self.maxRows * self.maxColumns
        if bombs > maxBombs:
            raise ValueError(f"Número de bombas ({bombs}) excede o limite de {maxBombs} células!")
        
    def distribute_bombs(self, bombs):
        self.validate_bomb_limit(bombs)
        
        i = 0
        while (i < bombs):
            newRow = random.randint(0, self.maxRows - 1)
            newColumn = random.randint(0, self.maxColumns - 1)

            if not self.cells[newRow][newColumn].isOpen and not self.cells[newRow][newColumn].hasBomb:
                self.cells[newRow][newColumn].hasBomb = True
                i += 1

    def update_bomb_counts(self):
        for row in range(self.maxRows):
            for column in range(self.maxColumns):
                self.cells[row][column].count_bombs_around()

    def open_all_cells(self):
        for row in range(self.maxRows):
            for column in range(self.maxColumns):
                self.cells[row][column].open_cell()
    
    def check_if_all_safe_cells_are_open(self):
        validation = True
        for row in range(self.maxRows):
            for column in range(self.maxColumns):
                if self.cells[row][column].hasBomb == False and self.cells[row][column].isOpen == False:
                    validation = False
        return validation

    def print_board(self):
        self.print_column_index()
        self.print_line()
        for row in range(self.maxRows):
            self.print_row_index(row)
            for column in range(self.maxColumns):
                if not self.cells[row][column].isOpen:
                    print("|_|", end = "")
                elif self.cells[row][column].hasBomb:
                    print("|*|", end = "")
                else:
                    print(f"|{self.cells[row][column].bombsAround}|", end = "")
            print()    
    
    def print_column_index(self):
        print("\t", end = "")
        for column in range(self.maxColumns):
            print(f"[{column}]", end = "")
        print()
        print()

    def print_row_index(self, row):
        print(f"[{row}]\t", end = "")

    def print_line(self):
        print("\t", end = "")
        for column in range(self.maxColumns):
            print(" _ ", end ="")
        print()