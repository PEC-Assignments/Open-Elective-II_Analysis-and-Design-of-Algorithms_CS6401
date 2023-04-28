# Solution to Question - Edit Distance

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


class Solution:
    """Class to implement Edit Distance Algorithm"""

    def editDistance(self, s: str, t: str) -> int:
        """Function to find the minimum number of operations
        required to convert string s to string t

        Args:
            s (str): the source string\n
            t (str): the target string

        Returns:
            int: the minimum number of operations required to convert string s to string t
        """
        n = len(s)
        m = len(t)
        prev = list(range(m + 1))
        curr = [0] * (m + 1)
        for i in range(1, n + 1):
            curr[0] = i
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    mn = min(1 + prev[j], 1 + curr[j - 1])
                    curr[j] = min(mn, 1 + prev[j - 1])
            prev = curr.copy()
        return prev[m]


if __name__ == "__main__":
    ob = Solution()
    ans = ob.editDistance(input(), input())
    print(ans)

# Complexity Analysis of the above solution:
# Time Complexity: O(n*m)
# Space Complexity: O(m+n)

# Sample input:
# Anshuman
# Antihuman
