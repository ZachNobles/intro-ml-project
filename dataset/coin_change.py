# input type: list[int]
import sys

def minimum_coins(amount, coins):
    if amount < 0:
        return None, []

    dp = [float("inf")] * (amount + 1)
    previous = [-1] * (amount + 1)
    dp[0] = 0

    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current:
                candidate = dp[current - coin] + 1

                if candidate < dp[current]:
                    dp[current] = candidate
                    previous[current] = coin

    if dp[amount] == float("inf"):
        return None, []

    chosen = []
    current = amount

    while current > 0:
        coin = previous[current]
        chosen.append(coin)
        current -= coin

    return int(dp[amount]), chosen

def main(data):
    coins = [1, 5, 10, 25, 40]
    results = []

    for amount in data:
        count, chosen = minimum_coins(amount, coins)

        results.append({
            "amount": amount,
            "minimum_coins": count,
            "chosen_coins": chosen,
            "total_verified": sum(chosen)
        })

    return results

if __name__ == "__main__":
    input = sys.argv[1:] if len(sys.argv) > 1 else [
        37, 63, 99, 123, 250, 499
    ]
    input = [int(x) for x in input]
    output = main(input)
    print(output)