
class Element:

    def __init__(self, letter=''):
        self.letter = letter
        self.display = '_'

    def __repr__(self):
        return f"Letter: {self.letter} - Display: {self.display}"
    
