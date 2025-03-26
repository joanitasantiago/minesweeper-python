from board import Board

class Game:

    def __init__(self):
        self.gameOver = False
        self.keepPlaying = True
        self.difficulty = 1
        self.bombs = 10
        self.selectedColumn = None
        self.selectedRow = None
        self.gameBoard = Board(9,9)
    
    def game_start(self):
        while self.keepPlaying:
            self.reset_game()
            self.first_move()
            while not self.gameOver:
                self.gameBoard.print_board()
                self.validate_open_cell()
                if self.gameOver:
                    break
                self.gameBoard.cells[self.selectedRow][self.selectedColumn].open_neighbors()
                self.is_the_game_over()
            self.get_play_again()

    def first_move(self):
        self.get_valid_game_difficulty()
        self.create_game_board()
        self.gameBoard.assign_all_neighbors()
        self.gameBoard.print_board()
        self.validate_open_cell()
        self.gameBoard.distribute_bombs(self.bombs, exclude=(self.selectedRow, self.selectedColumn))
        self.gameBoard.update_bomb_counts()
        self.gameBoard.cells[self.selectedRow][self.selectedColumn].open_neighbors()

    def get_valid_game_difficulty(self):
        errorMsg = "Entrada inválida! Digite 1 para FÁCIL, 2 para INTERMEDIÁRIO ou 3 para EXPERT."
        max_attempts = 15
        attempts = 0

        while attempts < max_attempts:
            try:
                difficulty = int(input("Em qual nível você quer jogar? Digite 1 para FÁCIL, 2 para INTERMEDIÁRIO ou 3 para EXPERT: "))
                if difficulty not in (1, 2, 3):
                    print(errorMsg)
                else:
                    self.difficulty = difficulty
                    return
            except ValueError:
                print(errorMsg)
            attempts += 1
        
        self.end_program()
    
    def create_game_board(self):
        match self.difficulty:
            case 1:
                self.bombs = 10;
                self.gameBoard = Board(9,9)
            case 2:
                self.bombs = 40;
                self.gameBoard = Board(16,16)
            case 3:
                self.gameBoard = Board(30,16)
                self.bombs = 99;

    def get_valid_row(self):

        limit = self.gameBoard.maxRows
        max_attempts = 15
        attempts = 0

        while attempts < max_attempts:
            try:
                self.selectedRow = int(input("Vamos abrir uma célula! Digite a linha: "))
                if self.selectedRow not in range(limit):
                    print(f"Linha fora dos limites do tabuleiro. Escolha um valor entre 0 e {limit - 1}: ")
                else:
                    return
            except ValueError:
                print("Entrada inválida! Digite apenas números")
            attempts += 1
        
        self.end_program()

    def get_valid_column(self):

        limit = self.gameBoard.maxColumns
        max_attempts = 15
        attempts = 0

        while attempts < max_attempts:
            try:
                self.selectedColumn = int(input("Vamos abrir uma célula! Digite a coluna: "))
                if self.selectedColumn not in range(limit):
                    print(f"Coluna fora dos limites do tabuleiro. Escolha um valor entre 0 e {limit - 1}: ")
                else:
                    return
            except ValueError:
                print("Entrada inválida! Digite apenas números")
            attempts += 1

        self.end_program()
    
    def validate_open_cell(self):
        while True:
            self.get_valid_row()
            if self.gameOver:
                return
            self.get_valid_column()
            if self.gameOver:
                return
            validation = self.gameBoard.cells[self.selectedRow][self.selectedColumn].open_cell()
            if not validation:
                print("Célula já está aberta. Tente novamente")
            else:
                break
    
    def check_if_its_bomb(self):
        if self.gameBoard.cells[self.selectedRow][self.selectedColumn].hasBomb:
            return True
        else:
            return False
    
    def check_victory(self):
        if self.gameBoard.check_if_all_safe_cells_are_open() == True:
            return True
        else:
            return False    
    
    def is_the_game_over(self):

        exploded = self.check_if_its_bomb()
        if exploded:
            print("\t\n~~~ BOOOOOOM ~~~ \t\n ~~~ VOCÊ PERDEU ~~~")
            self.end_game_match()
            return

        won = self.check_victory()
        if won:
            print("\t\n~~~ PARABÉNS ~~~ \t\n ~~~ VOCÊ VENCEU ~~~ ")
            self.end_game_match()

    def end_game_match(self):
        self.gameBoard.open_all_cells()
        self.gameBoard.print_board()
        self.gameOver = True

    def end_program(self):
        print("Número máximo de tentativas atingido. Encerrando o jogo.")
        self.gameOver = True
    
    def reset_game(self):
        self.gameOver = False
        self.keepPlaying = True
        self.difficulty = 1
        self.bombs = 10
        self.selectedColumn = None
        self.selectedRow = None
        self.gameBoard = Board(9, 9)

    def get_play_again(self):
        errorMsg = "Entrada inválida! Digite 1 para jogar novamente ou 0 para sair."
        while True:
            try:
                option = int(input("Digite 1 para jogar novamente ou 0 para fechar o jogo: "))
                if option not in (0, 1):
                    print(errorMsg)
                elif option == 0:
                    print("Até a próxima!")
                    self.keepPlaying = False
                    break
                elif option == 1:
                    print("\t\n~~~ REINICIANDO O JOGO ~~~\t\n")
                    self.keepPlaying = True
                    break
            except ValueError:
                print(errorMsg)