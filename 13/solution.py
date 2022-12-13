import json
import os
from functools import cmp_to_key


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    pairs = []
    packets = [json.loads("[[2]]"), json.loads("[[6]]")]
    first = None
    second = None
    for line in lines:
        if line == '':
            if first is not None and second is not None:
                pairs.append([first, second])
                first = None
                second = None
        elif first is None:
            first = json.loads(line)
            packets.append(json.loads(line))
        else:
            second = json.loads(line)
            packets.append(json.loads(line))

    def compare(v1, v2):
        if isinstance(v1, int) and isinstance(v2, int):
            if v1 < v2:
                return 1
            elif v1 > v2:
                return -1
            else:
                return 0
        elif isinstance(v1, int) and isinstance(v2, list):
            return compare([v1], v2)
        elif isinstance(v1, list) and isinstance(v2, int):
            return compare(v1, [v2])
        else:
            for index in range(len(v1)):
                if index > len(v2) - 1:
                    return -1
                comp = compare(v1[index], v2[index])
                if comp != 0:
                    return comp
            if len(v1) == len(v2):
                return 0
            else:
                return 1

    # First star
    indices = []
    for i, pair in enumerate(pairs):
        comp = compare(pair[0], pair[1])
        if comp >= 0:
            indices.append(i + 1)

    print(sum(indices))

    # Second star
    decoder_key = 1
    sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    for i, s in enumerate(sorted_packets):
        if s == json.loads("[[2]]") or s == json.loads("[[6]]"):
            decoder_key *= i + 1
    print(decoder_key)


if __name__ == "__main__":
    main()
