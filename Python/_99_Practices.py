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

# https://leetcode.com/problems/evaluate-reverse-polish-notation/
def evalRPN(self, tokens: List[str]) -> int:
    values = list()
    for token in tokens:
        if token not in '+-*/':
            values.append(int(token))
        else:
            new_value = None
            right_value = values.pop()
            left_value = values.pop()
            if token == '+':
                new_value = left_value + right_value
            elif token == '-':
                new_value =  left_value - right_value
            elif token == '*':
                new_value = left_value * right_value
            else:
                new_value = int(left_value / right_value)
            values.append(new_value)
    return values[0]

# https://leetcode.com/problems/merge-intervals/submissions/
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals or len(intervals) == 1:
        return intervals
    result = []
    intervals.sort()
    result.append(intervals[0])
    for start, end in intervals[1:]:
        current = result[-1]
        if (start <= current[1]):
            current[1] = max(end, current[1])
        else:
            result.append([start, end])
    return result

# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        left = head
        right = head.next
        while left and right:
            left.val, right.val = right.val, left.val
            if not right.next:
                break
            left = right.next
            if left and left.next:
                right = left.next
            else:
                break
        return head

# https://leetcode.com/problems/string-compression
def compress(self, chars: List[str]) -> int:
    if len(chars) == 1:
        return 1
    current_char = chars[0]
    current_count = 1
    output = []
    for c in chars[1:]:
        if c == current_char:
            current_count += 1
        else:
            output.append([current_char, current_count])
            current_char = c
            current_count = 1
    output.append([current_char, current_count])
    i = 0
    for entry in output:
        chars[i] = entry[0]
        i += 1
        if entry[1] > 1:
            count = str(entry[1])
            for c in count:
                chars[i] = c
                i += 1
    return i

# https://leetcode.com/problems/binary-tree-inorder-traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    inOrder = []
    self.__inorderTraversal(root, inOrder)
    return inOrder
def __inorderTraversal (self, node: Optional[TreeNode], inOrder: list[TreeNode]):
    if node:
        self.__inorderTraversal(node.left, inOrder)
        inOrder.append(node.val)
        self.__inorderTraversal(node.right, inOrder)

# https://leetcode.com/problems/longest-substring-without-repeating-characters
def lengthOfLongestSubstring(self, s: str) -> int:
    if s == None or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    left = 0
    right = 1
    my_set = set()
    my_set.add(s[0])
    max_len = 1
    while (right < len(s)):
        if right < len(s) and s[right] not in my_set:
            my_set.add(s[right])
            right += 1
            max_len = max(max_len, len(my_set))
        else:
            while s[left] != s[right]:
                my_set.remove(s[left])
                left += 1
            left += 1
            right += 1
    return max_len