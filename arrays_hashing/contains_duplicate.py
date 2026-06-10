# Contains Duplicate | Easy | Hash Set
# https://neetcode.io/problems/duplicate-integer
# Time: O(n), Space: O(n)

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
