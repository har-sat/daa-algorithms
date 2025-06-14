def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    if m > n:
        return "-1"

    positions = []  # to store output
    hash = {}
    num = 0
    for c in text:
        if c not in hash:
            hash[c] = num
            num += 1

    # hash the pattern
    p_hash = 0
    t_hash = 0
    for i in range(m):
        p_hash += hash[pattern[i]] * (10 ** (m - i - 1))
        t_hash += hash[text[i]] * (10 ** (m - i - 1))

    if t_hash == p_hash and text[:m] == pattern:
        positions.append(0)

    #find all the other patterns
    for i in range(1, n - m + 1):
        leaving = hash[text[i - 1]]
        coming = hash[text[i + m - 1]]
        t_hash = 10*(t_hash - leaving * (10 ** (m - 1))) + coming

        print("window hash for ", text[i : m + i], ": ", t_hash)
        if t_hash == p_hash and text[i : m + i] == pattern:
            positions.append(i)

    return " ".join(map(str, positions)) if positions else "-1"


print(rabin_karp("malayalam", "al"))
