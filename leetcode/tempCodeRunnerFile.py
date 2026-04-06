class Solution(object):
    def lengthOfLongestSubstring(self, s):
        cnt = 0
        last = []
        for w in s:
            if w in last:
                cnt = max(len(last), cnt)
                last = last[(last.index(w) + 1):]
            else:
                last.append(w)
                cnt = max(len(last), cnt)
        return cnt
        

res =  Solution.lengthOfLongestSubstring(Solution, "aabaab!bb")
print(res)