"""Two sum - variant
inputs:
list = [1, 4, 6, 9]
target = 5
outputs:
[0, 1] since 1+4 =5

def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map.keys():
            return [hash_map[diff], i]
        hash_map[num] = i

list1 = [3, 6, 4, 2]
tar = 7
print(two_sum(list1, tar))


#number of subarrys whose sum is k
nums = [1, 1, 1, 2]
k = 2

def sub_array(nums, k):
    print(nums, k)
    prefix = {0: 1}
    print(prefix)
    curr = 0
    count = 0
    for num in nums:
        print(num)
        curr += num
        print(curr)
        if curr - k in prefix:
            count += prefix[curr-k]
            print(count)
        prefix[curr] = prefix.get(curr, 0) + 1
        print(prefix)
    return count


print(sub_array(nums, k))
def two_sum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in mp :
            return [mp[diff], i]
        mp[num] = i
    return

"""
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(1) + factorial(4) + factorial(5))
num = 145
temp = num
new_num = 0
while num > 0:
    find_fact = num % 10
    print(find_fact)
    new_num += factorial(find_fact)
    print(new_num)
    num = num // 10
print(new_num)
print(num)
if new_num is temp:
    print("Strong")
else:
    print("Not strong")