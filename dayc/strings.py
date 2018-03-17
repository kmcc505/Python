#uppercase a string
mystring = 'i am the Senate'
print(mystring.upper())

#capitalize a string
print(mystring.capitalize())

#reverse a string
def reverse (mystring):
    str = ''
    for i in mystring:
        str = i + str
    return str
print(reverse(mystring))

#convert string text to Leetspeak in all caps tho
convertme = 'Have you ever heard the story of Darth Plaguies the Wise? I thought not. It\'s not a story the jedi would tell you.'
convertme = convertme.upper()
convertme = convertme.replace ('A','4')
convertme = convertme.replace ('E','3')
convertme = convertme.replace ('G','6')
convertme = convertme.replace ('I','1')
convertme = convertme.replace ('O','0')
convertme = convertme.replace ('T','7')
print(convertme)

#Print any word with long vowels with long vowels to length of 5
enterword = 'cheese'
enterword = enterword.replace('aa', 'aaaaa')
enterword = enterword.replace('ee', 'eeeee')
enterword = enterword.replace('ii', 'iiiii')
enterword = enterword.replace('oo', 'ooooo')
enterword = enterword.replace('uu', 'uuuuu')
print(enterword)

#Cipher decode
cipher = 'lbh zhfg hayrnea jung lbh unir yrnearq'
import codecs
cipher = codecs.decode('lbh zhfg hayrnea jung lbh unir yrnearq', 'rot13')
print(cipher)
