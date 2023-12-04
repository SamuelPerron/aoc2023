def parse_scratch_cards(test):
    with open(f"input{'.test' if test else ''}") as f:
        return f.read().splitlines()


class Card:
    def __init__(self, id, card_str):
        self.id = id
        self.card_str = card_str
        self.numbers = self.parse_numbers(card_str.split(" | ")[0])
        self.winning_numbers = self.parse_numbers(card_str.split(" | ")[1])

    def parse_numbers(self, card_str):
        numbers = card_str.split(" ")
        return [int(number) for number in numbers if number != ""]

    def compute_points(self):
        points = 0
        for number in self.numbers:
            if number in self.winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        return points

    def compute_total_number_of_winning_numbers(self):
        nb = 0
        for number in self.numbers:
            if number in self.winning_numbers:
                nb += 1

        return nb

    def __repr__(self):
        return f"Card {self.id}"


if __name__ == "__main__":
    i = 1
    total_points = 0
    for card in parse_scratch_cards(test=False):
        card_obj = Card(i, card.split(": ")[1])
        total_points += card_obj.compute_points()
        i += 1
    print(total_points)

    # ----------------------------

    cards_list = {}
    for card in parse_scratch_cards(test=False):
        id = int(card.split(": ")[0].replace("Card ", ""))
        card_obj = Card(id, card.split(": ")[1])
        cards_list[f"c{id}"] = [
            card_obj.compute_total_number_of_winning_numbers(),
            1
        ]

    for id, card in cards_list.items():
        int_id = int(id.replace("c", ""))
        for _ in range(0, card[1]):
            for i in range(1, card[0] + 1):
                cards_list[f"c{int_id + i}"][1] += 1

    print(sum([card[1] for card in cards_list.values()]))


