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

def letterCasePermutation(S):
    res = ['']
    for ch in S:
        if ch.isalpha():
            res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i+ch for i in res]
    return res

if __name__ == "__main__":
    S = "a1b2"
    result = letterCasePermutation(S)
    print(result)