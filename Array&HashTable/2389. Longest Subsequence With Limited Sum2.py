class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefixSum = [0]

        nums.sort()
        for n in nums:
            lastValue = prefixSum[-1]
            newValue = lastValue + n
            prefixSum.append(newValue)
        
        result = []

        for q in queries:
            index = bisect_right(prefixSum, q) -1
            result.append(index)
        
        return result
