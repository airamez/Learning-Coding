'''
In Python, Strings are arrays of bytes representing Unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
String literals are defined by " or '
String in Python is an immutable collection of Unicode characters
UNICODE: https://en.wikipedia.org/wiki/Unicode
         https://unicode-table.com/en/#control-character
'''

first_name = "Jose"
last_name = 'Santos'
print("Fullname:", first_name, last_name)

#
# Escape characters
# \t = Tab
# \n = New line
# \' = Single quote
# \" = Double Quotes
# \\ = Backslash
#
phrase = 'The world\tis\tbeautifil'
print("phrase:", phrase)

text = "This is the firstline\nThis is the second line\nThis is the third line"
print("Multilines", text)

phrase = "This isn't wrong"
print("phrase:", phrase)

phrase = 'This isn\'t wrong'
print("phrase:", phrase)

phrase = 'Using a \\ inside string'
print("phrase:", phrase)

course = 'Learning "Python"'
print("course:", course)

# Multiple lines string constant
family = "Family: " \
"José Santos; " \
"Leila Rodrigues; " \
"Artur Rodrigues"
print("Family: ", family)

#Using r before the string makes python ignore the escape character
dir = r"c:\root\name_folder\thefinal_folder"
print(dir)
