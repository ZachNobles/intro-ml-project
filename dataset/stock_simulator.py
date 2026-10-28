# input type: list[float]
import sys
import random

def main(investments):
    portfolio = investments.copy()
    history = []

    for day in range(30):
        portfolio = [
            value * random.uniform(0.97, 1.04)
            for value in portfolio
        ]
        history.append(round(sum(portfolio), 2))

    return {
        "initial_value": round(sum(investments), 2),
        "final_value": history[-1],
        "best_day_value": max(history),
        "worst_day_value": min(history),
        "daily_totals": history
    }

if __name__ == "__main__":
    input = [float(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [1000, 2500, 500]
    output = main(input)
    print(output)