import random
from card import Card


class Board:
    def __init__(self, size, randomize=True):
        self.size = size
        self.build_cards(size, randomize)

    def build_cards(self,size,randomize=True):
        self.cards = [Card(i) for i in range(size//2) for _ in range(2)]
        if randomize:
            random.shuffle(self.cards)

    def isLeagal(self,index):
        return index < 0 or index >= self.size or self.cards[index].face_up
    
    def get_user_input(self):
        index1 = int(input("Enter the index of the first card: "))
        index2 = int(input("Enter the index of the second card: "))

        if index1 == index2 or self.isLegal(index1) or self.isLegal(index2):
            print("Invalid input. Please try again.")
            return self.get_user_input()
        return (index1,index2)
    
    def check_match(self,indexes):
        if self.cards[indexes[0]].value == self.cards[indexes[1]].value:
            print("Match found!")
            return 1
        else:
            print("No match. Try again.")
            self.cards[indexes[0]].flip()
            self.cards[indexes[1]].flip()
        return 0
    
    def play(self):
        turns = 0
        pairs_found = 0

        while pairs_found < self.size // 2:
            self.display_board()
            
            cards_index = self.get_user_input()

            self.cards[cards_index[0]].flip()
            self.cards[cards_index[1]].flip()

            self.display_board()
            pairs_found+= self.check_match(cards_index)
            turns += 1

        print(f"Congratulations! You completed the game in {turns} turns.")

    def display_board(self):
        for i, card in enumerate(self.cards):
            if card.face_up:
                print(f"{card.value:2}", end=" ")
            else:
                print(" *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()

# Example usage
board_size = 4
game = Board(board_size)  
game.play()