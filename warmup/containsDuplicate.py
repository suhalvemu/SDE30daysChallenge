# time complexity O(n)
# space complexity O(n)

class Solution:
    def containsDuplicate(self, nums) -> bool:

        num_map=dict()

        for num in nums:
            if num in num_map.keys():
                return True
            else:
                num_map[num] = 1

        return False


if __name__ == '__main__':
    s = Solution()
    s.containsDuplicate([1,2,3,4])