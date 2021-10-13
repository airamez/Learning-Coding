import os, shutil


print('os.name: ', os.name)
currentDir = os.getcwd()
print('currentDir: ', currentDir)

print('Folder Content')
for entry in os.listdir():
  print(entry)

dirName = 'os_demo'

if os.path.isdir(dirName): # Check if the folder exists
  print(f'Deleting the existing folder: {dirName}')
  shutil.rmtree(dirName) # Deletes a folder and all its contents
  print('Folder deleted')
print(f'creating a folder called "{dirName}"')
os.mkdir(dirName) # Creates a folder

print(f'Changing to the {dirName} folder')
os.chdir(dirName) # Chancing to a folder

print("current dir: ", os.getcwd())


print('Returning to the parent folder')
os.chdir('..')
print("current dir: ", os.getcwd())

print("Writing text to a file")
file = open('log.txt', 'w+')

i = 1
while (True):
  line = input(f'Line {i} = ')
  if not line:
    break
  file.write(f'{i} {line}\n')
  i += 1
file.close()