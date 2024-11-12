class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        word1 = set(words[0])
        for char in word1:
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        return res
