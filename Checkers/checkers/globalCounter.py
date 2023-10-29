class GlobalCounter:
    
    chousen_board = []

    def set_chousen_board(self,chousen_board):
        self.chousen_board = chousen_board

    def __init__(self):
        self.node_count = 0

    def increment(self):
        self.node_count += 1

    def get_count(self):
        return self.node_count

    def __str__(self):
        return f'Chousen Board ={self.chousen_board} and number interation = {self.node_count}'