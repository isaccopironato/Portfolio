class tiktaktoe:
    def __init__(self) -> None:
        self.board = [["_","_","_"],["_","_","_"],["_","_","_"]]

    def print_board(self) -> None:
        print()
        for i in range(0,3):
            for j in range(0,3): 
                print(self.board[i][j], end=" ")
            print()
        print()

    def place_tik(self, row, col, val):
        self.board[row][col] = val

    def find_empty(self):
        for row in range(0,3):
            for col in range(0,3): 
                if self.board[row][col] == "_":
                    return row, col
        return False
    
    def emty_col(self, col): 
        for i in range(0,3):
            if self.board[i][col] == "_":
                return i
        return False
    
    def emty_row(self, row): 
        for i in range(0,3):
            if self.board[row][i] == "_":
                return i
        return False
    
    def emty_dig_1(self):
        if self.board[0][0] == "_":
            return 0,0
        if self.board[1][1] == "_":
            return 1,1
        if self.board[2][2] == "_":
            return 2,2 
        return False
    
    def emty_dig_2(self):
        if self.board[2][0] == "_":
            return 2,0
        if self.board[1][1] == "_":
            return 1,1 
        if self.board[0][2] == "_":
            return 0,2
        return False
    
    def place_tak(self):
        b = self.board
        if b[0][0] == "_":
            b[0][0] = "O"
            return True
        elif b[2][2] == "_":
            b[2][2] = "O"
            return True
        elif b[0][2] == "_":
            b[0][2] = "O"
            return True
        elif b[2][0] == "_":
            b[2][0] = "O"
            return True
        return False

    def place_rand(self):
        row, col = self.find_empty()
        self.board[row][col] = "O"

    def decide_play_move(self):
        if self.att_or_def("O"):
            return
        elif self.att_or_def("X"):
            return
        elif self.place_tak():
            return
        self.place_rand()

    def att_or_def(self, val):
        dig_1 = 0
        dig_2 = 0
        for i in range(0,3):
            col = 0
            row = 0
            # find if about to score 
            for j in range(0,3):
                # dig
                # row 
                if self.board[i][j] == val:
                    row += 1
                    if i == j:
                        dig_1 += 1
                    # dig 2 
                        if i == 2:
                            dig_2 += 1
                    if i == 0 and j == 3:
                        dig_2 += 1
                    elif i == 3 and j == 0:
                        dig_2 += 1
                # col 
                if self.board[j][i] == val:
                    col += 1 
        # place a defensive move
            if col > 1:
                if self.emty_col(i) != False:
                    self.board[self.emty_col(i)][i] = "O"
                    return True
            if row > 1:
                if self.emty_row(i) != False:
                    self.board[i][self.emty_row(i)] = "O"
                    return True
            
        if dig_1 > 1:
            if self.emty_dig_1() != False:
                row, col = self.emty_dig_1()
                self.board[row][col] = "O"
                return True
            
        if dig_2 > 1:
            if self.emty_dig_2() != False:
                row, col = self.emty_dig_2()
                self.board[row][col] = "O"
                return True 
        return False


    def count_emty(self):
        count = 0
        for i in self.board:
            count += i.count("_")
        return count
    
    def game_runner(self):

        while self.count_emty() > 0:

            self.print_board()
            row = int(input("row (0-2): "))
            col = int(input("col (0-2): "))

            if col > 2 or col < 0 or row < 0 or row > 2:
                print("out of range")
            else: 
                self.board[row][col] = "X"
                self.print_board()
                self.decide_play_move()



if __name__ == "__main__":

    game = tiktaktoe()
    game.game_runner()