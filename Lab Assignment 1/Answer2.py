import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# Comment the above 4 lines if you are not using file input output.


def brick_game(n):
    rounds = int((((9+24*n)**0.5)-3)/6)
    bricks = (3*rounds + 3*(rounds**2))/2

    if n-bricks > rounds+1:
        return "Motu"
    elif n-bricks == 0:
        return "Motu"
    else:
        return "Patlu"


if __name__ == "__main__":
    print(brick_game(int(input())))
