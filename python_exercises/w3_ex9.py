
# Write a Python program to find a list of integers containing exactly four distinct values, 
# such that no integer repeats twice consecutively among the first twenty entries.
# Input:
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False

def func(test1):
    print(test1)
    count = 0

    for i in test1[1:]: 
        if i == test1[count]:
            return False
        if count == 18: 
            return True
        if (count+1)% 3 == 0:
            if test1[count+1-3] == i: 
                return False
        count += 1
    return True

if __name__ == "__main__": 
    test1 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    test2 = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
    test3 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    test4 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 4]
    test5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(func(test1))
    print(func(test2))
    print(func(test3))
    print(func(test4))
    print(func(test5))
