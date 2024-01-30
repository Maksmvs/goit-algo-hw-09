import time

def find_min_coins(amount):
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
    amount = int(input("Введіть суму для видачі решти: "))
    coins, time_taken = find_min_coins(amount)
    print("Монети для видачі решти:")
    for coin, count in coins.items():
        print(f"{coin} грн: {count} шт.")
    print(f"Час виконання: {time_taken} секунд")

if __name__ == "__main__":
    main()
