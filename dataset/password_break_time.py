# input type: list[int]
import sys

def main(data):
    character_sets = {
        "digits": 10,
        "lowercase": 26,
        "letters": 52,
        "letters_and_digits": 62,
        "printable_subset": 94
    }

    guessing_rates = [
        1_000,
        1_000_000,
        1_000_000_000
    ]

    reports = []

    for length in data:
        if length < 1 or length > 100:
            reports.append({
                "length": length,
                "error": "Length must be between 1 and 100"
            })
            continue

        configurations = {}

        for name, alphabet_size in character_sets.items():
            combinations = alphabet_size ** length

            configurations[name] = {
                "alphabet_size": alphabet_size,
                "combinations": combinations,
                "estimated_seconds": {
                    str(rate): combinations / rate
                    for rate in guessing_rates
                }
            }

        reports.append({
            "password_length": length,
            "configurations": configurations
        })

    return reports

if __name__ == "__main__":
    input = sys.argv[1:] if len(sys.argv) > 1 else [
        4, 8, 12, 16, 20
    ]
    input = [int(x) for x in input]
    output = main(input)
    print(output)