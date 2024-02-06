def histogram():
    nums = str(input("enter nums by space: ")).split()
    for x in nums:
        print("*" * int(x))
        
histogram()