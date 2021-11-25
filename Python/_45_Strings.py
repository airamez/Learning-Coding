phrase = "I Love Computer Programming"

print("#0 Split")
words = phrase.split()
print(words)
words = "I_Love_Computer_Programming"
words = words.split('_')
print(words)
words = "I<->Love<->Computer<->Programming"
words = words.split('<->')
print(words)


print("\n#1 Substring/Slicing")
print(phrase[0:1])
print(phrase[2:6])
print(phrase[7:15])
print(phrase[7:])
print(phrase[:15])

print("\n#2 Lower/Upper Case")
phrase_lower = phrase.lower()
print(phrase_lower)
phrase_upper = phrase.upper()
print(phrase_upper)

print("\n#3 Testing Lower/Upper Case")
print(phrase_lower.islower())
print(phrase_lower.isupper())
print(phrase_upper.islower())
print(phrase_upper.isupper())

print("\n#4 Capitalize")
phrase_capitalized = phrase_lower.capitalize()
print(phrase_capitalized)

print("\n#5 Title")
phrase_titled = phrase_upper.title()
print(phrase_titled)

print("\n#6 Test Title")
print(phrase_titled.istitle())
print(phrase_lower.istitle())
print(phrase_upper.istitle())

print("\n#7 Swap case")
print(phrase_lower, "=>", phrase_lower.swapcase())
print(phrase_upper, "=>", phrase_upper.swapcase())
print(phrase_titled, "=>", phrase_titled.swapcase())

print("\n#8 Strip")
not_stripped = "    coding               "
print("Not Stripped =", f"'{not_stripped}'")
stripped = not_stripped.strip()
print('Stripped =', stripped)
not_stripped = "XXXXXXcodingXXX"
stripped = not_stripped.strip("X")
print('not_stripped =', not_stripped)
print('stripped =', stripped)
not_stripped = "XYZXYZcodingXYZXYZ"
stripped = not_stripped.strip("XYZ")
print(not_stripped, ' = ', stripped)

print("\n#9 Left/Right Strip")
not_stripped = "    coding               "
print(f"'{not_stripped}'")
leftStripped = not_stripped.lstrip()
print(f"Left Stripped = '{leftStripped}'")
rightStripped = not_stripped.rstrip()
print(f"Right Stripped = '{rightStripped}'")

print("\n#10 Center")
base = "center"
centralized = base.center(50, "_")
print(centralized)

print("\n#11 Left Justify")
left_justified = base.ljust(30, "_")
print(left_justified)

print("\n#12 Right Justify")
right_justified = base.rjust(30, "_")
print(right_justified)

print("\n#13 Replace")
print(phrase)
new_phrase = phrase.replace("Love", "Enjoy")
print(new_phrase)
new_phrase = phrase.replace("m", "")
print(new_phrase)

print("\n#14 ZFill")
s = "7.45"
print(s.zfill(10))
s = "+7.45"
print(s.zfill(10))
s = "-7.45"
print(s.zfill(10))

print("\n#15 Join")
namesList = list()
namesList.append('Jose')
namesList.append('Leila')
namesList.append('Artur')
namesStr = ','.join(namesList)
print(namesList)
print(namesStr)

print("\n#16 Sorting")
s = "lpoimjknbgtrsfdvcxaz"
print(type(s), s)
s = sorted(s)
print(type(s), s)
s = "".join(s)
print(type(s), s)
s = "".join(sorted(s, reverse=True))
print(type(s), s)
