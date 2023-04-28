# Solution to Question : 0 1 Knapsack Problem using Dynamic Programming

# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#
def knapSack(W: int, wt: list[int], val: list[int], n: int) -> int:
    """0 1 Knapsack Problem using Dynamic Programming

    Args:
        W (int): weight of knapsack
        wt (list[int]): list of weights of items
        val (list[int]): list of values of items
        n (int): number of items

    Returns:
        int: maximum value of knapsack
    """

    # Making the dp array
    dp = [0 for i in range(W + 1)]

    # Taking first i elements
    for i in range(1, n + 1):
        # Starting from back,
        # so that we also have data of
        # previous computation when taking i-1 items
        for wg in range(W, 0, -1):
            if wt[i - 1] <= wg:
                # Finding the maximum value
                dp[wg] = max(dp[wg], dp[wg - wt[i - 1]] + val[i - 1])

    # Returning the maximum value of knapsack
    return dp[W]


# Driver code
if __name__ == "__main__":
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    w = 50
    num = len(profit)
    print(knapSack(w, weight, profit, num))
