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
def knapSack(W: int, wt: list[int], val: list[int]) -> int:
    """0 1 Knapsack Problem using Dynamic Programming

    Args:
        W (int): weight of knapsack
        wt (list[int]): list of weights of items\n
        val (list[int]): list of values of items\n
        n (int): number of items\n

    Returns:
        int: maximum value of knapsack
    """

    n = len(wt)

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
    print(
        knapSack(
            int(input("Enter the capacity of knapsack:\n")),
            list(map(int, input("Enter the weights:\n").split())),
            list(
                map(int, input("Enter the profits for respective weights:\n").split())
            ),
        )
    )

# Complexity Analysis of the above solution:
# Time Complexity: O(n*W)
# Space Complexity: O(W)

# Sample Input:
# 50
# 10 20 30
# 60 100 120
