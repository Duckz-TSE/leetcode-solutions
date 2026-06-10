# Contains Duplicate

**Link:** https://neetcode.io/problems/duplicate-integer | **Difficulty:** Easy

## Problem

Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

**Example 1:**
```
Input: nums = [1, 2, 3, 3]
Output: true
```

**Example 2:**
```
Input: nums = [1, 2, 3, 4]
Output: false
```

## Solution

This is a problem about finding duplicate values in an array. The straightforward way to solve it would be to create a nested loop with two loops, comparing each number against every other one. But if we do that, the time/space complexity won't be optimal, so we need a different approach — and that's where a hash set comes in.

In a nutshell, a hash set works differently from a normal list. When you look for a value in a normal list, it has to check every slot one by one. But with a hash set, it takes the value you're searching for, runs it through a hash function to turn it into an address, and jumps straight to that location to check whether the value is there.

With that idea, we can solve this problem by creating an empty set (`seen = set()`), then using a for loop to go through each value in the array. During that process, before adding a value to the set, we use an `if` statement to check whether the value is already in the set — using `if num in seen`. If it is, we immediately return `true`. If not, we add the value to the set and keep going until we run out, and then return `false`.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```
