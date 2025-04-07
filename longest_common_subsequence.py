def lcs_length_and_sequences(str1: str, str2: str):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build LCS length table using DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to find all LCS sequences
    def backtrack(i, j):
        if i == 0 or j == 0:
            return {""}
        if str1[i - 1] == str2[j - 1]:
            return {seq + str1[i - 1] for seq in backtrack(i - 1, j - 1)}
        lcs_set = set()
        if dp[i - 1][j] >= dp[i][j - 1]:
            lcs_set.update(backtrack(i - 1, j))
        if dp[i][j - 1] >= dp[i - 1][j]:
            lcs_set.update(backtrack(i, j - 1))
        return lcs_set
    
    lcs_set = backtrack(m, n)
    lcs_set = {" ".join(seq) for seq in {"".join(seq.split()) for seq in lcs_set}}  # Preserve spacing format
    
    # Output results
    for seq in sorted(lcs_set):
        print(seq)
    print(f"The length of the Longest Common Subsequence is: {dp[m][n]}")

# Read input strings
str1 = input().strip()
str2 = input().strip()

lcs_length_and_sequences(str1, str2)
