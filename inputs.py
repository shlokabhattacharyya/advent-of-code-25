# FUNCTIONS TO DOWNLOAD PUZZLE INPUT


# get_puzzle_input returns the input for a particular day's puzzles
def get_puzzle_input(day):
    path = f"data/input{str(day).zfill(2)}.txt"

    with open(path, "r") as f:
        return f.read().strip("\n")

# parse_puzzle_input returns the input for a particular day's puzzle, optionally
# splits it via a separator, and applies a parser function to each piece
def parse_puzzle_input(day, sep="", parser=None): # default
    data = get_puzzle_input(day)

    if sep != "":
        data = data.split(sep)

        if parser != None:
            data = [parser(piece) for piece in data]

        return data

    elif parser != None:
        return parser(data)
    else:
        return data
