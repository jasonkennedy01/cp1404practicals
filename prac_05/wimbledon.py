"""
Wimbledon
Estimate: 40 mins 10:54-10:57, 11:08
Actual: 30 mins 11:34
"""
FILENAME = "wimbledon.csv"


def main():
    winners = get_wimbledon_winners()

    winner_to_occurrence = {}
    get_winner_to_occurrences(winner_to_occurrence, winners)

    print("Wimbledon Champions:")
    for items in winner_to_occurrence.items():
        print(items[0], items[1])

    display_winning_countries(winners)


def get_winner_to_occurrences(winner_to_occurrence, winners):
    for winner in winners:
        name = winner[2]
        winner_to_occurrence[name] = winner_to_occurrence.get(name, 0) + 1


def display_winning_countries(winners):
    countries = set(winner[1] for winner in winners)
    print(f"\nThese {len(countries)} countries have won Wimbledon")
    print(", ".join(country for country in sorted(countries)))


def get_wimbledon_winners():
    with open(FILENAME, encoding="utf-8-sig") as in_file:
        in_file.readline()
        winners = in_file.readlines()
    for i, winner in enumerate(winners):
        winners[i] = winner.strip().split(",")
    return winners


main()
