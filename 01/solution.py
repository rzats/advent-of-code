import os

def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]
    
    # Build a list of elves
    elves = []
    current = 0
    for line in lines:
        if line.isdigit():
            current += int(line)
        else:
            elves.append(current)
            current = 0
    elves.append(current)

    # Get the three chonkiest elves :)
    elves.sort()
    print(elves[-3] + elves[-2] + elves[-1])
    
if __name__ == "__main__":
    main()