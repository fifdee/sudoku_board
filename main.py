class Board:
    def __init__(self):
        self.square = [
            [Square3x3(), Square3x3(), Square3x3()],
            [Square3x3(), Square3x3(), Square3x3()],
            [Square3x3(), Square3x3(), Square3x3()],
        ]

    def check_if_rows_ok(self):
        for i in range(0, 3):
            for j in range(0, 3):
                row = self.square[i][0].row[j] + self.square[i][1].row[j] + self.square[i][2].row[j]
                print(row)
                if len(row) != len(set(row)):
                    return False
        return True

    def check_if_columns_ok(self):
        for i in range(0, 3):
            for j in range(0, 3):
                column = self.square[0][i].col[j] + self.square[1][i].col[j] + self.square[2][i].col[j]
                print(column)
                if len(column) != len(set(column)):
                    return False
        return True

    def __repr__(self):
        return_string = ''
        for i in range(0, 3):
            for j in range(0, 3):
                return_string += f'{self.square[i][0].row[j]} {self.square[i][1].row[j]} {self.square[i][2].row[j]}\n'
            return_string += '\n'

        return return_string


class Square3x3:
    how_many = 0

    def __init__(self):
        Square3x3.how_many += 1
        # self.field = [
        #     [None, None, None],
        #     [None, None, None],
        #     [None, None, None],
        # ]
        self.row = None
        self.col = None

        self.field = [
            [Square3x3.how_many * 10 + 1, Square3x3.how_many * 10 + 2, Square3x3.how_many * 10 + 3],
            [Square3x3.how_many * 10 + 4, Square3x3.how_many * 10 + 5, Square3x3.how_many * 10 + 6],
            [Square3x3.how_many * 10 + 7, Square3x3.how_many * 10 + 8, Square3x3.how_many * 10 + 9],
        ]

        self.update_rows_cols()

    def update_rows_cols(self):
        self.row = [
            self.field[0],
            self.field[1],
            self.field[2],
        ]

        self.col = [
            [self.field[0][0], self.field[1][0], self.field[2][0]],
            [self.field[0][1], self.field[1][1], self.field[2][1]],
            [self.field[0][2], self.field[1][2], self.field[2][2]]
        ]

    def set_field_value(self, i, j, value):
        self.field[i][j] = value
        self.update_rows_cols()

    def __repr__(self):
        return f"{self.field[0]}\n{self.field[1]}\n{self.field[2]}"


brd = Board()
brd.square[1][1].set_field_value(1, 1, 52)  # column check fail
# brd.square[1][1].field[1][1] = 54  # row check fail
# print(brd.check_if_rows_ok())

print(brd)
print()
print(brd.check_if_columns_ok())
#
# print(brd.square[1][1])
# print()
# print(brd.square[1][1].col[0])
