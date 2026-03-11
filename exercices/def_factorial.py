def factorial(num, show=False):
    import time
    

    num = int(num)
    fact = int(num)
    while num >= 1:
        if show == True:
            fact*=num-1
            time.sleep(0.5)
            print(f'{num}x', end='')
            num-=1
            if num == 1 :
                time.sleep(0.5)
                print(f'1 = {fact}')
                break
        else:
            fact*=num-1
            num-=1
            print (num)
    return fact
#factorial()
print(factorial(6, True))