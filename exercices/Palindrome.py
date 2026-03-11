phrase = input('Type one phrase: ')
phrase = phrase.replace(' ','')
inverted = ''.join(reversed(phrase))
notspace = inverted.replace(' ','')
if phrase == notspace:
    print('Palindrome!')
    print(notspace)

else:
    print('Not Palindrome.')
    print(notspace)