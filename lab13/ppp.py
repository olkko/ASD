import numpy as np

def najdlusza_sekwencja(P, T):
    D = np.zeros((len(P), len(T)))
    parent = [['X'] * len(T) for _ in range(len(P))]

    for row in range(len(P)):
        D[row][0] = row
        parent[row][0] = "D"

    for col in range(len(T)):
        D[0][col] = col
        parent[0][col] = "I"

    parent[0][0] = "X"

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            deletion = D[i - 1][j] + 1
            insertion = D[i][j - 1] + 1
            substitution = float('inf') if P[i] != T[j] else D[i - 1][j - 1] + (P[i] != T[j])

            D[i][j] = min(substitution, insertion, deletion)
            if D[i][j] == substitution and P[i] != T[j]:
                parent[i][j] = "S"
            elif D[i][j] == substitution:
                parent[i][j] = "M"
            elif D[i][j] == deletion:
                parent[i][j] = "D"
            elif D[i][j] == insertion:
                parent[i][j] = "I"
    
    ans = str()
    i = len(P) - 1
    j = len(T) - 1
    while i > 0 and j > 0:
        if parent[i][j] == "M" or parent[i][j] == "S":
            if T[j] != ' ':
                ans += str(T[j])
            i -= 1
            j -= 1
        elif parent[i][j] == "I":
            j -= 1
        elif parent[i][j] == "D":
            i -= 1

    return ans[::-1]
def sorting(text):
    string_list = sorted([int(x) for x in text.strip()])
    ans = "".join(str(x) for x in string_list)
    return ans


T = ' 243517698'
P = ' ' + sorting(T)
longest_subsequence = najdlusza_sekwencja(P, T)
print(longest_subsequence)