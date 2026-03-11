first_t = int(input('First Term: '))
reason = int(input('Reason: '))
term = int(input('Term: '))
first = {}
r = []
op = 0
#for n in range(first_t,reason,first_t+1):
if first_t >= reason:
    print('Error, First Term plus Reason!')
    exit

while first_t <= reason:
    first_t += 1
    op = int(first_t + term)
    r = int(op - first_t)
    ns = str(first_t)
    first[ns] = (op,r)
    if first_t >= reason:
       ce = int(input('\nContinue - 1\nEnd - 2\n...'))
       if ce == 1:
           reason += int(input('Reason: '))
           while first_t >= reason:
                if first_t >= reason:
                    break
                else:
                    first_t += 1
                    op = int(first_t + term)
                    r = int(op - first_t)
                    ns = str(first_t)
                    first[ns] = (op,r)
       else:
          break
            
print(f'\n{first}')
