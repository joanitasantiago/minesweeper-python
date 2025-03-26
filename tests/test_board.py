import pytest
import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.board import Board
from src.cell import Cell

def test_board_creation():
    board = Board(9,9)

    assert board.maxColumns == 9
    assert board.maxRows == 9

    assert len(board.cells) == 9
    assert all(len(row) == 9 for row in board.cells) 
# A função all(iterável) verifica se todos os elementos do iterável são True.
# Se TODOS forem True, ela retorna True. Se qualquer um for False, ela retorna False.

    assert isinstance(board.cells[0][0], Cell)
    assert isinstance(board.cells[8][8], Cell)
# A função isinstance(obj, classe) verifica se um objeto pertence a uma determinada classe.

def test_distribute_bombs():
    board = Board(9,9)
    amount_of_bombs_assigned = 0
    board.distribute_bombs(10)

    for row in range(board.maxRows):
        for column in range(board.maxColumns):
            if board.cells[row][column].hasBomb:
                amount_of_bombs_assigned += 1

    assert amount_of_bombs_assigned == 10

def get_bomb_positions(board):
    return {(row, column) for row in range(board.maxRows) for column in range(board.maxColumns) if board.cells[row][column].hasBomb}

    # Isso é um set comprehension. O Python já entende que {(row, col) for ...} deve criar um conjunto automaticamente.
    # set() → Quando precisamos de um conjunto vazio.
    # {} → Cria um dicionário, a menos que seja usado em um Set Comprehension.
    # {x for x in range(10)}	Conjunto
    # {}	Dicionário vazio 

def test_distribute_bombs_randomness():
    board1 = Board(9,9)
    board2 = Board(9,9)

    board1.distribute_bombs(10)
    board2.distribute_bombs(10)

    positions1 = get_bomb_positions(board1)
    positions2 = get_bomb_positions(board2)
    
    assert positions1 != positions2

def test_validate_bomb_limit():
    board = Board(9,9)
    bombs = board.maxRows * board.maxColumns + 1

    with pytest.raises(ValueError, match="Número de bombas"):  
        board.distribute_bombs(bombs)

    # Normalmente usamos assert para comparar valores.
    # Mas neste caso, não estamos verificando um valor retornado.
    # Em vez disso, estamos testando se um erro (ValueError) é levantado corretamente.
    # O pytest.raises(ValueError) já faz essa verificação para nós. 
    # Se distribute_bombs(bombs) não lançar um ValueError, o teste falhará automaticamente.