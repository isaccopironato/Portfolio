
def factorial_recursively(num: int)->int:
    if num == 0 or num == 1:
        print(num)
        return 1 
    else: 
        print(num)
        return num * factorial_recursively(num-1)

def factorial_iterativly(num: int)->int:
    output = 1
    for i in range(1, num+1):
        output *= i

    return output

print(factorial_iterativly(6))
print(factorial_recursively(6))