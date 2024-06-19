def isMatch(s: str, p: str) -> bool:
    memo = {}

    def reg(i, j):
        # sub-problem already solved -> use memoization
        if (i, j) in memo:
            return memo[(i, j)]
        # if end of pattern -> check if end of input string
        if j == len(p):
            return i == len(s)
        # check if the current characters of p and s matches
        first_match = (i < len(s) and (p[j] == s[i] or p[j] == '.'))
        # check if * is present
        if j + 1 < len(p) and p[j + 1] == '*':
            # zero or multiple occurences of the character p[j] -> handle both cases
            memo[(i, j)] = (reg(i, j + 2) or first_match and reg(i + 1, j))
        else:
            memo[(i, j)] = first_match and reg(i + 1, j + 1)

        return memo[(i, j)]
    # start matching
    return reg(0, 0)


# use case
s = "aab"
p = "c*a*b"
print(isMatch(s, p))
