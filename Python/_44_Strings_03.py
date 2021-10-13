phrase = "I Love Computer Programming"

print("# In and Not In")
print("Love" in phrase)
print("Love" not in phrase)
print("Python" in phrase)
print("Python" not in phrase)

print("# Find: Returns the index")
print(phrase)
print(phrase.find("Programming"))
print(phrase.find("Coding"))
print(phrase.find("m", 0))  # Find with start position
print(phrase.find("m", 10))
print(phrase.find("Love", 0, 10))  # Find with start and end position
print(phrase.find("Love", 20, 25))

print("# Right Find")
print(phrase.rfind("m"))
print(phrase.rfind("ming"))
print(phrase.rfind("m", 0, 10))
print(phrase.rfind("Python"))

print("# Starts with")
print(phrase)
print(phrase.startswith("I"))
print(phrase.startswith("B"))
print(phrase.startswith("I Love"))
print(phrase.startswith("Love"))

print("# Ends with")
print(phrase)
print(phrase.endswith("g"))
print(phrase.endswith("k"))
print(phrase.endswith("Programming"))
print(phrase.endswith("Computer"))

print("# Count")
s = "aaabbb aaabbb"
print(s)
print("a =", s.count("a"))
print("b =", s.count("b"))
print("c =", s.count("c"))
print("aaa =", s.count("aaa"))
print("aaabbb =", s.count("aaabbb"))
print("abbb a =", s.count("abbb a"))

print("# replace")
s = 'I love COBOL, because COBOL is so cool and everybody loves COBOL'
print(s)
s = s.replace('COBOL', 'Python')  # Returns a new string
print(s)
