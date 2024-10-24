# Draw cakes to the terminal, simple programe without inputs

# prototypes
# Fishcake(self, width) 

# -- prototypes incomplete --                               -- description --
# Victoria_Sponge(self, width)                              sponge, jam, cream, sponge
# Chocolate_Cake(self, width, int_layers, bool_icing)       icing (if true), sponge, (filling, sponge, ... n layers -loop)
# Vanilla_Cake(self, width, int_layers, string_topping)     topping ("cherries", "candals", "None" -default) evenly distributed across width, icing (with a drip down onto next layer, half unit), sponge, (jam, cream, sponge, ... n layers -loop)

# boot.dev joke cakes
# Fish_barrel_cake(self, width, int_layer, fish_colour)     fish tail (in center, may need special chars), sponge, (filling (same as Fishcake), sponge, ... n layers -loop) 

# Note:
#   candal wick can be '|'
#   candal wax can be half_unit

# ----- constants -----
# f"\033[38;2;{};{};{}m"
# f"\033[48;2;{};{};{}m"
CHAR_COLOURS = {
    "default": f"\033[39m", 
#    "white": f"\033[38;2;{255};{255};{255}m",
    "orange": f"\033[38;2;{220};{129};{39}m"
#    "dark_red": f"\033[38;2;{172};{50};{50}m", 
#    "light_red": f"\033[38;2;{217};{87};{99}m"
}
BG_COLOURS = {
    "default": f"\033[49m", 
    "cream_brown": f"\033[48;2;{238};{195};{154}m",
    "cream": f"\033[48;2;{251};{245};{225}m",
    "orange": f"\033[48;2;{220};{129};{39}m",
    "dark_red": f"\033[48;2;{172};{50};{50}m"
}

ERROR_COLOURS = {
    "red": f"\033[31m",
    "grey": f"\033[22;30m"
}

ERROR_MESSAGES = {
    "less than 3": [ERROR_COLOURS["red"], "The cake is so small, it cant be seen by the naked eye!\n", ERROR_COLOURS["grey"], "Cakes must be at least 3 units in width", CHAR_COLOURS["default"]]
}

# ----- class definitions -----

# One unit    = 2 chars
# Half a unit = 1 char
class Fishcake:
    def __init__(self, unit_width, cake_name, layers): # layers added for compatibility with make_cake() function, but is not used in this class
        self.name = cake_name
        self.all_cake_rows = []

        self.__width = unit_width - 1

        if unit_width < 3:  # unit_width is used due to it being the full width of the cake
            print(self.name)
            raise ValueError("".join(ERROR_MESSAGES["less than 3"]))

    def construct_cake(self):
        self.all_cake_rows = [CHAR_COLOURS["orange"], '(']
        end_cake = [')', CHAR_COLOURS["default"]]

        for _ in range(self.__width):
            self.all_cake_rows.append(BG_COLOURS["orange"])
            self.all_cake_rows.append("  ")
            self.all_cake_rows.append(BG_COLOURS["default"])
        self.all_cake_rows.append("".join(end_cake))

    def convert_to_string(self):
        self.construct_cake()
        return "".join(self.all_cake_rows)

    def print_cake(self, cake_string):
        print(self.name)
        print(cake_string)
    
#--------------------------------------------------------------------------------------------------------------------------------

#   ---- parent classes ----

#   ---- parent/child classes ----

class Cake():
    def __init__(self, unit_width, cake_name, layers):
        self.name = cake_name
        self.all_cake_rows = []
        self.width = unit_width
        self.num_of_layers = layers

        if unit_width < 3:
            print(self.name)
            raise ValueError("".join(ERROR_MESSAGES["less than 3"]))

    def sponge(self, height=2, col=BG_COLOURS["cream_brown"]):    # returns 'sponge' array. Uses self.width to create row arrays that are added to sponge array. Hight determins the number of rows in the sponge array.
        sponge = []
        for j in range(height):
            row = []
            row.append(col)
            for i in range(self.width):
                row.append('  ')
            row.append(BG_COLOURS["default"])
            sponge.append(row)
        return  sponge
    
    def filling(self, col):                                       # returns one layer of 'filling' array. Hight is 1. Width is self.width - 2 (units). The filling row should begin with a space (half unit).
        width = self.width - 2
        row = [' ', col]
        row.append(' ')
        for i in range(width):
            row.append('  ')
        row.append(' ')
        row.append(BG_COLOURS["default"])
        return  row

    def layers(self):                                             # returns 'layers' array of rows. Calls __filling and __sponge in a loop set to num_of_layers
        layers = []
        for i in range(self.num_of_layers):
            layers.append(self.filling(BG_COLOURS["dark_red"]))
            layers.append(self.filling(BG_COLOURS["cream"]))
            for r in self.sponge(2):
                layers.append(r)
        return  layers

    def construct_cake(self):                                       # calls __sponge and __layers to build the rows, sends them to all_cake_rows
        self.all_cake_rows.append(self.sponge(2))        
        self.all_cake_rows.append(self.layers())

    def convert_to_string(self):                                    # returns a single string. uses the self.__all_cake_rows array, converting each row into a string and adds the row to a temp array. Then joining the array using '\n' as the joiner
        str_row_array = []
        for cake_area in self.all_cake_rows:
            for row in cake_area:
                str_row_array.append("".join(row))
        return "\n".join(str_row_array)

    def print_cake(self, cake_string):                              # takes the return from convert_to_string as the argument. Prints the name of the cake (self.name) and the cake_string
        print(self.name)
        print(cake_string)

# ----- global functions -----

def make_cake(cake_class_name, cake_unit_width, cake_name="Unamed Cake", layers=None):
    try:
        Cake_class = globals()[cake_class_name] # turns a normal string into a class name
        cake = Cake_class(cake_unit_width, cake_name, layers)
        cake.construct_cake()
        cake.print_cake(cake.convert_to_string())
    except ValueError as error_message:
        print(error_message)

def main():
    print()

    # completed cakes
    make_cake("Fishcake", 7, "Fishcake")
    print() # new line

    # --------------- testing -----------------------
    make_cake("Cake", 15, "Basic cake", 1)
    print()
    make_cake("Cake", 20, "Basic cake", 2)




main()


