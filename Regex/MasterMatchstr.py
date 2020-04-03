'''
Use this only for testing purposes
'''

import re


inpstr = ["h4CkR", "a0$?ZW",'think?', '2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa13 57']
#r1 = "^[^0-9][^aeiou][^bcDF][^\r\n\t\f][^AEIOU][^\.,]"
r1 = "^[A-Za-z]{40}[13579|\s]{5}$"

# DO NOT EDIT
print(inpstr)
for _ in inpstr:
    print("\n Regex findall ",re.findall(r1, _))
