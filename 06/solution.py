import os


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    input = lines[0]

    # Four distinct characters
    result = -1
    for i in range(0, len(input) - 3):
        chars = set([*input[i:i+4]])
        if len(chars) == 4:
            result = i + 4
            break
    print(result)

    # FOURTEEN distinct characters
    result = -1
    for i in range(0, len(input) - 13):
        chars = set([*input[i:i+14]])
        if len(chars) == 14:
            result = i + 14
            break
    print(result)


if __name__ == "__main__":
    main()
