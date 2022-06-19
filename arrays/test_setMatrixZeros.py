from ast import main
import unittest
from setMatrixZeros import Solution



class SolutionTest(unittest.TestCase):

    def test_case_1(self):
        input_list=[[1,1,1],[1,0,1],[1,1,1]]
        obj = Solution()
        obj.setZeroes(input_list)
        self.assertEqual(input_list,[[1,0,1],[0,0,0],[1,0,1]])

    def test_case_2(self):
        input_list=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        obj = Solution()
        obj.setZeroes(input_list)
        self.assertEqual(input_list,[[0,0,0,0],[0,4,5,0],[0,3,1,0]])



if __name__ == '__main__':
    unittest.main()