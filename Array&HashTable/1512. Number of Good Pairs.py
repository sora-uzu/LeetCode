class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for i in nums:
            if i in hashMap:
                res += hashMap[i]
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        return res
