# Solution to Question 1 - Check palindrome.

import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# Comment the above 4 lines if you are not using file input output.


def check_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return "True"
    else:
        if s == s[::-1]:
            return "True"
        else:
            return "False"


if __name__ == "__main__":
    print(check_palindrome(input()))
