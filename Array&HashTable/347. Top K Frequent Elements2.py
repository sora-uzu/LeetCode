class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1
        
        sorted_cnt = sorted(cnt.items(), key=lambda item: item[1], reverse=True)

        top_k_keys = []
        for item in sorted_cnt[:k]:
            top_k_keys.append(item[0])
        
        return top_k_keys
