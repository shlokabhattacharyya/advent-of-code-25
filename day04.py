from inputs import parse_puzzle_input
import numpy as np

### DAY 04
### Can you find grid positions with fewer than four adjacent cells and calculate
### the total amount removable?

day = 4


## PART ONE
def part_one():
    lines = parse_puzzle_input(day, "\n", str)
    grid = np.array([[1 if c == '@' else 0 for c in line] for line in lines]) # P.S. this is the first ever documented transition of me turning into a one-liner for loops

    accessible = [] # empty list to hold number of accessible rolls

    # pad the grid with 0s to handle edge cases
    padded = np.pad(grid, pad_width = 1, mode = 'constant', constant_values = 0)

    # count neighbors by summing 8 shifted versions of the grid
    neighbor_count = np.zeros_like(grid)

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue # skip
            neighbor_count += padded[1+di:1+di+grid.shape[0],
                                 1+dj:1+dj+grid.shape[1]]

    # explanation of loop above using examples:
    #   iteration 1: di = -1, dj = -1 (top left)
    #                padded[0:height, 0:weight]
    #   iteration 2: di = -1, dj = 0 (top center)
    #                padded[0:height, 1:1+width]
    #   iteration 3: di = -1, dj = 1 (top right)
    #                padded[0:height, 2:2+width]
    #   iteration 4: di = 0, dj = -1 (middle left)
    #                padded[1:1+height, 0:width]
    #   iteration 5: di = 0, dj = 0 (middle center)
    #                skipped by continue
    #   iteration 6: di = 0, dj = 1 (middle right)
    #                padded[1:1+height, 2:2+width]
    #   iteration 7: di = 1, dj = -1 (bottom left)
    #                padded[2:2+height, 0:width]
    #   iteration 8: di = 1, dj = 0 (bottom center)
    #                padded[2:2+height, 1:1+width]
    #   iteration 9: di = 1, dj = 1
    #                padded[2:2+height, 2:2+width]

    # find accessible rolls (find spots that have paper & fewer than 4 neighbors)
    accessible.append((grid == 1) & (neighbor_count < 4))

    return np.sum(accessible)
                                 

## PART TWO
def part_two():
    lines = parse_puzzle_input(day, "\n", str)
    grid = np.array([[1 if c == '@' else 0 for c in line] for line in lines]) # P.S. this is the first ever documented transition of me turning into a one-liner for loops

    total = 0

    while True:
                
        # pad the grid with 0s to handle edge cases
        padded = np.pad(grid, pad_width = 1, mode = 'constant', constant_values = 0)

        # count neighbors by summing 8 shifted versions of the grid
        neighbor_count = np.zeros_like(grid)

        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue # skip
                neighbor_count += padded[1+di:1+di+grid.shape[0],
                                         1+dj:1+dj+grid.shape[1]]

        # find accessible rolls (find spots that have paper & fewer than 4 neighbors)
        accessible = (grid == 1) & (neighbor_count < 4)

        # count how many we found
        n = np.sum(accessible)

        # if none were found, then we're done
        if n == 0:
            break

        # remove them (set to 0)
        grid[accessible] = 0

        # add to total
        total += n
        
    return total
                                 

## ANSWERS
answers = [
        [part_one, 1411,
        [part_two, 8557],
]

if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
