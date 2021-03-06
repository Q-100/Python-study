class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # s = s[::-1]도 원래는 가능하지만 leetcode에서 공간복잡도를 O(1)로줌