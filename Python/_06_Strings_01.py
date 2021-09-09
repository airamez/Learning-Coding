#
# Escape characters
# 
phrase = 'The world\tis\tbeautifil'
print(phrase)

text = "This is the firstline\nThis is the second line\nThis is the third line"
print(text)


dir = "c:\root\name_folder\thefinal_folder"
print(dir)

#r makes python ignore the escape character
dir = r"c:\root\name_folder\thefinal_folder"
print(dir)

phrase = "This isn't wrong"
print(phrase)

phrase = 'This isn\'t wrong'
print(phrase)

phrase = 'Using a \\ inside string'
print(phrase)

course = '''Learning '"Python"'''
print(course)

# Multiple lines string constant
family = '''Family:
'José' "Santos"
'Leila' "Rodrigues"
'Artur' "Rodrigues"'''
print(family)

family = """Family:
"José" 'Santos'
"Leila" 'Rodrigues'
"Artur" 'Rodrigues'"""
print(family)

family = "Family: " \
        "José Santos; " \
        "Leila Rodrigues; " \
        "Artur Rodrigues"
print(family)