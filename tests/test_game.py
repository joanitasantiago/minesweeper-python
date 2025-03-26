import pytest
from src.game import Game

def test_game_initialization():
    game = Game()
    assert game.gameOver == False
    assert game.keepPlaying == True
    assert game.difficulty == 1
    assert game.bombs == 10
    assert game.selectedRow == 0
    assert game.selectedColumn == 0

def test_game_victory():
    game = Game()
    game.create_game_board()
    for row in range(game.gameBoard.maxRows):
        for col in range(game.gameBoard.maxColumns):
            if not game.gameBoard.cells[row][col].hasBomb:
                game.gameBoard.cells[row][col].isOpen = True
    assert game.check_victory() == True

def test_game_defeat():
    game = Game()
    game.create_game_board()
    game.gameBoard.cells[0][0].hasBomb = True
    game.selectedRow = 0
    game.selectedColumn = 0
    assert game.check_if_its_bomb() == True