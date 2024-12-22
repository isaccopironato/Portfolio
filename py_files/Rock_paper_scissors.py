from random import randrange

class rps:
    def __init__(self):
        self.player_input = None
        self.npc_input = None

    def player(self):
        p = ""
        while True:
            if p == "rock":
                break
            elif p == "paper":
                break
            elif p == "scissors":
                break

            print("play rock, paper or scissors")
            print(p)
            p = input()

        self.player_input = p

    def npc(self):
        
        p = randrange(1,4)

        if p == 1:
            p = "rock"
        elif p == 2:
            p = "paper"
        else: 
            p = "scissors"

        self.npc_input = p

    def winer(self, npc, player):
        n = 0
        p = 0

        # words to numbers 
        if npc == "rock":
            n = 1
        elif npc == "paper":
            n = 2
        else: 
            n = 3

        if player == "rock":
            p = 1
        elif player == "paper":
            p = 2
        else: 
            p = 3

        # decide the winner
        # 1 = rock
        # 2 = paper
        # 3 = scissors

        if n == 1:
            if p == 2:
                w = "NPC Wins"
            elif p == 3:
                w = "You Win"
            else:
                w = "TIE"

        elif n == 2:
            if p == 1:
                w = "NPC Wins"
            elif p == 3:
                w = "You Win"
            else:
                w = "TIE"

        else:
            if p == 1:
                w = "You Win"
            elif p == 2:
                w = "NPC Wins"
            else:
                w = "TIE"
        print("NPC Played", self.npc_input)
        print("Player played", self.player_input)
        print(w)

    def game(self):
        self.player()
        self.npc()
        self.winer(self.npc_input, self.player_input)

test = "hello"
print(type(test))

play = rps()
play.game()


