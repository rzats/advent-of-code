import copy
import os
import sys


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    # The state of the mountain
    mountain = []
    # Shortest path so far
    shortest = []
    # Where we went so far
    went = []

    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    potential_starts = []

    for i, line in enumerate(lines):
        mountain.append([])
        shortest.append([])
        went.append([])
        for j, c in enumerate(line):
            mountain[i].append(c)
            shortest[i].append(500000000)
            went[i].append([500000000, 500000000, 500000000, 500000000])

            # Keep track of start and end positions
            if c == 'S':
                start_x, start_y = i, j
                potential_starts.append([i, j])

            if c == 'a':
                potential_starts.append([i, j])

            if c == 'E':
                end_x, end_y = i, j

    shortest_pt2 = copy.deepcopy(shortest)
    went_pt2 = copy.deepcopy(went)

    # Get elevation - 'a' if start, 'E' if end, ord otherwise
    def get_ord(x, y):
        if mountain[x][y] == 'S':
            return ord('a')
        elif mountain[x][y] == 'E':
            return ord('z')
        else:
            return ord(mountain[x][y])

    to_traverse = [[start_x, start_y, 0]]

    # At each iteration, go up, down, left and right if our current path is more efficient than an existing one
    # Pretty much a reinvented Dijkstra-like algorithm (:
    def traverse():
        for item in to_traverse:
            x, y, current_len = item[0], item[1], item[2]
            to_traverse.remove(item)
            shortest[x][y] = min(shortest[x][y], current_len)

            if went[x][y][0] > current_len + 1 and x > 0 and get_ord(x, y) >= get_ord(x-1, y) - 1:
                went[x][y][0] = current_len + 1
                to_traverse.append([x - 1, y, current_len + 1])

            if went[x][y][1] > current_len + 1 and x < len(mountain) - 1 and get_ord(x, y) >= get_ord(x+1, y) - 1:
                went[x][y][1] = current_len + 1
                to_traverse.append([x + 1, y, current_len + 1])

            if went[x][y][2] > current_len + 1 and y > 0 and get_ord(x, y) >= get_ord(x, y-1) - 1:
                went[x][y][2] = current_len + 1
                to_traverse.append([x, y - 1, current_len + 1])

            if went[x][y][3] > current_len + 1 and y < len(mountain[0]) - 1 and get_ord(x, y) >= get_ord(x, y+1) - 1:
                went[x][y][3] = current_len + 1
                to_traverse.append([x, y + 1, current_len + 1])

    # First star
    while len(to_traverse) > 0:
        traverse()

    print(shortest[end_x][end_y])

    # Second star
    to_traverse = []
    shortest = copy.deepcopy(shortest_pt2)
    went = copy.deepcopy(went_pt2)

    # cool Reddit tip: we *can* iterate through every starting node
    # but putting all of them into the traversal queue at once works too and is a single pass
    for i, potential_start in enumerate(potential_starts):
        to_traverse.append([potential_start[0], potential_start[1], 0])

    while len(to_traverse) > 0:
        traverse()

    print(shortest[end_x][end_y])


if __name__ == "__main__":
    main()
