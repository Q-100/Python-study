class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i.isalnum():
                tmp.append(i.lower())
        return tmp == tmp[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]
