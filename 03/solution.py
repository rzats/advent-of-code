import os

def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]
    
    # Get single-rucksack priorities
    priority = 0
    for line in lines:
        half = len(line) // 2
        first = line[:len(line)-half]
        second = line[half:]
        for c in first:
            if c in second:
                if c.islower():
                    priority += ord(c) - 96
                else:
                    priority += ord(c) - 38
                break
    
    print(priority)

    # Get three-rucksack priorities
    priority = 0
    for l1, l2, l3 in zip(*[iter(lines)]*3):
        for c in l1:
            if c in l2 and c in l3:
                if c.islower():
                    priority += ord(c) - 96
                else:
                    priority += ord(c) - 38
                break
    print(priority)



if __name__ == "__main__":
    main()