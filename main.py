import random
import time


class Board:
    debug = True

    def __init__(self):
        self.square = [
            [Square3x3(), Square3x3(), Square3x3()],
            [Square3x3(), Square3x3(), Square3x3()],
            [Square3x3(), Square3x3(), Square3x3()],
        ]

    def clear(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.square[i][j].clear()

    def get_row_values(self, i, k):
        values = []
        for j in range(0, 3):
            for m in range(0, 3):
                val = self.square[i][j].field[k][m]
                if val:
                    values.append(val)
        return values

    def get_col_values(self, j, m):
        values = []
        for i in range(0, 3):
            for k in range(0, 3):
                val = self.square[i][j].field[k][m]
                if val:
                    values.append(val)
        return values

    def check_if_rows_ok(self):
        for i in range(0, 3):
            for j in range(0, 3):
                part1 = self.square[i][0].row[j]
                part2 = self.square[i][1].row[j]
                part3 = self.square[i][2].row[j]
                row = part1 + part2 + part3
                if len(row) != len(set(row)):
                    if Board.debug:
                        print(f'Wrong row: {row}')
                    if len(part1 + part2) != len(set(part1 + part2)):
                        return False
        return True

    def check_if_columns_ok(self):
        for i in range(0, 3):
            for j in range(0, 3):
                part1 = self.square[0][i].col[j]
                part2 = self.square[1][i].col[j]
                part3 = self.square[2][i].col[j]
                column = part1 + part2 + part3
                if len(column) != len(set(column)):
                    if Board.debug:
                        print(f'Wrong column: {column}')
                    return False
        return True

    def check_if_squares_ok(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if not self.square[i][j].check_if_ok():
                    if Board.debug:
                        print(f'Wrong square:\n{self.square[i][j]}')
                    return False
        return True

    def randomize_field_values(self):
        repeat = True
        n = 0
        t1 = time.time_ns()
        while repeat:
            n += 1
            errors = 0
            for i in range(0, 3):  # squares ROW
                for j in range(0, 3):  # squares COL
                    for k in range(0, 3):  # inner square ROW
                        for m in range(0, 3):  # inner square COL
                            if errors == 0:
                                square_values = self.square[i][j].get_all_fields_values()
                                row_values = self.get_row_values(i, k)
                                col_values = self.get_col_values(j, m)
                                choices = list(range(1, 10))
                                for v in set(square_values + row_values + col_values):
                                    if v in choices:
                                        choices.remove(v)

                                if len(choices) > 0:
                                    self.square[i][j].set_field_value(k, m, random.choice(choices))
                                else:
                                    errors += 1
                                    self.clear()
            if errors == 0:
                if self.check_if_squares_ok() and self.check_if_rows_ok() and self.check_if_columns_ok():
                    repeat = False

        if self.debug:
            print(f'iterations: {n}, {(time.time_ns() - t1) / 1000 / 1000} ms')

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

        self.row = None
        self.col = None

        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
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

    def clear(self):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.update_rows_cols()

    def get_all_fields_values(self):
        values = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.field[i][j]:
                    values.append(self.field[i][j])
        return values

    def set_field_value(self, i, j, value):
        self.field[i][j] = value
        self.update_rows_cols()

    def check_if_ok(self):
        values = []
        for i in range(0, 3):
            for j in range(0, 3):
                values.append(self.field[i][j])
        if len(values) != len(set(values)):
            return False
        return True

    def __repr__(self):
        return f"{self.field[0]}\n{self.field[1]}\n{self.field[2]}"


brd = Board()

brd.randomize_field_values()

print(brd)
