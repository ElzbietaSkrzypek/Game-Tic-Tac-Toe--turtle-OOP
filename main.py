import turtle
from print_x_o import PrintO, PrintX
from game_over import GameOver

ALIGMENT = "center"
FONT = ('Arial', 50, 'bold')

screen = turtle.Screen()
screen.setup(width=500, height=420)
screen.title("Tic Tac Toe Game")
image = "tic_tac_toe.gif"
screen.addshape(image)
turtle.shape(image)

clicked_nr = 0
x_cor = 0
y_cor = 0
a = ""
b = ""

# ------POSITIONS ---------

table = [[None, None, None],
         [None, None, None],
         [None, None, None]]


def check():

    # slants
    if table[0][0] == table[1][1] == table[2][2]:
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0]:
        return table[0][2]
    # rows
    for row in [0, 1, 2]:
        if table[row][0] == table[row][1] == table[row][2]:
            return table[row][0]
    # columns
    for col in [0, 1, 2]:
        if table[0][col] == table[1][col] == table[2][col]:
            return table[0][col]


def get_mouse_clicked_cor(x, y):
    global clicked_nr, x_cor, y_cor, a, b
    if y > 64:
        y_cor = 100
        a = 0
    if (-82) < y < 64:
        y_cor = (-40)
        a = 1
    if y < (-82):
        y_cor = (-180)
        a = 2
    if x < (-64):
        x_cor = (-140)
        b = 0
    elif x > 81:
        x_cor = 150
        b = 2
    else:
        x_cor = 10
        b = 1
    position = (x_cor, y_cor)
    print_x_o(position, a, b)

    # ---------- printing x / o ------------

def print_x_o(position, a, b):
    global clicked_nr
    if table[a][b] is None:
        clicked_nr += 1
        if clicked_nr in [1, 3, 5, 7, 9]:
            print_x_o = PrintX(position)
            table[a][b] = "X"
        elif clicked_nr in [2, 4, 6, 8, 9]:
            print_x_o = PrintO(position)
            table[a][b] = "O"

    # -----------check the winner ----------

    if check() is not None:
        game_over = GameOver()
        game_over.color("#251B37")
        game_over.write(f"{check()} won!", align=ALIGMENT, font=FONT)
        screen.exitonclick()

    elif check() is None and clicked_nr == 9:
        game_over = GameOver()
        game_over.color("#251B37")
        game_over.write(f"Game Over.", align=ALIGMENT, font=FONT)
        screen.exitonclick()


turtle.onscreenclick(get_mouse_clicked_cor)

turtle.mainloop()
