import re


def parse_engine_schematic(test):
    with open(f"input{'.test' if test else ''}") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    numbers = []
    symbols = []
    for line in parse_engine_schematic(test=False):
        LINE_LENGTH = len(line) - 1

        numbers.append([m for m in re.finditer(r"\d\d*", line)])

        pointless_line = line.replace(".", "a")
        symbols.append([m for m in re.finditer(r"\W", pointless_line)])

    i = 0
    part_numbers = []
    for line in numbers:
        for number in line:
            start = number.start()
            end = number.end()
            possible_indexes = [
                index for index in range(start - 1, end + 1)
                if index >= 0 and index <= LINE_LENGTH
            ]

            int_number = int(number.group())
            added = False
            if i > 0:
                for symbol in symbols[i - 1]:
                    if symbol.start() in possible_indexes:
                        part_numbers.append(int_number)
                        added = True

            for symbol in symbols[i]:
                if symbol.start() in range(start - 1, end + 1) and not added:
                    part_numbers.append(int_number)
                    added = True

            if i + 1 <= LINE_LENGTH and not added:
                for symbol in symbols[i + 1]:
                    if symbol.start() in possible_indexes:
                        part_numbers.append(int_number)
                        added = True

        i += 1
    print(sum(part_numbers))

    # ----------------------------

    i = 0
    gears = []
    for line in symbols:
        for symbol in line:
            if symbol.group() != "*":
                continue

            start = symbol.start()
            possible_indexes = [
                index for index in range(start - 1, start + 2)
                if index >= 0 and index <= LINE_LENGTH
            ]

            found_one = None
            found_two = None
            error = False
            if i > 0:
                for number in numbers[i - 1]:
                    if (
                        number.start() in possible_indexes
                        or number.end() - 1 in possible_indexes
                    ):
                        if found_one is None:
                            found_one = number.group()
                        elif found_two is None:
                            found_two = number.group()
                        else:
                            error = True

            if i + 1 <= LINE_LENGTH:
                for number in numbers[i + 1]:
                    if (
                        number.start() in possible_indexes
                        or number.end() - 1 in possible_indexes
                    ):
                        if found_one is None:
                            found_one = number.group()
                        elif found_two is None:
                            found_two = number.group()
                        else:
                            error = True

            if not error:
                for number in numbers[i]:
                    if (
                        number.start() - 1 == start
                        or number.end() == start
                    ):
                        if found_one is None:
                            found_one = number.group()
                        elif found_two is None:
                            found_two = number.group()
                        else:
                            error = True

            if not error and found_one is not None and found_two is not None:
                gears.append(int(found_one) * int(found_two))

        i += 1
    print(sum(gears))
