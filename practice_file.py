def n_queens(n):
    cols = set()
    posDiag = set()
    negDiag = set()

    board = [[0] * n for _ in range(n)]
    res = []

    def backtrack(r):
        # solution found
        if r == n:
            # deep copy row
            res.append([row[::] for row in board])
            return

        for c in range(n):
            if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # put queen at r, c
            board[r][c] = 1
            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)

            backtrack(r + 1)

            # remove the queen at r, c if backtracking
            # fails to give solution
            board[r][c] = 0
            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)

    backtrack(0)
    return res


res = n_queens(16)

for board in res:
    for row in board:
        print(*row)
    print("----")
