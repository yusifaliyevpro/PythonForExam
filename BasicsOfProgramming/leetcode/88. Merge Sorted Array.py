# 88. Merge Sorted Array

nums1 = input("Enter the list (with space): ")
nums1 = list(map(int, nums1.split()))

nums2 = input("Enter the list (with space): ")
nums2 = list(map(int, nums2.split()))
m = int(input("Enter number: "))
n = int(input("Enter number: "))

for i in range(m, m + n):
    nums1[i] = nums2[i - m]
nums1.sort()

print(nums1)
