import math


def parse_races(test):
    with open(f"input{'.test' if test else ''}") as f:
        return f.read().splitlines()


def extract_numbers_from_line(line):
    number = ""
    for c in line:
        if c.isdigit():
            number += c

    return int(number)


def get_distance_for_time_pressed(time, duration):
    return (duration - time) * time


if __name__ == "__main__":
    lines = parse_races(test=False)
    time = extract_numbers_from_line(lines[0])
    distance = extract_numbers_from_line(lines[1])

    winning_strategies = []
    winning_strategies_for_race = 0
    for pressed_time in range(0, time):
        estimated_distance = get_distance_for_time_pressed(pressed_time, time)
        if estimated_distance > distance:
            winning_strategies_for_race += 1

    winning_strategies.append(winning_strategies_for_race)

    print(math.prod(winning_strategies))
