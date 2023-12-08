from collections import Counter


def parse_hands(test):
    with open(f"input{'.test' if test else ''}") as f:
        return f.read().splitlines()


def convert_card_to_number(card):
    if card == "T":
        return 10
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    else:
        return int(card)


def calculate_score(hand):
    counts = Counter(hand)

    highest_card = 0
    pair = 0
    three_of_a_kind = 0
    four_of_a_kind = 0
    five_of_a_kind = 0

    for card, count in counts.items():
        nb_card = convert_card_to_number(card)
        if nb_card > highest_card:
            highest_card = nb_card

        if count == 2:
            pair += 1

        if count == 3:
            three_of_a_kind += 1

        if count == 4:
            four_of_a_kind += 1

        if count == 5:
            five_of_a_kind += 1

    if five_of_a_kind == 1:
        return 5000

    if four_of_a_kind == 1:
        return 4000

    if three_of_a_kind == 1 and pair == 1:
        return 3000

    if three_of_a_kind == 1:
        return 2000

    if pair == 2:
        return 1500

    if pair == 1:
        return 1000

    return 0


if  __name__ == "__main__":
    lines = parse_hands(test=False)
    hands = [line.split(" ")[0] for line in lines]
    bids = [line.split(" ")[1] for line in lines]

    results = []
    i = 0
    for hand in hands:
        score = calculate_score(hand)
        results.append(
            (
                int(bids[i]),
                score,
                convert_card_to_number(hand[0]),
                convert_card_to_number(hand[1]),
                convert_card_to_number(hand[2]),
                convert_card_to_number(hand[3]),
                convert_card_to_number(hand[4]),
                hand
            )
        )
        i += 1

    sorted_results = sorted(results, key=lambda x: (x[1], x[2], x[3], x[4], x[5], x[6]))
    final = 0
    j = 1
    for result in sorted_results:
        final += result[0] * j
        j += 1

    print(final)

