nums = []
for n in range(5):
    n1 = int(input(f'Type the {n}: '))
    if n == 0 or n1 > nums[len(nums)-1]:
        nums.append(n1)
    else:
        pos = 0
        while pos < len(nums):
            if n1 <= nums[pos]:
                nums.insert(pos, n1)
                break
            pos += 1
print(nums)