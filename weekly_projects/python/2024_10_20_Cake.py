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
#    "cream": f"\033[48;2;{251};{245};{225}m",
    "orange": f"\033[48;2;{220};{129};{39}m"
#    "dark_red": f"\033[48;2;{172};{50};{50}m"
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
    def __init__(self, unit_width, cake_name):
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

#   ---- parent/child classes ----
class Cake():
    def __init__(self, unit_width, cake_name, layers=1):
        self.name = cake_name
        self.all_cake_rows = []

        self.width = unit_width
        self.layers = layers

        if unit_width < 3:
            print(self.name)
            raise ValueError("".join(ERROR_MESSAGES["less than 3"]))


    # Note: when __sponge(), __filling(), __layers() and any other row building function that completes the row is to be placed into __all_cake_rows
    #       If the row is not yet fully complete, for example if an icing drip is still to be applied to the row, it is not to be placed into the __all_cake_rows array untill the drip is added

    # all_cake_rows = [
    #   (call __sponge)   [[sponge row 1], [sponge row 2], [sponge row 3]],                  
    #   (call __layers)   [[layer 1 filling 1], [layer 1 filling 2], [layer 1 sponge row 1], [layer 1sponge row 2], [layer 1sponge row 3]]
    #                 ]

    #       -- example of desiered construct_cake array argument structure --
    #                               all_cake_rows = [
    #   (call __sponge(width=5, height=2))              [
    #                                                       [f"BG_COLOURS["cream_brown"]", '..', '..', '..', '..', '..', f"BG_COLOURS["default"]"],
    #                                                       [f"BG_COLOURS["cream_brown"]", '..', '..', '..', '..', '..', f"BG_COLOURS["default"]"]
    #                                                   ]                  
    #   (call __layers(num_of_layers=1))                [
    #                                                       [f"BG_COLOURS["dark_red"]", ' ', '..', '..', '..', '..', f"BG_COLOURS["default"]"], 
    #                                                       [f"BG_COLOURS["cream"]", ' ', '..', '..', '..', '..', f"BG_COLOURS["default"]"], 
    #                                                       [f"BG_COLOURS["cream_brown"]", '..', '..', '..', '..', '..', f"BG_COLOURS["default"]"],
    #                                                       [f"BG_COLOURS["cream_brown"]", '..', '..', '..', '..', '..', f"BG_COLOURS["default"]"]
    #                                                   ]
    #                                               ]

    def __sponge(self, height=2, col=BG_COLOURS["cream_brown"]):    # returns 'sponge' array. Uses self.width to create row arrays that are added to sponge array. Hight determins the number of rows in the sponge array.
        # example of return, 
        #   height = 3    sponge = [[row 1], [row 2], [row 3]]
        #   height = 1    sponge = [[row 1]]
        pass
    
    def __filling(self, col):                                       # returns one layer of 'filling' array. Hight is 1. Width is self.width - 1 (unit). The filling row should begin with a space (half unit).
        # Note: The row structure will be the same as Sponge array structure
        # to keep everything consistent for the rows.
        # This will help later when I need to use "\n".join(array) to add the new lines between each row

        # example of return,
        #   width = 3   filling_width = width - 1 (2)   filling = [[' ', '..', '..']] # dots represent coloured space
        #   width = 5   filling_width = width - 1 (4)   filling = [[' ', '..', '..', '..', '..']] # dots represent coloured space
        pass

    def __layers(self, num_of_layers=1):                            # returns 'layers' array of rows. Calls __filling and __sponge in a loop set to num_of_layers
        # Note: Because __sponge() and __filling() return arrays within an array, the return array will need each item to be individually copied into it

        # example of return
        #   num_of_layers = 1   layers = [[layer 1 filling 1], [layer 1 filling 2], [layer 1 sponge 1]]
        #   num_of_layers = 3   layers = [[layer 1 filling 1], [layer 1 sponge 1], [layer 2 filling 1], [layer 2 sponge 1], [layer 3 filling 1], [layer 3 sponge 1]]
        pass

    def construct_cake(self):                                       # calls __sponge and __layers to build the rows, sends them to all_cake_rows
        
        pass

    def convert_to_string(self):                                    # returns a single string. uses the self.__all_cake_rows array, converting each row into a string and adds the row to a temp array. Then joining the array using '\n' as the joiner
        return "Working" # test

    def print_cake(self, cake_string):                              # takes the return from convert_to_string as the argument. Prints the name of the cake (self.name) and the cake_string
        print(self.name)
        print(cake_string)




# ----- prototype -----

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

# ----- global functions -----

def make_cake(cake_class_name, cake_unit_width, cake_name="Unamed Cake"):
    try:
        Cake_class = globals()[cake_class_name] # turns a normal string into a class name
        cake = Cake_class(cake_unit_width, cake_name)
        cake.print_cake(cake.convert_to_string())
    except ValueError as error_message:
        print(error_message)

def main():
    print()

    # completed cakes
    make_cake("Fishcake", 7, "Fishcake")
    print() # new line

    # --------------- testing -----------------------
    make_cake("Cake", 20, "Basic cake")


#make_cake("Fishcake", 7, "Fishcake") # Object class method prototype: print_cake(self) 
#make_cake("Cake", 20, "Basic cake")  # Object class method prototype: print_cake(self, ) 



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


