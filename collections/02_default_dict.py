#!/usr/bin/python3

from collections import defaultdict

def check_indices():
    pass 

if __name__ == "__main__":
    indice = 1
    mydict_a : defaultdict = defaultdict(list)
    mylist_b = []
    n, m = map(int, input().split())
    while n:
        x = input()
        mydict_a[x].append(indice)
        indice += 1
        n -= 1
    while m:
        x = input()
        mylist_b.append(x)
        m -= 1
    
    for item in mylist_b:
        if len(mydict_a[item]) == 0:
            print(-1)
        else:
            for idx in mydict_a[item]:
                print(idx,end=" ")
            print()