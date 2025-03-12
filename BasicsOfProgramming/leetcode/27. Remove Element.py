# 27. Remove Element
nums = input("Enter the list (with space): ")
nums = list(map(int, nums.split()))
val = int(input("Enter number: "))
t = nums.count(val)
while nums.count(val) != 0:
    nums.remove(val)

nums += t * ["_"]
print(f"{len(nums) - t}, {nums}")
