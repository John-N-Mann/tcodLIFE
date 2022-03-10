import tcod.tileset

def str_TCOD(i: int):
    this = chr(tcod.tileset.CHARMAP_TCOD[i])
    return this

def draw_border(x, y, width, height, console):
    for i in range(width - 2): # PRINTING TOP ROW
        console.print(x=(x + 1 + i), y=(y + 0), string=str_TCOD(47))
    for i in range(width - 2): # PRINTING BOTTOM ROW
        console.print(x=(x + 1 + i), y=(y+height-1), string=str_TCOD(47))
    for i in range(height - 2): # PRINTING LEFT COLUMN
        console.print(x=(x + 0), y=(y + 1 + i), string=str_TCOD(46))
    for i in range(height - 2): # PRINTING RIGHT COLUMN
        console.print(x=(x + width - 1), y=(y + 1 + i), string=str_TCOD(46))
    console.print(x=(x + 0),y=(y + 0), string=str_TCOD(54)) # TOP LEFT CORNER
    console.print(x=(x + width-1) ,y=(y + 0), string=str_TCOD(55)) # TOP RIGHT CORNER
    console.print(x=(x + 0), y=(y + height-1), string=str_TCOD(53)) # BOTTOM LEFT CORNER
    console.print(x=(x + width-1), y=(y + height-1), string=str_TCOD(56)) # BOTTOM RIGHT CORNER