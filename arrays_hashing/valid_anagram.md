# Valid Anagram

**Link:** https://neetcode.io/problems/is-anagram | **Difficulty:** Easy

## Problem

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**
```
Input: s = "racecar", t = "carrace"
Output: true
```

**Example 2:**
```
Input: s = "jar", t = "jam"
Output: false
```

## Solution

This problem asks us to return `true` when the two strings contain the same letters — they don't necessarily have to be in the same order. To do this, we can use a `dict` (hash map) to create an empty table, then write a for loop that goes through each character in the given string. Inside that loop we count how many times each character appears in the string, then do the same for the other string. After that, we compare the two dicts and return `true` if they're equal, otherwise `false`.

**Why use a dict?** A dict can remember and store whether a character is already in the table when we add a new one, and look it up almost instantly (O(1)). If we used a normal list instead, we'd need an extra for loop plus if/else logic to go search whether the character is already there — which is much slower.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = {}
        table2 = {}

        for ch in s:
            table1[ch] = table1.get(ch, 0) + 1
        for ch in t:
            table2[ch] = table2.get(ch, 0) + 1

        if table1 == table2:
            return True
        return False
```
