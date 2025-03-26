class Cell:
    def __init__(self, row, column):
        self.hasBomb = False
        self.isOpen = False
        self.bombsAround = 0
        self.row = row
        self.column = column
        self.neighbors = []
    
    def count_bombs_around(self):
        for neighbor in self.neighbors:
            if neighbor.hasBomb:
                self.bombsAround += 1

    def assign_neighbors(self, neighbors: list):
        self.neighbors = neighbors
    
    def open_cell(self):
        if self.isOpen == True:
            return False
        else:
            self.isOpen = True
            return True
    
    def open_neighbors(self):
        if self.bombsAround == 0:
            for neighbor in self.neighbors:
                if not neighbor.hasBomb and not neighbor.isOpen:
                    neighbor.open_cell()
                    if neighbor.bombsAround == 0:
                        neighbor.open_neighbors()