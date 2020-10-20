


# Peak Valley Approach
# initial index, peak, valley, max_profit variables
# iterate over prices
# iterate to find peaks and valleys
# while if price[i] >= price[i + 1] increment index by one
# define valley based off the condition
# while if price[i] <= price[i + 1] increment index by one
# define peak based off the condition
# calulate max_profile (peak - valley)

def best_time_to_buy_and_sell_stock_II(prices):
    index = 0
    max_profit = 0
    peak = prices[0]
    valley = prices[0]

    while index < len(prices) - 1:

        while index < len(prices) - 1 and prices[index] >= prices[index + 1]:
            index += 1
        peak = prices[index]

        while index < len(prices) - 1 and prices[index] <= prices[index + 1]:
            index += 1
        valley = prices[index]

        max_profit += abs(peak - valley)

    return max_profit

def best_time_to_buy_and_sell_stock_II_2(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit




















if __name__ == '__main__':


    r1 = best_time_to_buy_and_sell_stock_II_2([7,1,5,3,6,4])

    print(r1)
