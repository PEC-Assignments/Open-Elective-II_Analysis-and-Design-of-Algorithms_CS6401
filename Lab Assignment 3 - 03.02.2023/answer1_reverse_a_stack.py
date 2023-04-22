# Solution Question 1 - Reverse Stack using Recursion.

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


def reverse_stack(stack: list) -> None:
    """function to reverse the stack using recursion.

    Args:
        stack (list): a stack of integers
    """
    if len(stack) == 0:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)


def insert_at_bottom(stack: list, item: int) -> None:
    """a helper function to insert an item at the bottom of the stack.

    Args:
        stack (list): a stack of integers
        item (int): item to be inserted at the bottom of the stack
    """
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)


if __name__ == "__main__":
    stk = list(map(int, input().strip().split()))
    reverse_stack(stk)
    print(*stk)

# Complexity Analysis of the above solution:
# Time Complexity: O(n^2)
# Space Complexity: O(n)
