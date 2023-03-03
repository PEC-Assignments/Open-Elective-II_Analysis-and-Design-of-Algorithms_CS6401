# Solution of Question 1.

def no_of_stairs(n):

    # Recursive Solution

    # if n <= 2:
    #     return n
    # elif n == 3:
    #     return 4
    # else:
    #     return no_of_stairs(n-1) + no_of_stairs(n-2) + no_of_stairs(n-3)

    # Dynamic Programming Solution

    arr = [0, 1, 2, 4]
    for i in range(4, n+1):
        arr.append(arr[i-1] + arr[i-2] + arr[i-3])

    return arr[n]


if __name__ == "__main__":
    print(no_of_stairs(int(input())))
