# Ludo game

import tkinter as tk
from func import roll_dice


play_area = [3, 3, 3, 3, 11, 10, 11, 3, 3, 3, 3]

window = tk.Tk()

window.title('Mench Game')
window.geometry('1000x1000')

content = tk.Label(window, text='Wellcome to my Ludo game')
content.pack(pady=20, padx=100)

frame_game = tk.Frame(window, bg='black')
frame_game.pack(expand=True, side=tk.LEFT)

# Show the dice number
show_dice = tk.StringVar()
dice = tk.Label(window, textvariable=show_dice)
dice.pack(pady=15, padx=100)

# Show player turn
player_turn = tk.StringVar()
player_label = tk.Label(window, textvariable=player_turn)
player_label.pack(pady=15, padx=100)

# Player initializing  
players = ['blue', 'yelllow']
current_player = 0
home_pose = {'blue': (0, 7), 'yellow': (10, 7)}
player_pos = {'blue': (0, 8), 'yellow': (10, 6)}
white_pos: list[(int, int)] = []
blue_home: list[(int, int)] = []
red_home: list[(int, int)] = []
green_home: list[(int, int)] = []
yellow_home: list[(int, int)] = []

# Change Turn of the players 
def update_turn():
    # Here i used the actual current_player so my function doesnt take any input value
    global current_player
    current_player = (current_player + 1) % len(players)
    player_turn.set(f"Turn: {players[current_player]}")

for index, times in enumerate(play_area):
    if index != 0 and index != 10:
        if index <= len(play_area) // 2:
            match times:
                case 3:
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=6)
                    tk.Button(frame_game, text='', background='blue', fg='black', height=2, width=3, state=tk.DISABLED ).grid(row=index, column=7)
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=8)
                    white_pos.extend([(index, 6), (index, 8)])
                    blue_home.append((index, 7))
                case 11:
                    for i in range(times):
                        tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=i + 2)
                        white_pos.append((index, i+2))
                        if i == 5:
                            tk.Button(frame_game, text='', background='blue', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=7)
                            blue_home.append((index, 7))
        if index == 5:
            for i in range(times + 1):
                if i == 0 or i == 10:
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=i + 2)
                    white_pos.append((index, i+2))
                elif 1 <= i <= 4:
                    tk.Button(frame_game, text='', background='red', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=i + 2)
                    red_home.append((index, i+2))
                elif 6 <= i <= 9:
                    tk.Button(frame_game, text='', background='green', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=i + 2)
                    green_home.append((index, i+2))
                # TODO: Fix this shit for the dice and create command for it
                else:
                    tk.Button(frame_game, text='Roll dice', background='purple', height=2, width=3, command=roll_dice).grid(row=index, column=i + 2)
        if index > len(play_area) // 2:
            match times:
                case 3:
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=6)
                    tk.Button(frame_game, text='', background='yellow', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=7)
                    tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=8)
                    white_pos.extend([(index, 6), (index, 8)])
                    yellow_home.append((index, 7))

                case 11:
                    for i in range(times):
                        tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=i + 2)
                        white_pos.append((index, i+2))
                        if i == 5:
                            tk.Button(frame_game, text='', background='yellow', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=7)
                            yellow_home.append((index, 7))
    else:
        if index == 0 or index == 10:
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=6, sticky='nsew')
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=7)
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=8, sticky='nsew')
            white_pos.extend([(index, 6), (index, 7), (index, 8)])

player_button = {
    'blue': tk.Button(frame_game, text='blue', background='blue', fg='white', height=2, width=3, state=tk.DISABLED)
    .grid(row=player_pos['blue'][0], column=player_pos['blue'][1], sticky='nsew'), 
    'yellow': tk.Button(frame_game, text='yellow', background='yellow', fg='white', height=2, width=3, state=tk.DISABLED)
    .grid(row=player_pos['yellow'][0], column=player_pos['yellow'][1], sticky='nsew'), 
}

white_pos.remove((4, 7))
white_pos.remove((6, 7))
green_home = green_home[::-1]
yellow_home = yellow_home[::-1]

print('white_pos')
print(white_pos)


window.mainloop()
