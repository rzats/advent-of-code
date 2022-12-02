"""
--- Day 2: Rock Paper Scissors ---

A rock-paper-scissors tournament is in progress, and you get a cheeky strategy guide!

Part 1: What if you follow the unclear instructions?
Part 2: What if you follow the proper instructions?
"""


def input():
    with open("input.txt") as input:
        lines = input.read()

    # The strategy guide looks like letter pairs:
    # A Y   B X   C Z
    pairs = [line.split(" ") for line in lines.split("\n")]

    return pairs


def part1(rps_pairs):
    """
    What if X stands for rock, Y stands for paper, Z stands for scissors?
    """
    YOUR_MAPPING = {"X": 1, "Y": 2, "Z": 3}
    OTHER_MAPPING = {"A": 1, "B": 2, "C": 3}

    total_score = 0
    for pair in rps_pairs:
        other_choice, your_choice = OTHER_MAPPING[pair[0]], YOUR_MAPPING[pair[1]]
        # 1 for rock, 2 for paper, 3 for scissors.
        total_score += your_choice
        # You draw if the choices match.
        if other_choice == your_choice:
            total_score += 3
        # You win if: opponent chooses 1 and you choose 2, opponent chooses 2 and you choose 3, opponent chooses 3 and you choose 1.
        elif other_choice % 3 + 1 == your_choice:
            total_score += 6
        # Otherwise you lost! Add nothing to the score.
    return total_score


def part2(rps_pairs):
    """
    What if X stands for a win, Y stands for a draw, Z stands for a loss?
    """
    RIGGED_MAPPING = {"X": 0, "Y": 3, "Z": 6}
    OTHER_MAPPING = {"A": 1, "B": 2, "C": 3}

    total_score = 0
    for pair in rps_pairs:
        other_choice, rigged_result = OTHER_MAPPING[pair[0]], RIGGED_MAPPING[pair[1]]
        # 0 for losing, 3 for drawing, 6 for winning.
        total_score += rigged_result
        # If you lose, opponent chooses 1 and you choose 3, opponent chooses 2 and you choose 1, opponent chooses 3 and you choose 2.
        if rigged_result == 0:
            total_score += (other_choice + 1) % 3 + 1
        # If it's a draw, add the opponent's choice.
        elif rigged_result == 3:
            total_score += other_choice
        # If it's a win, use logic similar to part 1.
        else:
            total_score += other_choice % 3 + 1
    return total_score


def main():
    rps_pairs = input()
    print(f"Part 1 answer: {part1(rps_pairs)}; part 2 answer: {part2(rps_pairs)}")


if __name__ == "__main__":
    main()
