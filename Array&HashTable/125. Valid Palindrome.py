class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = [i for i in s.lower() if i.isalnum()]
        return text == text[::-1]
