# time complexity - O(n)
# space complexity - O(n)


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        repeat = {}
        pairs = 0

        for num in nums:

            if num in repeat:

                if repeat[num] == 1:
                    pairs += 1
                else:
                    pairs += repeat[num]

                repeat[num] += 1
            else:
                repeat[num] = 1

        return pairs
