def read_file():
    # return [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen",
    # ] # 281
    with open("input", "r") as f:
        return f.read().splitlines()


def convert_str_digits(file):
    lines = []
    keys = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for line in file:
        for digit in (
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        ):

            line = line.replace(digit, f"{digit}{keys[digit]}{digit}")

        lines.append(line)

    return lines

def get_digits_from_line(line):
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)

    return digits

def combine_first_and_last_digit(line):
    first = line[0]
    last = line[-1]

    return int(first + last)


print(sum(
    [
        combine_first_and_last_digit(
            get_digits_from_line(line)
        )
        for line in
        convert_str_digits(
            read_file()
        )
    ]
))
