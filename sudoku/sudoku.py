class SudokuPuzzle:
    INVALID = 0
    COMPLETE = 1
    VALID_INCOMPLETE = 2

    def __init__(self):
        self.dimension = 3  # TODO extend to allow rectangular grids
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

    def get_cols(self):
        cols = []
        for i in range(self.dimension **2):
            cols.append(self.get_col(i))
        return cols

    def get_row(self, y):
        return self.data[y]

    def get_rows(self):
        return self.data

    def get_sub_grid(self, x, y):
        "returns a flat list of numbers representing a sub-grid (index from 0, so 0,0 is top left, 2,2 is bottom right)"
        nums = []

        for i in range(self.dimension):
            row = self.get_row(y*3 + i)
            for j in range(self.dimension):
                nums.append(row[x*3 + j])

        return nums

    def get_sub_grids(self):
        grids = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                grids.append(i,j)
        return grids

    def check_list(self, l):
        "checks if a list of numbers is a valid sudoku set. Returns INVALID, COMPLETE, or VALID_INCOMPLETE"
        valid = True
        complete = True
        for i in l:
            if i is None:
                complete = False
                continue
            if l.count(i) > 1:
                valid = False
        return (valid, complete)


    def check_lists(self, ls):
        valid = True
        complete = True
        for l in ls():
            (valid, complete) = (valid, complete) and self.check_list(l)
        return (valid, complete)

    def check(self):
        "Check if current structure is valid"
        valid = True
        complete = True
        (valid, complete) = (valid, complete) and self.check_lists(self.get_rows())
        (valid, complete) = (valid, complete) and self.check_lists(self.get_cols())
        (valid, complete) = (valid, complete) and self.check_lists(self.get_sub_grids())
        return (valid, complete)
