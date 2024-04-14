import time

def naive_method(text, pattern):
    occur = 0
    compar = 0
    m = len(text)
    n = len(pattern)
    i = 0
    while i <= m - n:
        j = 0
        while j < n and text[i+j] == pattern[j]:
            compar += 1
            j += 1

        if j == n:
            occur += 1

        i += 1

    return occur, compar

with open("lotr.txt", encoding='utf-8') as f:
    text = f.read().lower()

pattern = "time."

t_start = time.perf_counter()
occur, compar = naive_method(text, pattern)
t_stop = time.perf_counter()

print(f'{occur}; {compar}')


#metoda Rabina_Karpa
d = 256
q = 101

def hash(word, N):
    hw = 0
    for i in range(N):
        hw = (hw*d+ord(word[i]))%q
    return hw

def rolling_hash(S, hS, m, N, h):
    return ((d * hS - ord(S[m]) * h) + ord(S[m + N])) % q

def rabin_karp(S, W):
    M = len(S)
    N = len(W)
    hW = hash(W, N)
    compar = 0
    matches = 0
    collisions = 0
    h = 1
    for i in range(N-1):
        h = (h * d) % q

    for m in range(M-N+1):
        hS = hash(S[m:m+N], N)  
        if hS == hW:
            if S[m:m+N] == W:
                matches += 1
            compar += 1
        elif m < M-N:
            hS = rolling_hash(S, hS, m, N, h)
            if hS < 0:
                hS += q
            compar += 1
            if hS == hW:
                collisions += 1

    return matches, compar, collisions

t_start_2 = time.perf_counter()
matches2, comparisons2, collisions2 = rabin_karp(text, pattern)
t_stop_2 = time.perf_counter()

print(f'{matches2}; {comparisons2}; {collisions2}')

#metoda Knutha_Morrisa_Pratta

def table_T(W):
    pos = 1
    cnd = 0
    T = [-1] * (len(W) + 1)
    while pos<len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd 
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T
 

def kmp_search(text, pattern):
    T = table_T(pattern)
    P = 0
    nP = 0
    m = 0
    i = 0

    while m < len(text):
        if pattern[i] == text[m]:
            m += 1
            i += 1
            if i == len(pattern):
                P = m - i
                nP += 1
                i = T[i]
        else:
            if i>0:
                i = T[i]
            else:
                m += 1
                i += 1
    return P, nP, T

t_start_3 = time.perf_counter()
comparisons3, matches3, table = kmp_search(text, pattern)
t_stop_3 = time.perf_counter()

print(f'{matches3}; { comparisons3}; {table}')