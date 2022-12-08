import os


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    # Build 2D arrays
    trees = []
    visibilities = []
    scenic = []

    for i, line in enumerate(lines):
        trees.append([])
        visibilities.append([])
        scenic.append([])
        for j, c in enumerate(line):
            trees[i].append(int(c))

            # Outer edges always visible!
            if i == 0 or i == len(lines) - 1 or j == 0 or j == len(line) - 1:
                visibilities[i].append(1)
            else:
                visibilities[i].append(0)

            scenic[i].append(0)

    # Part 1 - Visibility passes! Horizontal
    for i in range(len(trees)):
        largest = trees[i][0]
        for j in range(0, len(trees[i]) - 1):
            if trees[i][j+1] > largest:
                visibilities[i][j+1] = 1
                largest = trees[i][j+1]
        largest = trees[i][len(trees[i])-1]
        for j in range(len(trees[i]) - 1, 0, -1):
            if trees[i][j-1] > largest:
                visibilities[i][j-1] = 1
                largest = trees[i][j-1]
    # Vertical
    for j in range(len(trees[i])):
        largest = trees[0][j]
        for i in range(0, len(trees) - 1):
            if trees[i+1][j] > largest:
                visibilities[i+1][j] = 1
                largest = trees[i+1][j]
        largest = trees[len(trees)-1][j]
        for i in range(len(trees) - 1, 0, -1):
            if trees[i-1][j] > largest:
                visibilities[i-1][j] = 1
                largest = trees[i-1][j]

    # Sum of visible trees
    sum = 0
    for vv in visibilities:
        for v in vv:
            sum += v
    print(sum)

    # Part 2 - scenic scores!
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            s1, s2, s3, s4 = 0, 0, 0, 0
            k1, k2, k3, k4 = i, i, j, j
            while k1 < len(trees) - 1:
                s1 += 1
                k1 += 1
                if trees[k1][j] >= trees[i][j]:
                    break
            while k2 > 0:
                s2 += 1
                k2 -= 1
                if trees[k2][j] >= trees[i][j]:
                    break
            while k3 < len(trees[i]) - 1:
                s3 += 1
                k3 += 1
                if trees[i][k3] >= trees[i][j]:
                    break
            while k4 > 0:
                s4 += 1
                k4 -= 1
                if trees[i][k4] >= trees[i][j]:
                    break
            scenic[i][j] = s1 * s2 * s3 * s4

    max_score = 0
    for ss in scenic:
        for s in ss:
            max_score = max(s, max_score)
    print(max_score)


if __name__ == "__main__":
    main()
