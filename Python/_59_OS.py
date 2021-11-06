import os

print('os.name: ', os.name)
currentDir = os.getcwd()
print('currentDir: ', currentDir)

print('Folder Content')
for entry in os.listdir():
    print(entry)

folderName = 'os_demo'

if os.path.isdir(folderName):  # Check if the folder exists
    print(f'Folder already exists: {folderName}')
else:
    print(f'creating a folder called "{folderName}"')
    os.mkdir(folderName)  # Creates a folder

print(f'Changing to the {folderName} folder')
os.chdir(folderName)  # Changing to a folder

print("current dir: ", os.getcwd())

print("Writing text to a file")
file = open('log.txt', 'w+')  # Open a file to write
i = 1
print('Type lines for a text file. Empty line to finish!')
while (True):
    line = input(f'Line {i} = ')
    if not line:
        break
    file.write(f'{i} {line}\n')  # Writes to the text file
    i += 1
file.close()  # closed the file
# ATTENTION: try... catch is required for a robust program

print("Reading from a text file")

file = open('log.txt', 'r')  # Opens a file to read
for line in file.readlines():  # Reads lines from a text file
    print(line, end='')
file.close()

file = open('log.txt', 'r')
content = file.read()  # Reads the file content
print(content)
file.close()
