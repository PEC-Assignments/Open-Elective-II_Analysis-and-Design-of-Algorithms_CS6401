# Solution to Question 2 - Recursive Exponentiation.

import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# Comment the above 4 lines if you are not using file input output.


def pow(i, e):
    if e == 1:
        return i
    else:
        return i * pow(i, e - 1)


if __name__ == "__main__":
    num, exp = map(int, input().strip().split())
    print(pow(num, exp))

# Complexity Analysis of the above solution:
# Time Complexity: O(n)
# Space Complexity: O(1)
