# Solution Question - Square of sorted Array

# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("output.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#


def sortedSquares(nums: list[int]) -> list[int]:
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
    print(sortedSquares(list(map(int, input().strip().split()))))

# Analyzing Time Complexity of the code:
# Time Complexity: O(n)
# Space Complexity: O(1)
