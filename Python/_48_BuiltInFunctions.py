# https://docs.python.org/3.1/library/functions.html
print('abs(1) =', abs(1))
print('abs(-1) =', abs(-1))

# Check if all True
print('all([True, True, True]) =', all([True, True, True]))
print('all([True, True, True]) =', all([True, False, True]))

# Check if at least one is True
print('any([True, True, True]) =', any([True, True, True]))
print('any([True, True, True]) =', any([False, False, False]))

# printable representation of an object
print("ascii(['Jose', 'Leila', 'Artur'])=", ascii(['Jose', 'Leila', 'Artur']))

print('chr(65) =', chr(65))

# compile() with string source
code_str = '''
x=5
y=10
print("sum =",x+y)
'''
code = compile(code_str, 'sum.py', 'exec')
exec(code)

print('divmode(7,2) =', divmod(7, 2))

x = 1
print('eval("x + 2") =', eval("x + 2"))
