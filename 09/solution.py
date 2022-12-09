import os


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    def adjacent(head_i, head_j, tail_i, tail_j):
        return abs(head_i - tail_i) <= 1 and abs(head_j - tail_j) <= 1

    def adjust(head_i, head_j, tail_i, tail_j):
        if head_i < tail_i:
            tail_i -= 1
        elif head_i > tail_i:
            tail_i += 1
        if head_j < tail_j:
            tail_j -= 1
        elif head_j > tail_j:
            tail_j += 1
        return tail_i, tail_j

    # First star - create grid, place head
    grid = []
    for i in range(1000):
        grid.append([])
        for _ in range(1000):
            grid[i].append(0)

    head_i, head_j, tail_i, tail_j = 500, 500, 500, 500

    grid[tail_i][tail_j] = 1

    # Single-knot rope
    for line in lines:
        direction, steps = line.split(" ")[0], int(line.split(" ")[1])
        for _ in range(steps):
            if direction == 'R':
                head_j += 1
            elif direction == 'L':
                head_j -= 1
            elif direction == 'U':
                head_i -= 1
            else:
                head_i += 1
            if not adjacent(head_i, head_j, tail_i, tail_j):
                tail_i, tail_j = adjust(head_i, head_j, tail_i, tail_j)
            grid[tail_i][tail_j] = 1

    sum = 0
    for gg in grid:
        for g in gg:
            sum += g
    print(sum)

    # Second star - create grid, place head
    grid = []
    for i in range(2000):
        grid.append([])
        for _ in range(2000):
            grid[i].append(0)

    head_i, head_j = 1000, 1000

    knots = []
    NUM_KNOTS = 9
    for i in range(NUM_KNOTS):
        knots.append([head_i, head_i])

    grid[head_i][head_j] = 1

    # Ten-knot rope (ten non-head knots)
    for line in lines:
        direction, steps = line.split(" ")[0], int(line.split(" ")[1])
        for _ in range(steps):
            if direction == 'R':
                head_j += 1
            elif direction == 'L':
                head_j -= 1
            elif direction == 'U':
                head_i -= 1
            else:
                head_i += 1

            if not adjacent(head_i, head_j, knots[0][0], knots[0][1]):
                knots[0][0], knots[0][1] = adjust(
                    head_i, head_j, knots[0][0], knots[0][1])

            for i in range(NUM_KNOTS - 1):
                if not adjacent(knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1]):
                    knots[i+1][0], knots[i+1][1] = adjust(
                        knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1])

            grid[knots[NUM_KNOTS - 1][0]][knots[NUM_KNOTS - 1][1]] = 1

    sum = 0
    for gg in grid:
        for g in gg:
            sum += g
    print(sum)


if __name__ == "__main__":
    main()
