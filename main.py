import tkinter as tk
from ctypes import windll
from copy import deepcopy

from classes import Board

windll.shcore.SetProcessDpiAwareness(1)

entries = []
frames = []
boards = []


def handle_keypress(event):
    label_result.config(text='')
    print(event.char)
    w = [o for o in entries if o['obj'] == event.widget][0]
    print(f"square[{w['i']}][{w['j']}].field[{w['k']}][{w['m']}]")

    allowed_values = list(range(1, 10))

    new_value = w['obj'].get() + event.char
    print(new_value)

    if new_value in allowed_values:
        ...
    else:
        ...


def check_solution():
    if len(entries) > 0:
        correct = True
        for entry in entries:
            i = entry['i']
            j = entry['j']
            k = entry['k']
            m = entry['m']
            value = entry['obj'].get()
            correct_value = str(boards[1].square[i][j].field[k][m])
            if value != correct_value:
                correct = False
                break
    else:
        correct = False

    if correct:
        print("OK!")
        label_result.config(text="The solution is OK!")
    else:
        print("WRONG!")
        label_result.config(text="Wrong solution")


def solve_board():
    label_result.config(text='')
    for entry in entries:
        i = entry['i']
        j = entry['j']
        k = entry['k']
        m = entry['m']
        value = boards[1].square[i][j].field[k][m]
        entry['obj'].delete(0, tk.END)
        entry['obj'].insert(0, value)


def destroy_board():
    label_result.config(text='')
    entries.clear()
    boards.clear()
    for frame in frames:
        frame.destroy()


def redraw_board():
    destroy_board()

    brd = Board()
    brd.randomize_field_values()
    brd_solved = deepcopy(brd)
    brd.hide_random_fields()

    boards.append(brd)
    boards.append(brd_solved)

    print(brd)
    print(brd_solved)

    for i in range(0, 3):
        # big square row
        for j in range(0, 3):
            #  big square col
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i + 2, column=j, padx=5, pady=5)
            frames.append(frame)

            for k in range(0, 3):
                #  field row
                for m in range(0, 3):
                    #  field col
                    frame_inner = tk.Frame(
                        master=frame,
                        borderwidth=1
                    )
                    frame_inner.grid(row=k, column=m, padx=2, pady=2)
                    frames.append(frame_inner)

                    val = brd.square[i][j].field[k][m]
                    if val != '':
                        label = tk.Label(master=frame_inner, width=5, text=val)
                        label.pack()
                    else:
                        entry = tk.Entry(master=frame_inner, width=5, justify='center')
                        entry.insert(0, val)
                        entry.pack()

                        entries.append({
                            'obj': entry,
                            'i': i,
                            'j': j,
                            'k': k,
                            'm': m
                        })

    for entry in entries:
        entry['obj'].bind("<Key>", handle_keypress)


window = tk.Tk()

reload_board_btn = tk.Button(master=window, justify='center', text='New board', command=redraw_board)
reload_board_btn.grid(row=0, column=0)

solve_board_btn = tk.Button(master=window, justify='center', text='Solve board', command=solve_board)
solve_board_btn.grid(row=0, column=1)

check_board_btn = tk.Button(master=window, justify='center', text='Check solution', command=check_solution)
check_board_btn.grid(row=0, column=2)

label_result = tk.Label(master=window, justify='center', text='aaa')
label_result.grid(row=1, column=1)

redraw_board()

window.mainloop()
