class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = defaultdict(int)
        for i in s:
            cnt[i] += 1
        for i in t:
            cnt[i] -= 1
        for i in cnt.values():
            if i != 0:
                return False
        return True
