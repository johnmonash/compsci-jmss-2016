class SudokuPuzzle:
    INVALID = 0
    COMPLETE = 1
    VALID_INCOMPLETE = 2

    def __init__(self):
        self.dimension = 3
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
        "returns a flat list of numbers representing a sub-grid (index from 0, so 0,0 is top left, 2,2 is bottom right)"
        nums = []

        for i in range(self.dimension):
            row = self.get_row(y*3 + i)
            for j in range(self.dimension):
                nums.append(row[x*3 + j])

        return nums

    def check_nums(self, l):
        "checks if a list of numbers is a valid sudoku set. Returns INVALID, COMPLETE, or VALID_INCOMPLETE"
        result = self.COMPLETE  # DANGEROUS!!!
        for i in l:
            if i is None:
                result = self.VALID_INCOMPLETE
                continue
            if l.count(i) > 1:
                result = self.INVALID
        return result

    def check_row(self, y):
        self.check_nums(self.get_row(y))

    def check_col(self, x):
        self.check_nums(self.get_col(x))

    def check_sub_grid(self, x, y):
        self.check_nums(self.get_sub_grid(x,y))


    def check(self):
        "Check if current structure is valid"
        for
        # check each row
        # check each col
        # check each subgrid
