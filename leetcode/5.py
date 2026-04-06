# class Solution(object):
#     def exist_palindrome(s: str) -> bool:
#         start = 0
#         end = len(s) - 1
#         f = True
#         while start <= end:
#             if s[start] != s[end]:
#                 f = False
#             start += 1
#             end -= 1
#         return f

#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s) <= 1:
#             return s
#         if self.exist_palindrome(s):
#             res = s
#         else:
#             p1 = self.longestPalindrome(self, s[1:])
#             p2 = self.longestPalindrome(self, s[:-1])
#             res = max(p1, p2)
#         return res
    
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_palidrom = ""
        if len(s) <= 1:
            max_palidrom = s
            return max_palidrom
        for i in len(s):
            
        return max_palidrom

res =  Solution.longestPalindrome(Solution, "abaa")
print(res)