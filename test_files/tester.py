
def func(nums, val):
    k = 0
    while val in nums: 
        nums.remove(val)
        k += 1
    return k, nums


nums = [0,1,2,2,3,0,4,2]
val = 2
print(nums, val)
print(func(nums,val))

nums = [0,1,2,2,3,0,4,2]
val = 3
print(nums, val)
print(func(nums,val))

def my_func(haystack, needle):
    l = list(haystack)
    for i in range(len(l) - len(needle) + 1): 
        if l[i] == needle[0]:
            if "".join(l[i: i + len(needle)]) == needle:
                return i
    return -1

i = "sad"
b = "sadbutsad"
print(my_func(b, i))