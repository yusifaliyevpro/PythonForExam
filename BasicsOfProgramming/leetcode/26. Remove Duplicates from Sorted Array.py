# 26. Remove Duplicates from Sorted Array

nums = input("Enter the list (with space): ")
nums = list(reversed(list(map(int, nums.split()))))
t = 0
for i in nums:
    if nums.count(i) != 1:
        t += 1
        nums.remove(i)

nums = list(reversed(nums)) + t * ["_"]
print(f"{len(nums) - t}, {nums}")
