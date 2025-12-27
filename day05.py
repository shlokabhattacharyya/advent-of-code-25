from inputs import parse_puzzle_input

### DAY 05
### Can you filter a list of numbers by checking if they fall within given
### ranges and count the total unique numbers covered by those ranges?

day = 5


## PART ONE
def part_one():
    id_ranges_and_ids = parse_puzzle_input(day, "\n", str)

    id_ranges_str = []
    ids_str = []

    for line in id_ranges_and_ids:
        if not line:
            continue
        if "-" in line:
            id_ranges_str.append(line)
        else:
            ids_str.append(line)

    count = 0
    
    for id_to_check in ids_str:
        id_to_check = int(id_to_check)
        is_fresh = False
        
        for id_range in id_ranges_str:
            # define id range
            if "-" in id_range:
                parts = id_range.split("-")
                first_id = int(parts[0])
                last_id = int(parts[1])

            # iterate over id range to find if id to check is in range
            if first_id <= id_to_check <= last_id:
                is_fresh = True
                break

        if is_fresh:
            count+= 1

    return count
                    


## PART TWO
def part_two():
    id_ranges_and_ids = parse_puzzle_input(day, "\n", str)

    id_ranges = []
    ids = set() # set to handle duplicates

    for line in id_ranges_and_ids:
        if not line:
            continue
        if "-" in line:
            parts = line.split("-")
            first_id = int(parts[0])
            last_id = int(parts[1])
            id_ranges.append((first_id, last_id))
        else:
            continue

    id_ranges.sort() # sort ranges by start position

    # merge overlapping ranges
    merged = []
    for start, end in id_ranges:
        if merged and start <= merged[-1][1] + 1:
            # overlapping or adjacent get merged
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # non-ovelapping get added as new range
            merged.append((start, end))

    # count total ids
    total = 0
    for start, end in merged:
        total += (end - start + 1)

    return total


## ANSWERS
answers = [
        [part_one, 720],
        [part_two, 357608232770687],
]

if __name__ == "__main__":
    print("part one: ", part_one())
    print("part two: ", part_two())
