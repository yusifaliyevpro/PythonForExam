# 35. Search Insert Position

nums = input("Enter the list (with space): ")
nums = list(map(int, nums.split()))

target = int(input("Enter number: "))

if nums.count(target) != 0:
    print(nums.index(target))
else:
    while True:
        target -= 1
        a = nums.index(target)
        if a != -1:
            print(a + 1)
            break
