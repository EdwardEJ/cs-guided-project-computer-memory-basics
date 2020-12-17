def removeAdjacent(s):
    nd = ''             # O(1)
    for i in s:         # O(n)
        if len(nd):     # O()    
            if nd[-1] != i:
                nd += i
        else:
            nd += i
    return nd

