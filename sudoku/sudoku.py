class sudoku_puzzle:
    def __init__(self):
        self.data = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]
        ]


    def get_cell(self, x, y):
        return self.data[y][x]

    def get_col(self, x):
        col = []
        for row in self.data:
            col.append(row[x])

    def get_row(self, y):
        return self.data[y]

    def get_sub_grid(self, x, y):


    def check_sub_grid(self):
        pass

    def check_nums(self, l):


    def check_row(self, y):
        self.check_nums(self.get_row(y))

    def check_col(self, x):
        self.check_nums(self.get_col(x))

    def check(self):
        "Check if current structure is valid"
        # check each row
        # check each col
        # check each subgrid
