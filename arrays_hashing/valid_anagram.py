# Valid Anagram | Easy | Hash Map
# https://neetcode.io/problems/is-anagram
# Time: O(n + m), Space: O(1)  (at most 26 lowercase letters)

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
