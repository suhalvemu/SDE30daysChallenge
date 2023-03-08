# time complexity O(n)
# space complexity O(1) because english has 26 alphabets
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_1, dict_2 = dict(), dict()

        if len(s) != len(t):
            return False

        for c in s:
            if c in dict_1:
                dict_1[c] += 1
            else:
                dict_1[c] = 1

        for c in t:
            if c in dict_2:
                dict_2[c] += 1
            else:
                dict_2[c] = 1

        return dict_1 == dict_2