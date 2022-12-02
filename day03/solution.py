"""
--- Day 3: Rucksack Reorganization ---

The elves have packed lots of items into their rucksacks, but they seem to have some duplicates...

Part 1: Find out how many, in two halves of the same rucksack!s
Part 2: Find out how many, in three elves from a group!
"""


def input():
    with open("input.txt") as input:
        lines = input.read()

    # No transformations here!
    rucksacks = lines.split("\n")

    return rucksacks


def to_priority(item):
    """
    Convert a letter into a numeric priority:
    a-z 1-26
    A-Z 27-50
    """
    if item.islower():
        # ASCII code of 'a' is 97, but we subtract 1 so it starts off as 1
        return ord(item) - (97 - 1)
    # ASCII code of 'A' is 65, but we subtract 27 so it starts off as 27
    return ord(item) - (65 - 27)


def common_item(rucksack):
    """
    Get the common item from two halves of the same rucksack.
    """
    # Split into two halves (and convert to character sets, for efficiency)
    first_half, second_half = set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :])
    for item in first_half:
        if item in second_half:
            return item


def part1(rucksacks):
    """
    Find the common items in two halves of each rucksack.
    """
    sum_of_commons = 0
    for rucksack in rucksacks:
        sum_of_commons += to_priority(common_item(rucksack))
    return sum_of_commons


def part2(rucksacks):
    """
    Find the common items in elf groups. Each group is three elves in order.
    """
    sum_of_commons = 0
    for i in range(0, len(rucksacks) // 3):
        first, second, third = set(rucksacks[i * 3]), set(rucksacks[i * 3 + 1]), set(rucksacks[i * 3 + 2])
        for item in first:
            if item in second and item in third:
                sum_of_commons += to_priority(item)
                break
    return sum_of_commons


def main():
    rucksacks = input()
    print(f"Part 1 answer: {part1(rucksacks)}; part 2 answer: {part2(rucksacks)}")


if __name__ == "__main__":
    main()
