'''
You have a test string .
Your task is to write a regex that will match  with the following conditions:

 must be of length 6.
First character should not be a digit .
Second character should not be a lowercase vowel.
Third character should not be b, c, D or F.
Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
Fifth character should not be a uppercase vowel .
Sixth character should not be a . or , symbol.
'''

import re


inpstr = "h4CkR"
inpstr = "a0$?ZW"
inpstr = 'think?'

#r1 = "^[^0-9][^aeiou][^bcDF][^\r\n\t\f][^AEIOU][^\.,]"
r1 = "^[A-Za-z]{40}[13579|\s]{5}$"
print(inpstr)
print("\n Regex findall ",re.findall(r1, inpstr))
