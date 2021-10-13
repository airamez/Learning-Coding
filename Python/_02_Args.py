import sys  # Importing a Python library

#execute: python _02_Args.py Parameter_1 Parameter_2 'Parameter 3 with spaces'
print('Argment count: ', len(sys.argv))
print('Arguments array: ', sys.argv)
print('Program Name: ', sys.argv[0])
print('Argment 1: ', sys.argv[1])
print('Argment 2: ', sys.argv[2])
print('Argment 3: ', sys.argv[3])
