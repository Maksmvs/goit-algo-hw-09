import time

def find_coins_greedy(amount):
    start_time = time.time_ns()
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}

    for coin in coins:
        if amount >= coin:
            coin_count[coin] = amount // coin
            amount %= coin

    end_time = time.time_ns()
    execution_time = end_time - start_time

    return coin_count, execution_time

def main():
    amount = int(input("Введіть суму для видачі решти: "))
    coins, time_taken_ns = find_coins_greedy(amount)
    print("Монети для видачі решти:")
    for coin, count in coins.items():
        print(f"{coin} грн: {count} шт.")
    print(f"Час виконання: {time_taken_ns} наносекунд")

if __name__ == "__main__":
    main()
