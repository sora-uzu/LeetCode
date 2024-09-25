class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumNum = 0
        res = []
        for i in nums:
            sumNum += i
            res.append(sumNum)
        return res
