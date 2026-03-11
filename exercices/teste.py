nums = [2,7,11,15,18]
nums_ok = []
target = int(input('Target: '))
n = []
limit = (len(nums_ok))

for num in nums:
    if num < target:
       nums_ok.append(num)
#print(f'Aqui1{nums_ok}')
        
for num in nums_ok:
    #print(f'Aqui2: {num}')
    if num + nums_ok[limit] == target:
        n.append(num)
        n.append(nums_ok[limit])
    if limit == None:
        break

if not n:
    print(f'Any Result.')
else:
    n = list(set(n))
    print(f'The result betwing SUM {n}: {target}')
