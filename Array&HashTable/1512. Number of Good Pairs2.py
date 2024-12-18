class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        cnt = 0

        for i in nums:
            if i in repeat:
                if repeat[i] == 1:
                    cnt += 1
                else:
                    cnt += repeat[i]
                repeat[i] += 1
            else:
                repeat[i] = 1
                
        return cnt
