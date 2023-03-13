#initial solution failed with TLE
class Solution:

    def numOfSubarrays(self, arr, k, threshold) -> int:

        count = 0
        for i in range(len(arr)):
            import pdb;pdb.set_trace()
            if i + k > len(arr):
                break
            if sum(arr[i:i + k])// k >= threshold:
                count += 1

        return count


#implemeted current running sum. Passed all test cases.
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # we are counting sum

        curSum = sum(arr[:k - 1])
        count = 0

        for leftptr in range(len(arr) - k + 1):

            curSum += arr[leftptr + k - 1]
            if curSum // k >= threshold:
                count += 1

            curSum -= arr[leftptr]

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays([2,2,2,2,5,5,5,8],3,4))
