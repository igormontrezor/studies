nums = []
n = sm = 0
while n != 999:
    n = int(input('Insert the number, if number is 999 the program is stoped: '))
    if n == 999:
        break
    else:
        nums.append(n)
        sm += n
nums.sort()
median = sm/len(nums)
hig = nums[len(nums)-1]
low = nums[0]
print(f'\nThe Lowest is: {low}\nThe Highest: {hig}\nThe Sum {len(nums)-1} values is: {sm}\nThe Median: {median}\nAll the numbers typed: {nums}')