# Two Sum

**Link:** https://neetcode.io/problems/two-integer-sum | **Difficulty:** Easy

## Problem

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume exactly one valid pair exists. Return the answer with the smaller index first.

**Example 1:**
```
Input: nums = [3,4,5,6], target = 7
Output: [0,1]      (nums[0] + nums[1] == 7)
```

**Example 2:**
```
Input: nums = [5,5], target = 10
Output: [0,1]
```

## Solution

This problem asks us to return the indices of the two numbers whose sum equals `target`, with the condition that the two indices can't be the same.

There are many ways to find those two indices, but if we use ordinary if/else logic we'd have to add every number against every other one to find the pair — that's slow, an O(n²) solution. Instead we use a hash map (a `dict`), because a dict stores a **value → index** pair. That way, when we look up a value, we get back its index rather than the value itself.

But before coding it, we need to figure out how to search efficiently. We need `nums[i] + nums[j] == target`. Keeping it in this form is hard to apply a hash map to. Instead, if we fix the current number `num` and rearrange the equation into `diff = target - num`, then `diff` is exactly the other number we're looking for — and we can use the hash map to find it quickly.

**How it works:** We create an empty hash table (`seen = {}`), then run a for loop with a counter `i` and `num` holding the current value from the array (`for i, num in enumerate(nums)`). Inside the loop we compute `diff = target - num`. Then we check whether `diff` is already in the map (`if diff in seen`). If it is, it means `diff + num == target`, so we just return the index of `diff` and `i` (the index of the current number) — done. If `diff` isn't in the map yet, we store the current value with its index into the map (`seen[num] = i`) and continue the loop until it finishes.

Checking before storing is what guarantees `i != j`: we only ever match the current number against numbers we've already seen in earlier iterations, so the two indices can never be the same.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return
```
