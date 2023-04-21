# Solution of Question 2 -  Motu Patlu Brick Game.

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


def brick_game(num: int) -> str:
    """A function to determine the winner of the game.

    Args:
        num (int): number of bricks

    Returns:
        str: name of the winner "Motu" or "Patlu"
    """

    rounds = int((((9 + 24 * num) ** 0.5) - 3) / 6)
    bricks = (3 * rounds + 3 * (rounds**2)) / 2

    if num - bricks > rounds + 1:
        return "Motu"
    elif num - bricks == 0:
        return "Motu"
    else:
        return "Patlu"


if __name__ == "__main__":
    print(brick_game(int(input())))

# Complexity Analysis of the above solution:
# Time Complexity: O(1)
# Space Complexity: O(1)
