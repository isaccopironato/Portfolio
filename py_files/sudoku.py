
class Sudokugame:

    def __init__(self, board) -> None:
        self.board = board

    def print_board(self):
        num = 1
        print()
        print("    1 2 3   4 5 6   7 8 9")
        print("----------------------------")
        for matrix in self.board:
            print(num, "|", end=" ")
            counter = 1
            for element in matrix: 
                print(element, end=" ")
                if counter%3 == 0: 
                    print("|", end=" ")
                counter += 1   
            print()
            if num%3 == 0:
                print("----------------------------")
            num += 1 
        print()

    def add_num(self, row = int, colum = int , num = int ) -> None:
        self.board[row-1][colum-1] = num

    def remuve_num(self, row = int, colum = int)-> None: 
        self.board[row-1][colum-1] = "#"

    def check_row(self, row) -> bool:
        unique = set(row)
        for i in unique:
            if i == "#":
                pass
            elif row.count(i) > 1: 
                return False
        return True

    def splice_board(self) -> tuple:
        board = self.board
        colum = []
        box = []
        top = []
        midle = []
        botom = []

        for col in range(1,10): 
            temp_col = []

            for row in range(1,10):
                temp_col.append(board[row-1][col-1])

                if row <= 3: 
                    top.append(board[row-1][col-1])

                elif row > 3 and row <= 6 :
                    midle.append(board[row-1][col-1])

                else: 
                    botom.append(board[row-1][col-1])

            colum.append(temp_col)

            if col%3 == 0:
                box.append(top)
                box.append(midle)
                box.append(botom)
                top = []
                midle = []
                botom = []

        return colum, box
    
#! stai ancora lavorando 
    def check_position(self, num,  row, colum) -> bool:

        # check row 
        for i in range(0,9):
        
            if self.board[row][i] == num and i != colum:
                return False
            
            # check colum 
            if self.board[i][colum] == num and i != row: 
                return False
            
        box_x = colum // 3
        box_y = row // 3

        # check box 
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != (row, colum):
                    return False

        return True
    
    def find_empty(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.board[row][col] == "#":
                    return row, col

        return None

    def sudoku_solver(self):

        if not self.find_empty():
            return True
        
        row, col = self.find_empty()

        for num in range(1,10):

            if self.check_position(num, row, col): 
                self.board[row][col] = num
            
                if self.sudoku_solver():
                    return True
                
                self.board[row][col] = "#"

        return False

    # non utilizzato 
    def test_ading_one_num(self)-> None: 
        row = self.board
        for y in range(1,10):
            for x in range(1,10):

                if row[y-1][x-1] == "#":
                    for i in range(1,10):

                        row[y-1][x-1] = i
                        if self.check_board():
                            break


#! stai ancora lavorando

    def check_board(self):
        colum, box = self.splice_board()
        for i in colum, box, self.board:
            for j in i:
                if self.check_row(j) == False:
                    return False
        return True

 
    def amount_of_mising_numbers(self) -> int:
        counter = 0
        for i in self.board:
            counter += i.count("#")
        return counter 
    
    def check_range(self, row = None, colum = None, num = None):

        if num == None: 
            num = 1 

        if colum not in range(1,10) or row not in range(1,10) or num not in range(1,10):
            return False
        return True



    def comands(self):
        print("0 exit")
        print("1 add num")
        print("2 remove one number")
        print("3 check if corect")
        print("4 solve board")
        print("5 ad one correct num")
        print("6 print comands")


    def game_runner(self):
        self.comands

        while self.amount_of_mising_numbers() > 0:

            self.print_board()

            comand = int(input("input comand: "))

            if comand == 0:
                print("game ended")
                return

            elif comand == 1:
                num = int(input("input nun: "))
                
                row = int(input("input row: "))

                colum = int(input("input column: "))

                if self.check_range(row, colum, num):
                    self.add_num(row, colum, num)
                else: 
                    print("out of range")

            elif comand == 2:
                row = int(input("input row: "))

                colum = int(input("input column: "))

                if self.check_range(row, colum):
                    self.remuve_num(row, colum)
                else: 
                    print("out of range")
                
            elif comand == 3: 
                if self.check_board():
                    print(True)
                else:
                    print(False)
            
            elif comand == 4: 
                self.sudoku_solver()
                self.print_board()
                return
            
            elif comand == 5: 
                # ad one correct number
                pass

            elif comand == 6: 
                self.comands()

            else: 
                print("wrong comand")

        if self.check_board():
            print("solved")
        else:
            print("not solved")


if __name__ == "__main__":
    board = [
        ["#","#","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"],       
        ["#","#","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"]
        ]

    board = Sudokugame(board)
    board.game_runner()