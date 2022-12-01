"""
--- Day 1: Calorie Counting ---

Elves carry food supplies for their expedition to the deep deep jungle!

Part 1: How many calories is the elf with the most calories carrying?
Part 2: How many calories are the top three elves carrying?
"""


def input():
    with open("input.txt") as input:
        lines = input.read()

    # Elves carry a bunch of items. They looks like this:
    # 1000 2000 3000   4000   5000 6000
    # So first, let's split the input into a list where each element initially looks like this: 1000\n2000\n3000
    # We split by two newlines because that means there's a gap in the elves.
    elves = lines.split("\n\n")

    # And turn that list of lists into a list of calorie sums.
    elf_sums = [sum([int(food) for food in elf.split("\n")]) for elf in elves]
    return elf_sums


def part1(elf_sums):
    """
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    """
    return max(elf_sums)


def part2(elf_sums):
    """
    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    """
    return sum(sorted(elf_sums, reverse=True)[:3])


def main():
    elf_sums = input()
    print(f"Part 1 answer: {part1(elf_sums)}; part 2 answer: {part2(elf_sums)}")


if __name__ == "__main__":
    main()
