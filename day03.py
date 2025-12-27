from inputs import parse_puzzle_input

### DAY 03
### Can you find the maximum integer made up by non-consecutive digits within
### a number without rearranging the digits?

day = 3


## PART ONE
def part_one():
    banks = parse_puzzle_input(day, "\n", str)

    max_joltages = [] # empty list to hold max joltage of each bank
    
    for bank in banks:
        max_joltage = 0
        
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                joltage = int(bank[i]) * 10 + int(bank[j])
                max_joltage = max(max_joltage, joltage)

        max_joltages.append(max_joltage)

    total = sum(max_joltages)

    return total


## PART TWO
def part_two():
    banks = parse_puzzle_input(day, "\n", str)

    max_joltages = [] # empty list to hold max joltage of each bank

    for bank in banks:
        max_joltage = "" # string
        start = 0
        
        for i in range(12):
            remaining = 12 - i - 1 # amount of digits we need after this one
            end = len(bank) - remaining
            max_battery = max(bank[start:end]) # find max digit (battery)
            max_idx = bank.index(max_battery, start, end) # find index of max digit

            max_joltage += max_battery
            start= max_idx + 1 # new start can only be after current max

        max_joltages.append(int(max_joltage))

    total = sum(max_joltages)

    return total
            

## ANSWERS
answers = [
        [part_one, 16993],
        [part_two, 168617068915447],
]

if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
