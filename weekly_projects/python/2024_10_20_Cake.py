# Draw cakes to the terminal, simple programe without inputs

# prototypes                                                description
# Victoria_Sponge(self, width)                              sponge, jam, cream, sponge
# Chocolate_Cake(self, width, int_layers, bool_icing)       icing (if true), sponge, (filling, sponge, ... n layers -loop)
# Vanilla_Cake(self, width, int_layers, string_topping)     topping ("cherries", "candals", "None" -default) evenly distributed across width, icing (with a drip down onto next layer, half unit), sponge, (jam, cream, sponge, ... n layers -loop)

# Note:
#   candal wick can be '|'
#   candal wax can be half_unit

# constants
# f"\033[38;2;{};{};{}m"
# f"\033[48;2;{};{};{}m"
CHAR_COLOURS = {
    "default": f"\033[39m", 
#    "white": f"\033[38;2;{255};{255};{255}m",
#    "dark_red": f"\033[38;2;{172};{50};{50}m", 
#    "light_red": f"\033[38;2;{217};{87};{99}m"
}
BG_COLOURS = {
    "default": f"\033[49m", 
#    "cream_brown": f"\033[48;2;{238};{195};{154}m",
#    "cream": f"\033[48;2;{251};{245};{225}m",
#    "dark_red": f"\033[48;2;{172};{50};{50}m"
}

# layer function
#def sponge_layer(width, height, col, char):
#    sponge = []
#    unit = char + char
#    half_unit = char # used 

#    for j in range(height):
#        row = []
#        for i in range(width):
#            row.append(col)
#            row.append(unit)
#            row.append(BG_COLOURS["default"])

#            if i == width - 1 and j != height - 1:
#                row.append('\n')

#        sponge.append(''.join(row))
    
#    print(''.join(sponge))


def main():
    print() # test
    # sponge_layer(unit_width, unit_height, colour, )
    # 1 unit = 2 spaces
    # half a unit = 1 space
#    sponge_layer(1, 1, BG_COLOURS["cream_brown"], '..') # test
#    sponge_layer(1, 1, BG_COLOURS["cream"], '.') # test
#    sponge_layer(1, 1, BG_COLOURS["dark_red"], '..') # test
#    print()

#    iceing = 1
#    sponge = 2
#    jam = 1
#    cream = 1
#    sponge_layer(21, iceing, CHAR_COLOURS["white"], '_')
#    sponge_layer(20, sponge, BG_COLOURS["cream_brown"], ' ') # test
#    sponge_layer(19, jam, BG_COLOURS["dark_red"], ' ') # test
#    sponge_layer(19, cream, BG_COLOURS["cream"], ' ') # test
#    sponge_layer(20, sponge, BG_COLOURS["cream_brown"], ' ') # test




    



main()


