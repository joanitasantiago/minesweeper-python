import pytest
import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.cell import Cell

def test_cell_initialization():
    cell = Cell(2, 3)

    assert cell.row == 2
    assert cell.column == 3
    assert cell.hasBomb is False
    assert cell.isOpen is False
    assert cell.bombsAround == 0
    assert cell.neighbors == []

def test_assign_neighbors():
    cell = Cell(0, 0)
    
    neighbors = [Cell(0, 1), Cell(1, 0), Cell(1, 1)]

    cell.assign_neighbors(neighbors)

    assert len(cell.neighbors) == 3
    assert cell.neighbors == neighbors

def test_count_bombs_around():
    cell = Cell(0, 0)
    
    neighbor1 = Cell(0, 1)
    neighbor2 = Cell(1, 0)
    neighbor3 = Cell(1, 1)

    neighbor1.hasBomb = True

    neighbors = [neighbor1, neighbor2, neighbor3]
    cell.assign_neighbors(neighbors)
    
    cell.count_bombs_around()

    assert cell.bombsAround == 1

def test_open_cell():
    cell = Cell(0, 0)

    assert cell.open_cell() == True
    assert cell.isOpen == True
    assert cell.open_cell() == False

def test_open_neighbors():
    pass