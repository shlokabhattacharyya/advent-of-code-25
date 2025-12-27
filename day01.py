from inputs import parse_puzzle_input

### DAY 01
### Can you count how many times a rotating safe dial lands on or passes by zero?

day = 1


## PART ONE
def part_one():
    rotations = parse_puzzle_input(day, "\n", str)

    current = 50
    count = 0

    for rotation in rotations:
        direction = rotation[0] # L or R
        shift = int(rotation[1:])

        if direction == "L":
            current = (current - shift) % 100
        else: # if direction == "R"
            current = (current + shift) % 100

        if current == 0:
            count += 1

    return count


## PART TWO
def part_two():
    rotations = parse_puzzle_input(day, "\n", str)

    current = 50
    count = 0

    for rotation in rotations:
        direction = rotation[0] # L or R
        shift = int(rotation[1:])

        # count number of complete rotations and the partial rotation left
        complete = shift // 100
        count += complete
        remaining = shift % 100

        if direction == "L":
            change = -remaining
        else: # if direction == "R"
            change = remaining

        next_position = current + change
        
        if current != 0:
            if direction == "L" and next_position <= 0:
                count += 1
            elif direction == "R"  and next_position >= 100:
                count += 1

        current = next_position % 100
            
    return count


## ANSWERS
answers = [
        [part_one, 969],
        [part_two, 5887],
]

if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
