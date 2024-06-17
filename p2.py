# Ludo game

import tkinter as tk


play_area = [3, 3, 3, 3, 11, 10, 11, 3, 3, 3, 3]

window = tk.Tk()

window.title('Mench Game')
window.geometry('1000x1000')

frame_game = tk.Frame(window, bg='black')

for index, times in enumerate(play_area):
    if index != 0 and index != 10:
        if index <= len(play_area) // 2:
            match times:
                case 3:
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=6)
                    tk.Button(frame_game, text='', background='blue', fg='black', height=2, width=3).grid(row=index, column=7)
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=8)
                case 11:
                    for i in range(times):
                        tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=i + 2)
                        if i == 5:
                            tk.Button(frame_game, text='', background='blue', fg='black', height=2, width=3).grid(row=index, column=7)
        if index == 5:
            for i in range(times + 1):
                if i == 0 or i == 10:
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=i + 2)
                elif 1 <= i <= 4:
                    tk.Button(frame_game, text='', background='red', fg='black', height=2, width=3).grid(row=index, column=i + 2)
                elif 6 <= i <= 9:
                    tk.Button(frame_game, text='', background='green', fg='black', height=2, width=3).grid(row=index, column=i + 2)
                # TODO: Fix this shit for the dice and create command for it
                else:
                    tk.Button(frame_game, text='Roll dice', background='purple', height=2, width=3).grid(row=index, column=i + 2)
        if index > len(play_area) // 2:
            match times:
                case 3:
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=6)
                    tk.Button(frame_game, text='', background='yellow', fg='black', height=2, width=3).grid(row=index, column=7)
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=8)
                case 11:
                    for i in range(times):
                        tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=i + 2)
                        if i == 5:
                            tk.Button(frame_game, text='', background='yellow', fg='black', height=2, width=3).grid(row=index, column=7)
    else:
        if index == 0 or index == 10:
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=6)
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=7)
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3).grid(row=index, column=8)


frame_game.pack(expand=True, side=tk.LEFT)


window.mainloop()

