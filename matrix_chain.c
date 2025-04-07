// You are using GCC
#include <stdio.h>
#include <limits.h>

// Function to print optimal parenthesization
void printOptimalParenthesis(int i, int j, int n, int *bracket, int *name)
{
    if (i == j)
    {
        printf("M%d", (*name)++);
        return;
    }
    printf("(");
    printOptimalParenthesis(i, *((bracket + i * n) + j), n, bracket, name);

    printOptimalParenthesis(*((bracket + i * n) + j) + 1, j, n, bracket, name);
    printf(")");
}

// Function to compute the matrix chain order
void matrixChainOrder(int p[], int n)
{
    int dp[n][n];
    int bracket[n][n];
    // Initialize the diagonal elements to zero
    for (int i = 1; i < n; i++)
        dp[i][i] = 0;

    // Fill dp array using bottom-up approach
    for (int chain_len = 2; chain_len < n; chain_len++)
    {
        for (int i = 1; i < n - chain_len + 1; i++)
        {
            int j = i + chain_len - 1;

            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++)
            {
                int cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (cost < dp[i][j])
                {
                    dp[i][j] = cost;
                    bracket[i][j] = k;
                }
            }
        }
    }

    printf("%d\n", dp[1][n - 1]);
    int name = 1; // Start with M1
    printOptimalParenthesis(1, n - 1, n, (int *)bracket, &name);
    printf("\n");
}
int main()
{
    int n;
    scanf("%d", &n);
    int p[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &p[i]);
    }
    matrixChainOrder(p, n);
    return 0;
}