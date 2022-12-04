import os


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    # Calculate scores! ...if the strategy guide is followed
    score = 0
    for line in lines:
        symbols = line.split(" ")

        # Shape score
        if symbols[1] == 'X':
            score += 1
        elif symbols[1] == 'Y':
            score += 2
        else:
            score += 3

        # Round score
        if symbols[0] == 'A' and symbols[1] == 'X':
            score += 3
        elif symbols[0] == 'A' and symbols[1] == 'Y':
            score += 6
        elif symbols[0] == 'A' and symbols[1] == 'Z':
            score += 0
        elif symbols[0] == 'B' and symbols[1] == 'X':
            score += 0
        elif symbols[0] == 'B' and symbols[1] == 'Y':
            score += 3
        elif symbols[0] == 'B' and symbols[1] == 'Z':
            score += 6
        elif symbols[0] == 'C' and symbols[1] == 'X':
            score += 6
        elif symbols[0] == 'C' and symbols[1] == 'Y':
            score += 0
        else:
            score += 3

    print(score)

    # Calculate scores! ...if you do a little cheating
    score = 0
    for line in lines:
        symbols = line.split(" ")

        # Round score
        if symbols[1] == 'X':
            score += 0
        elif symbols[1] == 'Y':
            score += 3
        else:
            score += 6

        # Shape score
        if symbols[0] == 'A' and symbols[1] == 'X':
            # losing to rock -> must choose scissors
            score += 3
        elif symbols[0] == 'A' and symbols[1] == 'Y':
            # drawing to rock -> must choose rock
            score += 1
        elif symbols[0] == 'A' and symbols[1] == 'Z':
            # winning to rock -> must choose paper
            score += 2
        elif symbols[0] == 'B' and symbols[1] == 'X':
            # losing to paper -> must choose rock
            score += 1
        elif symbols[0] == 'B' and symbols[1] == 'Y':
            # drawing to paper -> must choose paper
            score += 2
        elif symbols[0] == 'B' and symbols[1] == 'Z':
            # winning to paper -> must choose scissors
            score += 3
        elif symbols[0] == 'C' and symbols[1] == 'X':
            # losing to scissors -> must choose paper
            score += 2
        elif symbols[0] == 'C' and symbols[1] == 'Y':
            # drawing to scissors -> must choose scissors
            score += 3
        else:
            # winning to scissors -> must choose rock
            score += 1

    print(score)


if __name__ == "__main__":
    main()
