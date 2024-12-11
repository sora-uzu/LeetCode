class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        sortedItems = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        topKItems = sortedItems[:k]
        
        return [key for key, value in topKItems]
