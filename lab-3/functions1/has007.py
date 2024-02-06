nums = [1, 0, 2, 0, 3, 7, 4]
nums1 = [0, 0, 7]
nums2 = [1, 7, 2, 0, 3, 0, 4]

def has007(nums):
    nums = [x for x in nums if x == 0 or x == 7]
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

print(has007(nums))
print(has007(nums1))
print(has007(nums2))