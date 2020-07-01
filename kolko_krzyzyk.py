class GameBoard():
    fields = {7: ' ', 8: ' ', 9: ' ',
              4: ' ', 5: ' ', 6: ' ',
              1: ' ', 2: ' ', 3: ' '}
    chosen_field = None
    scores_X = 0
    scores_O = 0

    def draw(self):
        a = [self.fields[7], self.fields[8], self.fields[9]]
        line = '-+-+-'
        b = [self.fields[4], self.fields[5], self.fields[6]]
        c = [self.fields[1], self.fields[2], self.fields[3]]

        print('|'.join(a))
        print(line),
        print('|'.join(b))
        print(line)
        print('|'.join(c))

    def put(self, y):
        self.chosen_field = int(input("Enter field number from 1-9: "))
        while self.fields[self.chosen_field] != ' ':
            if self.fields[self.chosen_field] != ' ':
                self.chosen_field = int(input("This field is busy. Choose another one."))
        self.fields[self.chosen_field] = y
        self.draw()
        self.win()

    def win(self):
        condition = (self.fields[1] + self.fields[2] + self.fields[3],
                     self.fields[1] + self.fields[4] + self.fields[7],
                     self.fields[1] + self.fields[5] + self.fields[9],
                     self.fields[2] + self.fields[5] + self.fields[8],
                     self.fields[3] + self.fields[5] + self.fields[7],
                     self.fields[3] + self.fields[6] + self.fields[9],
                     self.fields[4] + self.fields[5] + self.fields[6],
                     self.fields[7] + self.fields[8] + self.fields[9])
        for i in condition:
            if i == "XXX":
                return i
            elif i == "OOO":
                return i

    def turn(self):
        if self.win() == 'XXX':

            self.scores_X += 1
            print("Winner is X!\nX: {}\nO: {}\nO is starting.".format(self.scores_X, self.scores_O))
            self.clean()

        elif self.win() == 'OOO':

            self.scores_O += 1
            print("Winner is O!\nX: {}\nO: {}\nX is starting.".format(self.scores_X, self.scores_O))
            self.clean()

    def play(self):

        while self.scores_X < 3 and self.scores_O < 3:

            self.put('X')

            self.turn()
            if self.scores_O == 3:
                print("Final winner is O. The end")
                break
            elif self.scores_X == 3:
                print("Final winner is X. The end")
                break

            self.put('O')

            self.turn()
            if self.scores_O == 3:
                print("Final winner is O. The end")
                break
            elif self.scores_X == 3:
                print("Final winner is X. The end")
                break

    def clean(self):
        self.fields = {7: ' ', 8: ' ', 9: ' ',
                       4: ' ', 5: ' ', 6: ' ',
                       1: ' ', 2: ' ', 3: ' '}


game = GameBoard()

game.draw()
game.play()
