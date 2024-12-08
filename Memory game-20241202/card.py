class Card:
    def __init__(self, value):
        self.value = value
        self.face_up = False

    def flip(self):
        self.face_up = not self.face_up