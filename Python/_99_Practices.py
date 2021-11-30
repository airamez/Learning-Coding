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

# https://leetcode.com/problems/merge-intervals/
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

# https://leetcode.com/problems/swap-nodes-in-pairs/
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

# https://leetcode.com/problems/3sum
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = set()
    for i in range(len(nums) - 2):
        if (nums[i]) > 0:
            break
        # Skip duplicated
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            value = nums[i] + nums[left] + nums[right]
            if value == 0:
                entry = tuple([nums[i], nums[left], nums[right]])
                triplets.add(entry)
                left += 1
                right -= 1
            elif value < 0:
                left += 1
            else:
                right -= 1
    return list(triplets)

# https://leetcode.com/problems/missing-number/
def missingNumber(self, nums: List[int]) -> int:
    if len(nums) == 1:
        if nums[0] != 0:
            return nums[0] - 1
        else:
            return nums[0] + 1
    _min = nums[0]
    _max = nums[0]
    _sum = 0
    for num in nums:
        _min = min(_min, num)
        _max = max(_max, num)
        _sum += num
    if _min == 1:
        return 0
    total_sum = 0
    for num in range(_min, _max + 1):
        total_sum += num
    return total_sum - _sum if total_sum - _sum > 0 else _max + 1

# https://leetcode.com/problems/binary-tree-level-order-traversal
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _levelOrder(self, node: Optional[TreeNode], _dict, level):
    if node:
        if level not in _dict.keys():
            _dict[level] = list()
        _dict[level].append(node.val)
        self._levelOrder(node.left, _dict, level + 1)
        self._levelOrder(node.right, _dict, level + 1)

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    _dict = dict()
    self._levelOrder(root, _dict, 0)
    result = list()
    for level, nodes in _dict.items():
        result.append(nodes)
    return result

# https://leetcode.com/problems/trapping-rain-water
def trap(self, height: List[int]) -> int:
    max_left = 0
    max_right = 0
    max_list = list()
    for i in range(len(height)):
        max_list.append([max_left,0])
        max_list[i][0] = max_left
        max_left = max(max_left, height[i])
    for i in range(len(height) - 1, -1, -1):
        max_list[i][1] = max_right
        max_right = max(max_right, height[i])
    total_water = 0
    for i in range(len(height) - 1, -1, -1):
        boundaries = min(max_list[i][0], max_list[i][1])
        if boundaries > height[i]:
            total_water += boundaries - height[i]
    return total_water

# https://leetcode.com/problems/game-of-life
def get_status(self, board: List[List[int]], i, j) -> int:
  ''''
    Dead  = 0
    Alive = 1
    Death to Alive = 2
    Alive to Death = 3
  '''
  alive_count = 0
  for _i in range(i - 1, i + 2):
      for _j in range(j - 1, j + 2):
        if _i >= 0 and _i < len(board) and \
            _j >= 0 and _j < len(board[_i]):
          if _i == i and _j == j:
            continue;
          if board[_i][_j] in [1,3]:
            alive_count += 1
  if board[i][j] in [1,3]:
      if alive_count < 2:
          return 3
      elif alive_count <= 3:
          return 1
      else:
          return 3
  if board[i][j] in [0,2]:
      if alive_count == 3:
          return 2
      else:
          return 0

def gameOfLife(self, board: List[List[int]]) -> None:
  for i in range(len(board)):
      for j in range(len(board[i])):
          board[i][j] = self.get_status(board, i, j)
  for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == 2:
          board[i][j] = 1
        if board[i][j] == 3:
          board[i][j] = 0

# https://leetcode.com/problems/4sum
# Solution 1
def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
    result = set()
    nums.sort()
    for i in range(0, len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range(j + 1, len(nums) - 1):
                my_target = target - (nums[i] + nums[j] + nums[k])
                index = self.binary_search(nums, my_target, k + 1)
                if index != -1:
                    entry = tuple([nums[i], nums[j], nums[k], nums[index]])
                    result.add(entry)
    final_result = list()
    for e in result:
        final_result.append(list(e))
    return final_result

def binary_search (self, nums: List[int], target: int, index: int) -> int:
    left = index
    right = len(nums) - 1
    while (left <= right):
        mid = left + ((right - left) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
# Solution 2
def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
    result = set()
    nums.sort()
    for i in range(0, len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            ij_sum = nums[i] + nums[j]
            left = j + 1
            right = len(nums) - 1
            while left < right:
                left_right_sum = nums[left] + nums[right]
                if ij_sum + left_right_sum == target:
                    entry = tuple([nums[i], nums[j], nums[left], nums[right]])
                    result.add(entry)
                    left += 1
                elif ij_sum + left_right_sum > target:
                    right -= 1
                else:
                    left += 1
    final_result = list()
    for e in result:
          final_result.append(list(e))
    return final_result

# https://leetcode.com/problems/same-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def add_to_queue(self, queue: List[TreeNode], tree: Optional[TreeNode]) -> None:
    if tree != None:
        queue.append(tree)

def is_equal(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    if tree1.left is None and tree2.left is not None:
        return False
    if tree1.left is not None and tree2.left is None:
        return False
    if tree1.right is None and tree2.right is not None:
        return False
    if tree1.right is not None and tree2.right is None:
        return False
    return tree1.val == tree2.val

def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    if tree1 == None and tree2 == None:
        return True
    if (tree1 == None and tree2 != None) or \
        (tree1 != None and tree2 == None):
        return False
    queue1 = list()
    queue2 = list()
    queue1.append(tree1)
    queue2.append(tree2)
    while len(queue1) > 0 and len(queue2) > 0:
        node1 = queue1.pop(0)
        node2 = queue2.pop(0)
        if not self.is_equal(node1, node2):
            return False
        self.add_to_queue(queue1, node1.left)
        self.add_to_queue(queue1, node1.right)
        self.add_to_queue(queue2, node2.left)
        self.add_to_queue(queue2, node2.right)
    return True

# https://leetcode.com/problems/merge-k-sorted-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    comp = list()
    for l in lists:
        if l:
            comp.append(l)
    head = None
    tail = None
    while len(comp) > 0:
        smaller = comp[0].val
        smaller_index = 0
        for i in range(len(comp)):
            if comp[i].val < smaller:
                smaller = comp[i].val
                smaller_index = i
        if head == None:
            head = ListNode(smaller)
            tail = head
        else:
            tail.next = ListNode(smaller)
            tail = tail.next
        comp[smaller_index] = comp[smaller_index].next
        if comp[smaller_index] == None:
            del comp[smaller_index]
    return head

'''
Given A and B two interval lists sorted by start time, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap.
Example,
A: [1,5], [10,14], [16,18]
B: [2,6], [8,10], [11,20]
output [1,6], [8, 20]
'''
def _merge(current_interval: list, result: list) -> None:
    if current_interval[0] <= result[-1][1]:
        result[-1][1] = max(current_interval[1], result[-1][1])
    else:
      result.append([current_interval[0], current_interval[1]])

def merge_intervals(intervals1: list, intervals2: list) -> list:
    i1 = 0
    i2 = 0
    result = list()
    while i1 < len(intervals1) and i2 < len(intervals2):
        current_interval = None
        if intervals1[i1][0] < intervals2[i2][0]:
            current_interval = intervals1[i1]
            i1 += 1
        else:
            current_interval = intervals2[i2]
            i2 += 1
        if len(result) == 0:
            result.append([current_interval[0], current_interval[1]])
        else:
            _merge(current_interval, result)
    for i in range(i1, len(intervals1)):
        _merge(intervals1[i], result)
    for i in range(i2, len(intervals2)):
        _merge(intervals2[i], result)
    return result

# https://leetcode.com/problems/validate-binary-search-tree
class Solution:
    current = None
    isBST = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isBST = True
        self.inOrder(root)
        return self.isBST
    
    def inOrder(self, node: Optional[TreeNode]) -> None:
        if node is None or not self.isBST:
            return
        self.inOrder(node.left)
        if self.current is None:
            self.current = node.val
        else:
            if node.val <= self.current:
                self.isBST = False
                return
        self.current = node.val
        self.inOrder(node.right)

# https://leetcode.com/problems/move-zeroes
def moveZeroes(self, nums: List[int]) -> None:
    left = 0
    while left < len(nums) and nums[left] != 0:
        left += 1
    right = left + 1
    while right < len(nums):
        if right < len(nums) and nums[right] != 0:
            nums[left] = nums[right]
            nums[right] = 0
            left += 1
        right += 1

# https://leetcode.com/problems/single-number
def singleNumber(self, nums: List[int]) -> int:
    mySet = set()
    for n in nums:
        if n not in mySet:
            mySet.add(n)
        else:
            mySet.remove(n)
    return list(mySet)[0]

# https://leetcode.com/problems/roman-to-integer
def romanToInt(self, s: str) -> int:
    table = dict()
    table['I']  = 1
    table['IV'] = 4
    table['V']  = 5
    table['IX'] = 9
    table['X']  = 10
    table['XL'] = 40
    table['L']  = 50
    table['XC'] = 90
    table['C']  = 100
    table['CD'] = 400
    table['D']  = 500
    table['CM'] = 900
    table['M']  = 1000
    result = 0
    i = 0
    while i < len(s):
        term = None
        if i < len(s) - 1:
            twoDigits = s[i: i+2]
            if twoDigits in table.keys():
                term = table[twoDigits]
                i += 1
            else:
                term = table[s[i]]
        else:
            term = table[s[i]]
        result += term
        i += 1
    return result


# https://leetcode.com/problems/rotate-list/
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head == None:
        return None
    count = 0
    right = head
    left = None
    count = 1
    listLen = self.listLen(head)
    if listLen == 1 or k == 0 or listLen == k or k % listLen == 0:
        return head
    k = k %  listLen
    while right.next != None:
        if left is not None:
            left = left.next
        if count == k:
            left = head
        right = right.next
        count += 1
    newHead = left.next
    right.next = head
    left.next = None
    return newHead

def listLen(self, head: Optional[ListNode]) -> int:
    runner = head
    count = 0
    while (runner is not None):
        count += 1
        runner = runner.next
    return count
  
# https://leetcode.com/problems/copy-list-with-random-pointer
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
        return None
    mapping = dict()
    runner = head
    while runner:
        mapping[runner] = Node(runner.val)
        runner = runner.next
    runner = head
    while runner:
        if runner.next:
            mapping[runner].next = mapping[runner.next]
        if runner.random:
            mapping[runner].random = mapping[runner.random]
        runner = runner.next
    return mapping[head]

# https://leetcode.com/problems/valid-palindrome
def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# https://leetcode.com/problems/rotate-image
def rotate(self, matrix: List[List[int]]) -> None:
    # Rotate matrix using the principal diagonal as pivot
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each line
    for i in range(len(matrix)):
        left = 0
        right = len(matrix) - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

# https://leetcode.com/problems/symmetric-tree
class Solution:
    
    __isSymmetric = True
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.__isSymmetric = True
        if root:
            self.__check(root.left, root.right)
        return self.__isSymmetric

    def __check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> None:
        if not self.__isSymmetric:
            return
        if left is None and right is None:
            return
        elif left is None or right is None:
            self.__isSymmetric = False
        elif left.val != right.val:
            self.__isSymmetric = False
        else:
            self.__check(left.left, right.right)
            self.__check(left.right, right.left)

# https://leetcode.com/problems/maximum-depth-of-binary-tree
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    else:
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

# https://leetcode.com/problems/rotting-oranges/

# Solution one
def restoreValues(self, grid: List[List[int]]) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 3:
                grid[i][j] = 2

def rottenAround(self, grid: List[List[int]], i: int, j: int) -> bool:
    if i > 0 and grid[i - 1][j] == 2:
        return True
    if i < len(grid) - 1 and grid[i + 1][j] == 2:
        return True
    if j > 0 and grid[i][j - 1] == 2:
            return True
    if j < len(grid[i]) - 1 and grid[i][j + 1] == 2:
            return True
    return False

def allRotten(self, grid: List[List[int]]) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return False
    return True

def orangesRotting(self, grid: List[List[int]]) -> int:
    activity = True
    count = 0
    while activity:
        activity = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and self.rottenAround(grid, i, j):
                    grid[i][j] = 3
                    activity = True
        self.restoreValues(grid)
        count += 1
    if self.allRotten(grid):
        return count - 1
    else:
        return -1

# Solution 2
class Solution:
    
    FRESH = 1
    ROTTEN = 2
    
    def processCell(self, grid: List[List[int]], cell: list, nextQueue: list) -> None:
        i = cell[0]
        j = cell[1]
        if i > 0 and grid[i-1][j] == self.FRESH:
            grid[i-1][j] = self.ROTTEN
            nextQueue.insert(0, [i-1, j])
        if i < len(grid) - 1 and grid[i+1][j] == self.FRESH:
            grid[i+1][j] = self.ROTTEN
            nextQueue.insert(0, [i+1,j])
        if j > 0 and grid[i][j-1] == 1:
            grid[i][j-1] = self.ROTTEN
            nextQueue.insert(0, [i, j-1])
        if j < len(grid[i]) - 1 and grid[i][j+1] == self.FRESH:
            grid[i][j+1] = self.ROTTEN
            nextQueue.insert(0, [i, j+1])
    
    def hasStatus(self, grid: List[List[int]], status: int) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == status:
                    return True
        return False
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not self.hasStatus(grid, self.ROTTEN):
            if self.hasStatus(grid, self.FRESH):
                return -1
            else:
                return 0
        currentQueue = list()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == self.ROTTEN:
                    currentQueue.append([i, j])
        response = 0
        nextQueue = list()
        while len(currentQueue) > 0:
            currentCell = currentQueue.pop()
            self.processCell(grid, currentCell, nextQueue)
            if len(currentQueue) == 0:
                response += 1
                currentQueue = nextQueue
                nextQueue = list()
        if self.hasStatus(grid, self.FRESH):
            return -1
        else:
            return response - 1

# https://leetcode.com/problems/squares-of-a-sorted-array
def sortedSquares(self, nums: List[int]) -> List[int]:
    left = -1
    for i in range(len(nums) - 1):
        if nums[i] < 0 and nums[i + 1] >= 0:
            left = i
            break
    if left == -1:
        if (nums[0] < 0):
            nums.reverse()
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return nums
    right = left + 1
    sortedList = list()
    while left >= 0 and right < len(nums):
        leftSquare = nums[left] ** 2
        rightSquare = nums[right] ** 2
        if leftSquare < rightSquare:
            sortedList.append(leftSquare)
            left -= 1
        else:
            sortedList.append(rightSquare)
            right += 1
    print(left, right)
    while left >= 0:
        sortedList.append(nums[left] ** 2)
        left -= 1
    while right < len(nums):
        sortedList.append(nums[right] ** 2)
        right += 1
    return sortedList