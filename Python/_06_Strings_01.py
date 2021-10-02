# String literals are defined by " or '
first_name = "Jose"
last_name = 'Santos'
print("Fullname:", first_name, last_name)

#
# Escape characters
# \t = Tat
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