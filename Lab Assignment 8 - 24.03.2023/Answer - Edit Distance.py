# Solution to Question - Edit Distance

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

class Solution:
    def editDistance(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        prev = [j for j in range(m+1)]
        curr = [0] * (m+1)

        for i in range(1, n+1):
            curr[0] = i
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j-1]
                else:
                    mn = min(1 + prev[j], 1 + curr[j-1])
                    curr[j] = min(mn, 1 + prev[j-1])
            prev = curr.copy()

        return prev[m]


if __name__ == "__main__":
    s = "Anshuman"
    t = "Antihuman"

    ob = Solution()
    ans = ob.editDistance(s, t)
    print(ans)
