class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = nums[0]
        if len(nums) == 0:
            return res

        for i in range(1, len(nums)):
            res ^= nums[i]

        return res