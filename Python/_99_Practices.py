from typing import List, Optional

# https://leetcode.com/problems/first-bad-version/
def isBadVersion(version):
  pass

def firstBadVersion(self, n):
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            if isBadVersion(mid - 1):
                right = mid - 1
            else:
                return mid
        else:
            left = mid + 1

# https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(self, nums: List[int]) -> bool:
    s = set()
    for i in range(0, len(nums)):
        if nums[i] in s:
            return True
        s.add(nums[i])
    return False

# https://leetcode.com/problems/binary-search/
def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while (True):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        if left > right:
            return -1

# https://leetcode.com/problems/container-with-most-water/
def maxArea(self, height: List[int]) -> int:
    left = 0;
    right = len(height) - 1
    maxWater = 0
    while left < right:
        localWater = min(height[left], height[right]) * (right - left)
        maxWater = max(maxWater, localWater)
        if (height[left] < height[right]):
            left += 1
        else:
            right -= 1
    return maxWater

# https://leetcode.com/problems/group-anagrams/
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagramsDic = dict()
    for s in strs:
        sSorted = str(sorted(s))
        if sSorted not in anagramsDic.keys():
            anagramsDic[sSorted] = list()
        anagramsDic[sSorted].append(s)
    result = list()
    for values in anagramsDic.values():
        result.append(list(values))
    return result

# https://leetcode.com/problems/richest-customer-wealth/
def maximumWealth(self, accounts: List[List[int]]) -> int:
    maxWealth = 0
    for a in accounts:
        sum_accounts = sum(a)
        maxWealth = max(maxWealth, sum_accounts)
    return maxWealth

# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = None
    last = None
    if not l1:
        return l2
    if not l2:
        return l1
    while l1 and l2:
        if l1.val < l2.val:
            newNode = ListNode(l1.val)
            l1 = l1.next
        else:
            newNode = ListNode(l2.val)
            l2 = l2.next
        if not head:
            head = newNode
            last = head
        else:
            last.next = newNode
            last = newNode
    while l1:
        last.next = ListNode(l1.val)
        l1 = l1.next
        last = last.next
    while l2:
        last.next = ListNode(l2.val)
        l2 = l2.next
        last = last.next
    return head

# https://leetcode.com/problems/merge-sorted-array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if m == 0:
        nums1.extend(nums2)
    if n == 0:
        return
    del nums1[m:]
    i1 = 0
    i2 = 0
    while i1 < len(nums1) and i2 < len(nums2):
        if nums2[i2] < nums1[i1]:
            nums1.insert(i1, nums2[i2])
            i1 += 1
            i2 += 1
        else:
            i1 += 1
    if i2 < len(nums2):
        for i in range(i2, len(nums2)):
            nums1.insert(i1 + 1, nums2[i])
            i1 += 1

# https://leetcode.com/problems/longest-common-prefix
class Solution:
  
  def get_prefix(self, s1, s2):
      i = 0;
      while i < len(s1) and i < len(s2):
          if s1[i] != s2[i]:
              break
          i += 1
      return s1[0:i]
  
  def longestCommonPrefix(self, strs: List[str]) -> str:
      if len(strs) < 1:
          return ''
      if len(strs) == 1:
          return strs[0]
      prefix = strs[0]
      for i in range(1, len(strs)):
          prefix = self.get_prefix(prefix, strs[i])
          if not prefix:
              return ''
      return prefix

'''
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
You can assume the given expression is always valid.
'''
def process (expression: list) -> float:
  values = list()
  for term in expression:
    if isinstance(term, float) or isinstance(term, int):
      values.append(term)
    else:
      newValue = None;
      value_right = values.pop()
      value_left = values.pop()
      if term == '+':
        newValue = value_left + value_right
      elif term == '-':
        newValue = value_left - value_right
      elif term == '*':
        newValue = value_left * value_right
      else:
        newValue = value_left / value_right
      values.append(newValue)
  return values[0]

print(process([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))
print(process([5, 3, '+']))

