# Solution of Question 1 -  Staircase problem.

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
except FileNotFoundError as e:
    pass


# ---------------------- Code Starts Here ----------------------#


def no_of_stairs(num: int) -> int:
    """
    input: n - number of stairs
    return: int - number of ways to climb the stairs
    """

    # Recursive Solution
    # if num <= 2:
    #     return num
    # elif num == 3:
    #     return 4
    # else:
    #     return no_of_stairs(num-1) + no_of_stairs(num-2) + no_of_stairs(num-3)

    # Dynamic Programming Solution
    arr = [0, 1, 2, 4]
    for i in range(4, num + 1):
        arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])

    return arr[num]


if __name__ == "__main__":
    print(no_of_stairs(int(input())))

# Complexity Analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(n)
