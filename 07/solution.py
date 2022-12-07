import os
import sys


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    # Filesystem
    fs = {}
    # Working directory
    pwd = []
    for line in lines:
        # Process cd commands (ls does nothing for us)
        if line.startswith("$"):
            commands = line.split(" ")
            if commands[1] == "cd":
                # Go to root directory
                if commands[2] == "/":
                    pwd = []
                # Remove last directory
                elif commands[2] == "..":
                    pwd.pop()
                # Add extra directory
                else:
                    pwd.append(commands[2])
        # Process dir commands - add empty dict
        elif line.startswith("dir"):
            wd = fs
            for dir in pwd:
                wd = wd[dir]
            wd[line.split(" ")[1]] = {}
        # Process filesize commands - add new file
        else:
            wd = fs
            for dir in pwd:
                wd = wd[dir]
            wd[line.split(" ")[1]] = int(line.split(" ")[0])

    # Get directory sizes
    dirs_sizes = {}

    def get_directory_sizes(dir, name):
        sum = 0
        for k, v in dir.items():
            # Append size of file
            if isinstance(v, int):
                sum += v
            # Append size of directory (recursive!)
            else:
                sum += get_directory_sizes(v, f"{name}/{k}")
        dirs_sizes[name] = sum
        return sum

    get_directory_sizes(fs, '/')

    # First star - total size of directories with size less than 100k
    sum_totals = 0
    for _, v in dirs_sizes.items():
        if v <= 100000:
            sum_totals += v
    print(sum_totals)

    # Second star - least large directory deleting which will bring total disk space to <40M
    size_to_free = dirs_sizes['/'] - 40000000
    min_to_free = sys.maxsize
    for _, v in dirs_sizes.items():
        if v >= size_to_free and v < min_to_free:
            min_to_free = v
    print(min_to_free)


if __name__ == "__main__":
    main()
