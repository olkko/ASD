def table_T(W):
    pos = 1
    cnd = 0
    T = []
    T[0] = -1
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
 

def kmp_search(text, pattern):
    T = table_T(pattern)
    P = 0
    nP = 0
    for m in range(text):
        for i in range(pattern):
            while m < len(text):
                if pattern[i] == text[m]:
                    m +=1
                    i+=1
                    if i == len(W):
                        P = m-i
                        nP = nP+1
                        i = T[i]
                    else:
                        i = T[i]
                        if i<0:
                            m +=1
                            i+=1
    return P, nP