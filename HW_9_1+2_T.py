import time
from prettytable import PrettyTable

def find_coins_greedy(amount):
    start_time = time.time()  

    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}

    for coin in coins:
        if amount >= coin:
            coin_count[coin] = amount // coin
            amount %= coin

    end_time = time.time()
    execution_time = end_time - start_time 

    return coin_count, execution_time

def find_min_coins(amount):
    if amount > 10000000:
        return {"cannot be calculated": 0}, 0

    start_time = time.time() 

    coins = [1, 2, 5, 10, 25, 50]
    num_coins = [0] * (amount + 1)
    coin_used = [0] * (amount + 1)

    for cents in range(1, amount + 1):
        min_coins = cents
        new_coin = 1
        for j in [c for c in coins if c <= cents]:
            if num_coins[cents - j] + 1 < min_coins:
                min_coins = num_coins[cents - j] + 1
                new_coin = j
        num_coins[cents] = min_coins
        coin_used[cents] = new_coin

    coin_count = {}
    cents = amount
    while cents > 0:
        this_coin = coin_used[cents]
        if this_coin in coin_count:
            coin_count[this_coin] += 1
        else:
            coin_count[this_coin] = 1
        cents = cents - this_coin

    end_time = time.time()  
    execution_time = end_time - start_time  

    return coin_count, execution_time

def main():
    table = PrettyTable()
    table.field_names = ["Алгоритм", "Сума для решти", "Час виконання", "Різниця часу"]

    for i in range(5):
        amount = int(input(f"Введіть {i+1}-у суму для видачі решти: "))
        if amount > 10000000:
            print("Сума для видачі решти занадто велика для обчислення.")
            continue

        coins_greedy, time_greedy = find_coins_greedy(amount)

        coins_dp, time_dp = find_min_coins(amount)

        time_diff = abs(time_greedy - time_dp)

        table.add_row(["Жадібний", amount, round(time_greedy, 6), ""])
        table.add_row(["Динамічний", amount, round(time_dp, 6), round(time_diff, 6)])

    print(table)

if __name__ == "__main__":
    main()