import os


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    contained = 0
    overlapping = 0

    for line in lines:
        first, second = line.split(",")
        f1, f2 = map(int, first.split("-"))
        s1, s2 = map(int, second.split("-"))

        # Check if one interval contains another
        if (f1 >= s1 and f2 <= s2) or (s1 >= f1 and s2 <= f2):
            print(f"contained {line} {f1} {f2} {s1} {s2}")
            contained += 1
        else:
            print(f"not contained {line} {f1} {f2} {s1} {s2}")
            pass

        # Check if two intervals overlap
        if (f1 > s1 and f2 > s1 and f1 > s2 and f2 > s2) or (s1 > f2 and s2 > f2 and s1 > f1 and s2 > f1):
            print(f"not overlapping {line} {f1} {f2} {s1} {s2}")
        else:
            print(f"overlapping {line} {f1} {f2} {s1} {s2}")
            overlapping += 1

    print(contained)
    print(overlapping)


if __name__ == "__main__":
    main()
