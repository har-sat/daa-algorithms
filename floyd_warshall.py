# n is the no of vertices
INF = 999


def floyd_warshall(n, graph):
    dp = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] != INF and dp[k][i] == INF:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(*floyd_warshall(n, graph))