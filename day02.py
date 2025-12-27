from inputs import parse_puzzle_input

### DAY 02
### Can you find and add up all of the numbers with sequences of exactly or at
### least twice-repeated digits within given ranges?

day = 2


## PART ONE
def part_one():
    id_ranges = parse_puzzle_input(day, ",", str)

    invalid_ids = [] # list to hold all invalid ids
    total = 0 # sum of invalid ids

    for id_range in id_ranges:
        
        # define id range
        if "-" in id_range:
            parts = id_range.split("-")
            first_id = int(parts[0])
            last_id = int(parts[1])
        else:
            continue
            
        # iterate over list to find invalid ids
        for id_number in range(first_id, last_id + 1):
            id_number_str = str(id_number)
            n = len(id_number_str)
            if n % 2 != 0: # do nothing for ids with odd number of digits
                pass 
            else: # if n % 2 == 0
                x = n // 2 # midway point
                first_half = int(id_number_str[:x])
                second_half = int(id_number_str[x:])
                if first_half == second_half: # check if they match
                    invalid_ids.append(id_number)

    total = sum(invalid_ids)
    
    return total



## PART TWO
def part_two():
    id_ranges = parse_puzzle_input(day, ",", str)

    invalid_ids = [] # list to hold all invalid ids
    total = 0 # sum of invalid ids

    for id_range in id_ranges:
        
        # define id range
        first_id = 0
        last_id = 0
        if "-" in id_range:
            parts = id_range.split("-")
            first_id = int(parts[0])
            last_id = int(parts[1])
        else:
            continue
            
        # iterate over list to find invalid ids
        for id_number in range(first_id, last_id + 1):
            id_number_str = str(id_number)
            n = len(id_number_str)

            factors = []
            for i in range(1, n): # do not include n
                if n % i == 0:
                    factors.append(i)

            # split each number into equal parts
            is_invalid = False
            for factor in factors:
                parts = [id_number_str[j:j+factor] for j in range(0, n, factor)]

                # check if parts are equal to each other
                if len(set(parts)) == 1:
                    invalid_ids.append(id_number)
                    is_invalid = True
                    break

    total = sum(invalid_ids)
    
    return total


## ANSWERS
answers = [
        [part_one, 40055209690],
        [part_two, 50857215650],
]

if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
