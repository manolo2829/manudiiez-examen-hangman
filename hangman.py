from element import Element
from invalidAssignmentException import InvalidAssignmentException

class Hangman:

    def __init__(self):
        self.lifes = 5
        self.word = []

    def show(self):
        auxiliar = f"Lifes: {self.lifes} - Word: "

        for letter in self.word:
            auxiliar += f"{letter.display} "

        return auxiliar

    def set_word(self, word):
        for letter in word.lower():
            self.word.append(Element(letter))
            
    def assign(self, letter):
        letter = letter.lower()
        auxiliar = False
        for each in self.word:
            if(letter == each.letter):
                auxiliar = True
                each.display = each.letter
        if not auxiliar:
            self.lifes -= 1
            raise InvalidAssignmentException('Letra no valida')

    def winner(self):
        auxiliar = True
        for each in self.word:
            if not each.letter == each.display:
                auxiliar = False

        return auxiliar
    
    def play(self):
        while self.lifes > 0 and not self.winner():
            print(self.show())

            letter = input()

            try:
                self.assign(letter)
            except InvalidAssignmentException:
                print(f'Letra invalida. Le quedan {self.lifes} vidas')

            print(self.show())

        if self.lifes > 0:
            return 'Ganaste' 
        else:
            return 'Perdiste' 