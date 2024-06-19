def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # empty string -> empty pattern
    dp[0][0] = True

    # patterns like a*, a*b*, a*b*c* etc.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # zero occurrences of the character before *
                dp[i][j] = dp[i][j - 2]
                # one or more occurrences of the character before *
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]


# use case
s = "aab"
p = "c*a*b"
print(isMatch(s, p))
