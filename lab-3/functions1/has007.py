nums = [1, 2, 3, 3, 4, 5, 5, 6, 0, 0, 7]

def has_33(nums):
    for i in range (len(nums) - 1):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False
print(has_33(nums))