from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 1
        while result in nums:
            result += 1
        return result

app = Solution()
print(app.firstMissingPositive([1,2,3,10,2147483647,9]))