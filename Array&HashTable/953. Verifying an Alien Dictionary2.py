class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def alienKey(word):
            key=[]
            for c in word:
                key.append(order.index(c))
            return key
        
        sortedWords = sorted(words, key=alienKey)

        return words == sortedWords
