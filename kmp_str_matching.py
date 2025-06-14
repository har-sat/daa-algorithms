def fill_lps(s: str):
    lps = [0] * len(s)
    j, i = 0, 1

    while i < len(s):
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j == 0:
            lps[i] = 0
            i += 1
        else:
            j = lps[j - 1]

    print(*lps)
    return lps


def kmp(text: str, pattern: str):
    n, m = len(text), len(pattern)
    if m > n:
        return "-1"

    lps = fill_lps(pattern)
    i, j = 0, 0

    res = []
    while i < n:
        if j < m and text[i] == pattern[j]:
            j += 1
            i += 1

            if not j < m:
                res.append(i - m)
        elif j == 0:
            i += 1
        else:
            j = lps[j - 1]

    return " ".join(map(str, res)) if res else "-1"


print(kmp(input(), input()))
