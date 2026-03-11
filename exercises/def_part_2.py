'''def vote(birth_year=0):
    from datetime import date


    analysis = int(date.today().year - birth_year)
    
    print
    if analysis > 16 and analysis < 65:
        return(f'This people is Mandatory and have: {analysis} years.')
    elif analysis >= 65:
        return(f'This people is Optional and have: {analysis} years.')
    else:
        return(f'This people is Denied and have: {analysis} years.')

year = vote(int(input('Enter year of birth: ')))
print(year)'''

class Solution:
    def isPalindrome(self, x):

        x = str(x)
        if x == x[::-1]:
            return(True)
        else:
            return(False)

        
x = 121
print(Solution().isPalindrome(x))

def exclusive_int(n):
    """
    docstring
    """ 
    try:
        n = int(n)
        print(f'{n} is a INT value.')
    except:
        print(f'Error {n} is not int!')
        while type(n) != type(int()):
            try:
                n = input('Enter whit a number: ') 
                n = int(n)
                print(f'Ok {n} is a INT number!')
            except:
                print(f'Error {n} is not int!')
                
    return n


num = input('Enter whit a number: ')    
num_plus = exclusive_int(num)+1
print(num_plus)