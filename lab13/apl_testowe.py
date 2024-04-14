import numpy as np

def string_compare(P, T, i=None, j=None):
    if i == None:
        i = len(P)-1
    if j==None:
        j = len(T)-1
    if (i==0):
        return j
    
    if (j==0):
        return i
    
    zamian = string_compare(P, T, i-1, j-1) + (P[i]!=T[j])
    wstawien = string_compare(P, T, i, j-1) + 1
    usuniec = string_compare(P, T, i-1, j) + 1

    najniszy_koszt = min(zamian, wstawien, usuniec)
    
    return najniszy_koszt


def PD(P, T, path = False):
    i = 0
    j = 0
    D = np.zeros((len(P), len(T)))
    parent = [['X'] * (len(T)) for _ in range(len(P))]

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
            substitution = D[i - 1][j - 1] + (P[i] != T[j])

            D[i][j] = min(substitution, insertion, deletion)
            if D[i][j] == substitution and P[i] != T[j]:
                parent[i][j] = "S"
            elif D[i][j] == substitution:
                parent[i][j] = "M"
            elif D[i][j] == deletion:
                parent[i][j] = "D"
            elif D[i][j] == insertion:
                parent[i][j] = "I"

    if not path:
        return D[len(P) - 1][len(T) - 1]
    
    ans = str()
    i = len(P) - 1
    j = len(T) - 1
    while len(ans) < len(P):
        ans += str(parent[i][j]) if parent[i][j] != "X" else str("D")
        if parent[i][j] == "M" or parent[i][j] == "S":
            i -= 1
            j -= 1
        elif parent[i][j] == "I":
            j -= 1
        elif parent[i][j] == "D":
            i -= 1

    return ans[::-1]



def dopasowanie(P, T):
    parent = [["X"] * len(T) for x in range((len(P)))]
    D = [[0] * len(T) for x in range((len(P)))]
    for x in range(len(P)):
        D[x][0] = x


    for i in range(1, len(P)):
        for j in range(1, len(T)):
            deletion = D[i - 1][j] + 1
            insertion = D[i][j - 1] + 1
            substitution = D[i - 1][j - 1] + (P[i] != T[j])

            D[i][j] = min(substitution, insertion, deletion)
            if D[i][j] == substitution and P[i] != T[j]:
                parent[i][j] = "S"
            elif D[i][j] == substitution:
                parent[i][j] = "M"
            elif D[i][j] == deletion:
                parent[i][j] = "D"
            elif D[i][j] == insertion:
                parent[i][j] = "I"

    ans = None
    i = len(P) - 1
    for j in range(len(P) - 1, len(T)):
        if ans is None or D[i][ans] > D[i][j]:
            ans = j

    return ans - len(P) + 1

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


if __name__ == '__main__':
#rekurencja
    P = ' kot'
    T = ' pies'
    print(string_compare(P, T))
#PD
    P = 'kot'
    T = 'pies'
    min_cost = PD(P, T)
    print(min_cost)
#PD odtwarcie ścieżki
    P = ' thou shalt not'
    T = ' you should not'
    min_cost = PD(P, T, path = True)
    print( min_cost)
#dopasowanie
    P = ' ban'
    T = ' mokeyssbanana'
    print(dopasowanie(P, T))

#najdlusza sekwencja
    P = ' democrat'
    T = ' republican'
    print(najdlusza_sekwencja(P, T))
#najdlusza podsekwencja monotoniczna
    T = ' 243517698'
    P = ' ' + sorting(T)
    longest_subsequence = najdlusza_sekwencja(P, T)
    print(longest_subsequence)