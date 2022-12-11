import copy
import os


class Monke:
    def __init__(self, items, op1, op2, divisible, yeet_true, yeet_false):
        self.items = items
        self.op1 = op1
        self.op2 = op2 if op2 == "old" else int(op2)
        self.divisible = int(divisible)
        self.yeet_true = int(yeet_true)
        self.yeet_false = int(yeet_false)
        self.counter = 0

    def add_item(self, item):
        self.items.append(item)

    def inspect(self, worry_decreases=True):
        yeet_where = []
        while len(self.items) > 0:
            self.counter += 1

            item = self.items.pop(0)
            op2 = item if self.op2 == "old" else self.op2
            if self.op1 == "+":
                item = item + op2
            elif self.op1 == "*":
                item = item * op2

            if worry_decreases:
                item = item // 3

            if item % self.divisible == 0:
                yeet_where.append([item, self.yeet_true])
            else:
                yeet_where.append([item, self.yeet_false])
        return yeet_where

    def __repr__(self):
        return f"Items: {self.items}; operation: new = old {self.op1} {self.op2}; check: divisible by {self.divisible}, yeet if true: {self.yeet_true}, yeet if false: {self.yeet_false}; counter: {self.counter}"


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    monkes = []
    common_denominator = 1
    for i, line in enumerate(lines):
        if line.startswith("Monkey"):
            items = [int(x.replace(",", " ").strip()) for x in lines[i + 1].split(" ") if x.replace(",", " ").strip().isdigit()]
            op1 = lines[i+2].strip().split(" ")[4]
            op2 = lines[i+2].strip().split(" ")[5]
            divisible = lines[i+3].strip().split(" ")[3]
            common_denominator *= int(divisible)
            yeet_true = lines[i+4].strip().split(" ")[5]
            yeet_false = lines[i+5].strip().split(" ")[5]
            monkes.append(Monke(items, op1, op2, divisible, yeet_true, yeet_false))
    monkes2 = copy.deepcopy(monkes)

    # First star - 20 cycles
    for _ in range(20):
        for monke in monkes:
            yeet_where = monke.inspect()
            for yeet in yeet_where:
                monkes[yeet[1]].add_item(yeet[0])

    counters = []
    for monke in monkes:
        counters.append(monke.counter)
    counters.sort(reverse=True)
    print(counters[0] * counters[1])

    # Second star - 10k cycles + cap
    for _ in range(10000):
        for monke in monkes2:
            yeet_where = monke.inspect(worry_decreases=False)
            for yeet in yeet_where:
                monkes2[yeet[1]].add_item(yeet[0] % common_denominator)

    counters = []
    for monke in monkes2:
        counters.append(monke.counter)
    counters.sort(reverse=True)
    print(counters[0] * counters[1])


if __name__ == "__main__":
    main()
