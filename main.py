import random, time
import tcod, tcod.event
from drawborder import draw_border, str_TCOD

# GLOBAL PARAMATERS
WIDTH, HEIGHT = 120, 68
SPEEDSCALE = 0.1

RANDLIST = [False, True]

gameboard = [[False] * (HEIGHT) for i in range(WIDTH)]

for x in range(1, len(gameboard)-1):
    for y in range(1, len(gameboard[0])-1):
        this = random.randint(0, 1)
        gameboard[x][y] = RANDLIST[this]


def check_neighbors(gameboard, x, y, bool) -> int:
    count = 0
    for _x in range(x-1, x+2):
        for _y in range(y-1, y+2):
            if gameboard[_x][_y] == bool:
                count += 1
    if gameboard[x][y] == True: # this checks if the selected cell is True and removes it from the count
        count -= 1
    return count


# DEFINE MAIN LOOP HERE
def main() -> None:
    global SPEEDSCALE
    global gameboard
    
    tileset = tcod.tileset.load_tilesheet("MANNfont10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    root_console = tcod.Console(WIDTH, HEIGHT, order="F")

    with tcod.context.new(columns=WIDTH, rows=HEIGHT, tileset=tileset, title='tcodLIFE') as context:
        while True:

            # 1 - Any dead cell with exactly 3 neighbors becomes alive by repopulation
            # 2 - Any alive cell with 2-3 neighbors stays alive
            # 3 - Any alive cell with less than two neighbors dies by underpopulation
            # 4 - Any alive cell with more than three neighbors dies by overpopulation

            # reference active gameboard (this skips the border zone)
            for x in range(1, len(gameboard)-1):
                for y in range(1,len(gameboard[0])-1):
                    if gameboard[x][y] == True:
                        this = check_neighbors(gameboard,x,y,True)
                        if this < 2:
                            gameboard[x][y] = False
                        elif this > 3:
                            gameboard[x][y] = False
                    elif gameboard[x][y] == False:
                        this = check_neighbors(gameboard,x,y,True)
                        if this == 3:
                            gameboard[x][y] = True

            # Clear console
            root_console.clear()

            draw_border(x=0, y=0, width=WIDTH, height=HEIGHT, console = root_console)

            # Printing gameboard. +/-1 in for loop reference to accomodate for border at 0,0 and HEIGHT,WIDTH
            for x in range(1, len(gameboard)-1):
                for y in range(1, len(gameboard[0])-1):
                    if gameboard[x][y] == False:
                        root_console.print(x=(x),y=(y),string=str_TCOD(159))
                    if gameboard[x][y] == True:
                        root_console.print(x=(x),y=(y),string=str_TCOD(45))

            # console blit
            context.present(console=root_console)

            time.sleep(SPEEDSCALE)

            for event in tcod.event.get():
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.KeyDown):
                        if str(event.sym) == 'KeySym.ESCAPE':
                            raise SystemExit()
                        if str(event.sym) == 'KeySym.LEFT':
                            SPEEDSCALE = SPEEDSCALE / 0.9
                        if str(event.sym) == 'KeySym.RIGHT':
                            SPEEDSCALE = SPEEDSCALE * 0.9
            


# RUN MAIN LOOP HERE
if __name__ == '__main__':
    main()