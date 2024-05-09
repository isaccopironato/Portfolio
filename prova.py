def topKFrequent(nums, k):
    unique = []
    my_dic = {}
    output = [] 
    for i in nums: 
        if i not in unique:
            unique.append(i)
            my_dic[i] = nums.count(i)

    for i in range(0,k):
        num = 0
        amount = 0
        for j in unique:
            if my_dic[j] > amount:
                amount = my_dic[j]
                num = j
        output.append(num)
        unique.remove(num)
        my_dic.pop(num)
    return output

nums = [1,1,1,2,2,3,3,3,3]
k = 2

print(topKFrequent(nums, k))
