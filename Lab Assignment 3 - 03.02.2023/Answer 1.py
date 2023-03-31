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

def reverseStack(stack):
    if len(stack) == 0:
        return
    temp = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, temp)


def insertAtBottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.append(temp)


if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    reverseStack(stack)
    print(stack)
