import os


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    interesting_cycles = [20, 60, 100, 140, 180, 220]
    line_cycles = [40, 80, 120, 160, 200, 240]
    signal_strength = 0

    X = 1
    cycle = 1
    signal_strength = 0
    sprite = ""

    def increment_cycle(cycle, signal_strength, sprite):
        if cycle in interesting_cycles:
            signal_strength += X * cycle
        if abs(cycle % 40 - X - 1) <= 1:
            sprite += "#"
        else:
            sprite += "."
        if cycle in line_cycles:
            sprite += "\n"
        return cycle + 1, signal_strength, sprite


    for line in lines:
        if line == 'noop':
            cycle, signal_strength, sprite = increment_cycle(cycle, signal_strength, sprite)
        else:
            cycle, signal_strength, sprite = increment_cycle(cycle, signal_strength, sprite)
            cycle, signal_strength, sprite = increment_cycle(cycle, signal_strength, sprite)
            X += int(line.split(" ")[1])


    print(signal_strength)
    print(sprite)


if __name__ == "__main__":
    main()
