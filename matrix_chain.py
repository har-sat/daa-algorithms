def matrix_chain(d):
    # n is the number of matrices
    n = len(d) - 1

    dp = {
        (i, j): (0 if i == j else float("inf"), 0)
        for i in range(1, n + 1)
        for j in range(i, n + 1)
    }

    for r in range(n):
        for i in range(1, n - r + 1):
            j = i + r
            for k in range(i, j):
                cost = dp[i, k][0] + dp[k + 1, j][0] + d[i - 1] * d[k] * d[j]
                if cost < dp[i, j][0]:
                    dp[i, j] = cost, k

    def get_order(i, j):
        if i == j:
            return f"M{i}"
        k = dp[i, j][1]
        return f"({get_order(i, k)}{get_order(k+1,j)})"

    min_cost = dp[i, j][0]
    order = get_order(1, n)

    return min_cost, order


print(*matrix_chain([1, 2, 3, 4, 3]))
