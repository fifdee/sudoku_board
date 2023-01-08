import random


class Board:
    debug = True

    def __init__(self):
        self.square = [
            [Square3x3(), Square3x3(), Square3x3()],
            [Square3x3(), Square3x3(), Square3x3()],
            [Square3x3(), Square3x3(), Square3x3()],
        ]

    def check_if_rows_ok(self):
        for i in range(0, 3):
            for j in range(0, 3):
                part1 = self.square[i][0].row[j]
                part2 = self.square[i][1].row[j]
                part3 = self.square[i][2].row[j]
                row = part1 + part2 + part3
                if len(row) != len(set(row)):
                    if Board.debug:
                        print(f'Wrong row {3 * i + j}: {row}')
                    if len(part1 + part2) != len(set(part1 + part2)):
                        return False, self.square[i][1]
                    else:
                        return False, self.square[i][2]
        return True

    def check_if_columns_ok(self):
        for i in range(0, 3):
            for j in range(0, 3):
                column = self.square[0][i].col[j] + self.square[1][i].col[j] + self.square[2][i].col[j]
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
                    return False, self.square[i][j]
        return True, None

    def randomize_field_values(self):
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for m in range(0, 3):
                        self.square[i][j].set_field_value(k, m, random.randint(1, 9))

        while True:
            if self.check_if_squares_ok()[0] and self.check_if_rows_ok()[0] and self.check_if_columns_ok():
                break
            else:
                for i in range(0, 3):
                    for j in range(0, 3):
                        choices = [x for x in range(1, 10)]
                        for k in range(0, 3):
                            for m in range(0, 3):
                                value = random.choice(choices)
                                choices.remove(value)
                                self.square[i][j].set_field_value(k, m, value)

            # is_ok, square = self.check_if_squares_ok()
            # if is_ok:
            #     is_ok, square = self.check_if_rows_ok()
            #
            # if not is_ok:
            #     choices = [i for i in range(1, 10)]
            #     for k in range(0, 3):
            #         for m in range(0, 3):
            #             value = random.choice(choices)
            #             choices.remove(value)
            #             square.set_field_value(k, m, value)
            # else:
            #     break

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
# brd.square[1][1].set_field_value(1, 1, 52)  # column check fail
# brd.square[1][1].field[1][1] = 54  # row check fail
# print(brd.check_if_rows_ok())
brd.randomize_field_values()

print(brd)
