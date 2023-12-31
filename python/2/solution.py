class Bag:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class CubeSet:
    def __init__(self, cubes_str):
        self.red = self.parse_cube(cubes_str, "red")
        self.green = self.parse_cube(cubes_str, "green")
        self.blue = self.parse_cube(cubes_str, "blue")

    def parse_cube(self, cubes_str, color):
        nb = 0
        for cube_str in cubes_str.split(", "):
            if cube_str.endswith(color):
                nb += int(cube_str.split(f" {color}")[0])
        return nb


class Game:
    def __init__(self, id, game_str):
        self.id = id
        self.cube_sets = self.parse_cube_sets(game_str)
        self.min_red = self.min_number_of_color("red")
        self.min_green = self.min_number_of_color("green")
        self.min_blue = self.min_number_of_color("blue")

    def parse_cube_sets(self, game_str):
        cube_sets = []
        for set_str in game_str.split(";"):
            cube_sets.append(CubeSet(set_str))

        return cube_sets

    def is_bag_possible(self, bag):
        for cube_set in self.cube_sets:
            if (
                cube_set.red > bag.red
                or cube_set.green > bag.green
                or cube_set.blue > bag.blue
            ):
                return False

        return True

    def min_number_of_color(self, color):
        return max(
            getattr(cube_set, color) for cube_set in self.cube_sets
        )


def parse_games(test):
    games = []
    with open(f"input{'.test' if test else ''}") as f:
        i = 1
        for line in f.read().splitlines():
            game_str = line.split(": ")[1]
            games.append(Game(i, game_str))
            i += 1

    return games


class Solution:
    def __init__(self, bag, test):
        self.bag = bag
        self.games = parse_games(test)

    def get_final_number(self):
        final_number = 0
        for game in self.games:
            if game.is_bag_possible(self.bag):
                final_number += game.id

        return final_number


class SecondSolution:
    def __init__(self, test):
        self.games = parse_games(test)

    def get_final_number(self):
        final_number = 0
        for game in self.games:
            final_number += game.min_red * game.min_green * game.min_blue

        return final_number


if __name__ == "__main__":
    solution = Solution(Bag(12, 13, 14), test=False)
    second_solution = SecondSolution(test=False)

    print(solution.get_final_number())
    print(second_solution.get_final_number())



