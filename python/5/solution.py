def parse_maps(test):
    with open(f"input{'.test' if test else ''}") as f:
        return f.read().splitlines()


def build_map(maps):
    to_build = {}
    nb_lines = 0
    for line in maps:
        if line == "":
            break


        if line[0].isdigit():
            numbers = [int(number) for number in line.split(" ")]
            i = 0
            for n in range(numbers[0], numbers[0] + numbers[2] + 1):
                to_build[f"d{numbers[1] + i}"] = n
                i += 1

        nb_lines += 1

    maps = maps[nb_lines + 1:]

    return to_build, maps


def go_up(source_id, destination_map):
    if f"d{source_id}" in destination_map:
        return destination_map[f"d{source_id}"]

    return source_id


if __name__ == "__main__":
    maps = parse_maps(test=False)
    seeds = [int(seed) for seed in maps[0].split(": ")[1].split(" ")]

    seed_to_soil, maps = build_map(maps[2:])
    soil_to_fertilizer, maps = build_map(maps)
    fertilizer_to_water, maps = build_map(maps)
    water_to_light, maps = build_map(maps)
    light_to_temperature, maps = build_map(maps)
    temperature_to_humidity, maps = build_map(maps)
    humidity_to_location, maps = build_map(maps)

    for seed in seeds:
        soil = go_up(seed, seed_to_soil)
        fertilizer = go_up(soil, soil_to_fertilizer)
        water = go_up(fertilizer, fertilizer_to_water)
        light = go_up(water, water_to_light)
        temperature = go_up(light, light_to_temperature)
        humidity = go_up(temperature, temperature_to_humidity)
        location = go_up(humidity, humidity_to_location)

        print(water)

