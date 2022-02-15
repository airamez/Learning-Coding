from itertools import permutations

s = 'abc'
'''
for perm in permutations(s):
  p = ''.join(perm)
  print(p)
'''

dic = dict()
for i in range(len(s)):
  if i == 0:
    dic[0] = list(s[i])
  else:
    for pre in dic[i - 1]:
      for indice in range(len(pre), -1, -1):
        newStr = list(pre)
        if i not in dic:
          dic[i] = list()
        newStr.insert(indice, s[i])
        dic[i].append(''.join(newStr))

print(dic[len(s) - 1])


