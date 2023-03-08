class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        value = x
        rev_num = ""
        import pdb;
        pdb.set_trace()
        while x:
            rev_num += str(x % 10)
            x = x // 10

        return value == int(rev_num)


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if 0 <= x < 10:
            return True

        rev_num = 0

        while x > rev_num:
            rev_num = rev_num * 10 + (x % 10)
            x = x // 10

        return x==rev_num or x==rev_num/10


if __name__ == '__main__':
    s = Solution2()
    s.isPalindrome(121)
