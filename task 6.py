def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

def get_operations(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    i, j = m, n
    operations = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            operations.append(('No change', s1[i - 1]))
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(('Substitute', s1[i - 1], s2[j - 1]))
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            operations.append(('Delete', s1[i - 1]))
            i -= 1
        elif dp[i][j] == dp[i][j - 1] + 1:
            operations.append(('Insert', s2[j - 1]))
            j -= 1
    while i > 0:
        operations.append(('Delete', s1[i - 1]))
        i -= 1
    while j > 0:
        operations.append(('Insert', s2[j - 1]))
        j -= 1
    operations.reverse()
    return operations

s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
ed = edit_distance(s1, s2)
ops = get_operations(s1, s2)
print(f'Minimum number of operations: {ed}')
print('Operations:')
for op in ops:
    print(op)