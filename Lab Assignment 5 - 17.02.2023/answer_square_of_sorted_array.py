# Solution Question - Square of sorted Array


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


def sorted_squares(nums: list[int]) -> list[int]:
    """a function to return the sorted square of a sorted array.

    Args:
        nums (list[int]): the array to be sorted

    Returns:
        list[int]: the sorted square of the array
    """

    ans = [0] * len(nums)

    w = len(nums) - 1
    l = 0

    r = len(nums) - 1
    l_square = nums[l] ** 2
    r_square = nums[r] ** 2
    while w >= 0:
        if l_square > r_square:
            ans[w] = l_square
            l += 1
            l_square = nums[l] ** 2
        else:
            ans[w] = r_square
            r -= 1
            r_square = nums[r] ** 2
        w -= 1
    return ans


if __name__ == "__main__":
    print(sorted_squares(list(map(int, input().strip().split()))))

# Complexity Analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(1)
