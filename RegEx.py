import re


#For a table of REs, check:
#https://www.w3resource.com/python/python-regular-expression.php



#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
def regex1(str1):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    str1 = charRe.search(str1)
    print(not bool(str1))
#regex1("ABCDEFabcdef123450")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program that matches a string that has an a followed by zero or more b's.
def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns,  text): return 'Found a match!'
    else: return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))