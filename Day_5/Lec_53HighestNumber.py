nums = input("Enter your numbers : ").split()
for n in range(0, len(nums)):
    nums[n] = int(nums[n])

max = 0
for score in nums:
    if score > max:
        max = score

print(f"The highest score in the class is : {max}")
