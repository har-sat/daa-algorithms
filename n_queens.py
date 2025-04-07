def nqueens(n):
    cols = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [([0] * n) for i in range(n)]

    def backtrack(r):
        if r == n:
            res.append([row[:] for row in board])
            return

        for c in range(n):
            if c in cols or (r - c) in negDiag or (r + c) in posDiag:
                continue

            board[r][c] = 1
            # update the sets
            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)

            backtrack(r + 1)

            # undo changes for next interation
            board[r][c] = 0
            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)

    backtrack(0)
    return res


n = int(input())
res = nqueens(n)

for board in res:
    for row in board:
        print(*row)
    print("----") 