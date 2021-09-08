import math


def climbstairs(n):
    x = int(n / 2)
    ways = 1  # 全部為1時算一次=
    one_sum = 0  # 1的個數

    for i in range(1, x+1):  # i為2的個數
        one_sum = n - (i * 2)
        ways = ways + int(math.factorial(one_sum + i) /
                          (math.factorial(one_sum) * math.factorial(i)))

    print(ways)


def main():
    climbstairs(1)
    climbstairs(2)
    climbstairs(3)
    climbstairs(4)
    climbstairs(5)
    climbstairs(6)
    climbstairs(7)
    climbstairs(17)


if __name__ == "__main__":
    main()
