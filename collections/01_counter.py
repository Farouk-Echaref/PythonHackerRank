#!/usr/bin/python3

from collections import Counter
from typing import List, Tuple


# sample input:
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50



if __name__ == "__main__":
    money = 0
    n_shoes = int(input())
    list_shoe_sizes = list(map(int, input().split()))
    n_customers = int(input())
    shoe_counter = Counter(list_shoe_sizes)
    while n_customers:
        shoe_number, price = map(int, input().split())
        # res = shoe_counter.get(shoe_number, None)
        check = shoe_counter[shoe_number]
        if check != 0:
            money += price
            shoe_counter[shoe_number] -= 1
        n_customers -= 1

    print(money)
    # print(list_shoe_sizes)
    # print(shoe_counter)

    
# def returnCounter(arr: List) -> Counter:
#     return Counter(arr)

# if __name__ == "__main__":
    # myList : List = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    # print(returnCounter(myList))
    # print(returnCounter(myList).items())
    # print(returnCounter(myList).keys())
