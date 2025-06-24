# sliding window
# leetcode 121 Best time to buy and sell a stock
# Say you have an array for which the i^th element is the price of a given stock on day l.
# If you were only permitted to complete at most one transaction, (ie buy one and sell one share of the stock)
# design an algorithm to make maxmimun profit.

# Note you cannot sell a stock before you buy one.

# use 2 pointers

# Example 1
# Input [7, 1, 5, 3, 6, 4]
# Output 5
# Explaination: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5,
# Not 7 - 1 = 6, as selling price needs to be larger than the buying price.

# Memory O(1)
# Time O(n)

#!/usr/bin/env python3

def maxProfit(prices):
    """
    Calculate the maximum possible profit from a single stock transaction.

    Args:
        prices (list): A list of stock prices.

    Returns:
        int: The maximum possible profit.
    """
    if not prices:
        return 0

    # Initialize two pointers, one at the start (buy) and one at the start + 1 (sell)
    buy = 0
    sell = 1
    max_profit = 0

    while sell < len(prices):
        # If the price at the sell pointer is less than the price at the buy pointer,
        # move the buy pointer to the sell pointer
        if prices[sell] < prices[buy]:
            buy = sell
        # Otherwise, calculate the profit and update the max_profit if necessary
        else:
            max_profit = max(max_profit, prices[sell] - prices[buy])
        # Move the sell pointer forward
        sell += 1

    return max_profit


def main():
    # Example usage
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))  # Output: 5


if __name__ == "__main__":
    main()
