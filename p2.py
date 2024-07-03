# Ludo game

import tkinter as tk
from func import roll_dice, sort_data_ludo
import time


play_area = [3, 3, 3, 3, 11, 10, 11, 3, 3, 3, 3]

window = tk.Tk()

window.title('Mench Game')
window.geometry('1000x1000')

content = tk.Label(window, text='Wellcome to my Ludo game')
content.pack(expand=True, pady=5, padx=100)

# Show the dice number
show_dice = tk.StringVar()
dice = tk.Label(window, textvariable=show_dice)
dice.pack(expand=True, pady=5, padx=100)

# Show player turn
player_turn = tk.StringVar()
player_label = tk.Label(window, textvariable=player_turn)
player_label.pack(expand=True, pady=5, padx=100)

message_box = tk.StringVar()
message_label = tk.Label(window, textvariable=message_box)
message_label.pack(expand=True, pady=5, padx=150)


frame_game = tk.Frame(window, bg='black')
frame_game.pack(expand=True)


# Player initializing  
players = ['blue', 'yellow']
current_player = 0
player_pos = {'blue': (0, 8), 'yellow': (10, 6)}
white_pos: list[(int, int)] = []
blue_home: list[(int, int)] = []
red_home: list[(int, int)] = []
green_home: list[(int, int)] = []
yellow_home: list[(int, int)] = []
player_buttons = {
    'blue': [], 
    'yellow': [], 
}

# Roll the dice and Change the player
# TODO: Make it move the player button
def dice_move():
    value = roll_dice()
    show_dice.set(f'Dice came: {value} for {players[current_player]}')
    move(players[current_player], value)
    update_turn()


def player_start():
    for player in players:
        # for i in range(2):
        pos = player_pos[player]
        btn = tk.Button(frame_game, text=player, bg=player, fg='black', height=2, width=3)
        btn.grid(row=pos[0], column=pos[1])
        # print(btn)
        player_buttons[player].append(btn)


# TODO: Make The move function
def move(player, step):
    position = player_pos[player]
    play_ground = player_playground[player]
    if step <= 45 - (play_ground.index(position)+1):
        player_pos[player] = play_ground[play_ground.index(position) + step]
        update_position(player)        
    else:
        message_box.set(f"{player} You got Unlucky your dice number is more than homes you neet to achive\nwait for next move!")
        time.sleep(0.5)
        message_box.set('')
    

def update_position(player):
    btn = player_buttons[player][0]
    row, column = player_pos[player]
    
    btn.grid(row=row, column=column)
    if  player_pos[player] == player_playground[player][-1]:
            message_box.set(f"Congrat plyaer {player} You won the game")
            time.sleep(5)
            window.destroy()


# Change Turn of the players 
def update_turn():
    # Here i used the actual current_player so my function doesnt take any input value
    global current_player
    current_player = (current_player + 1) % len(players)
    player_turn.set(f"Next Turn: {players[current_player]}")

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
                        if i == 5:
                            tk.Button(frame_game, text='', background='blue', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=7)
                            blue_home.append((index, 7))
                        else:
                            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=i + 2)
                            white_pos.append((index, i+2))
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
                    tk.Button(frame_game, text='Roll dice', background='purple', height=2, width=3, command=dice_move).grid(row=index, column=i + 2)
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
                        if i == 5:
                            tk.Button(frame_game, text='', background='yellow', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=7)
                            yellow_home.append((index, 7))
                        else:
                            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=i + 2)
                            white_pos.append((index, i+2))
    else:
        if index == 0 or index == 10:
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=6)
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=7)
            tk.Button(frame_game, text='', background='white', fg='black', height=2, width=3, state=tk.DISABLED).grid(row=index, column=8)
            white_pos.extend([(index, 6), (index, 7), (index, 8)])

player_start()

# Here i made the order of these house right
green_home = green_home[::-1]
yellow_home = yellow_home[::-1]

# Sorting the button in order
sort_buttons = sort_data_ludo(white_pos)

# Homes which blue should travel
blue_home = sort_buttons + blue_home

# Homes which yellow shoulf travel
yellow_home = sort_buttons[21:] + sort_buttons[:21] + yellow_home

player_playground = {'blue': blue_home, 'yellow': yellow_home}

player_turn.set(f"Turn: {players[current_player]}")



window.mainloop()
