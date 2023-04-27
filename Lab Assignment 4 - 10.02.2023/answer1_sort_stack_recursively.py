# Solution Question 1 - Sort Stack

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


def sorted_insert(stack: list[int], element: int) -> None:
    """a helper function to insert an element in a sorted manner in a stack.

    Args:
        stack (list[int]): the stack in which the element is to be inserted\n
        element (int): the element to be inserted
    """
    if len(stack) == 0 or element > stack[-1]:
        stack.append(element)
        return
    temp = stack.pop()
    sorted_insert(stack, element)
    stack.append(temp)


def sort_stack(stack: list[int]) -> None:
    """a function to sort a stack using recursion.

    Args:
        stack (list[int]): the stack to be sorted
    """
    if len(stack) != 0:
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)


if __name__ == "__main__":
    s = list(map(int, input().strip().split()))
    sort_stack(s)
    print(*s)

# Complexity Analysis of the above solution:
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Sample input:
# 30 -5 18 14 -3
