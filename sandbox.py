def A(n):
    if n <= 0:
        return 0
    else:
        return n + A(n - 1)

if __name__ == "__main__":
    # print(A(5))  # Output: 15
    # print(A(0))  # Output: 0
    # print(A(-3)) # Output: 0
    # print(A(10)) # Output: 55
    # print(A(1))  # Output: 1
    print(A(6))  # Output: 21


