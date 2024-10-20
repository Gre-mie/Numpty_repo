# Draw cakes to the terminal, simple programe without inputs



# constants
# f"\033[38;2;{};{};{}m"
# f"\033[48;2;{};{};{}m"
CHAR_COLOURS = {
    "default": f"\033[39m", 
    "white": f"\033[38;2;{255};{255};{255}m",
    "dark_red": f"\033[38;2;{172};{50};{50}m", 
    "light_red": f"\033[38;2;{217};{87};{99}m"
}
BG_COLOURS = {
    "default": f"\033[49m", 
    "cream_brown": f"\033[48;2;{238};{195};{154}m",
    "cream": f"\033[48;2;{251};{245};{225}m",
    "dark_red": f"\033[48;2;{172};{50};{50}m"
}


# layer functions

def sponge_layer(width, height, col, char):
    sponge = []
    sponge.append(col)

    for j in range(height):
        row = []
        for i in range(width):
            row.append(char)
            if i == width - 1 and j != height - 1:
                row.append('\n')

        if j != height - 1:
            sponge.append('\n')
        
        sponge.append(''.join(row))

    sponge.append(BG_COLOURS["default"])
    print(''.join(sponge))


def main():
    print("\nworking\n")

    sponge_layer(20, 2, BG_COLOURS["cream_brown"], '.') # test

    sponge_layer(10, 1, CHAR_COLOURS["white"], '@') # test
    sponge_layer(10, 1, CHAR_COLOURS["dark_red"], '@') # test
    sponge_layer(10, 1, CHAR_COLOURS["light_red"], '@') # test

    sponge_layer(10, 1, BG_COLOURS["cream_brown"], ' ') # test
    sponge_layer(10, 1, BG_COLOURS["cream"], ' ') # test
    sponge_layer(10, 1, BG_COLOURS["dark_red"], ' ') # test





    



main()


