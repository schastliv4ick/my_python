class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        r = 0.0        
        l = len(nums1) + len(nums2)
        nums = sorted(nums1 + nums2)
        ind_med = l//2
        if len(nums) % 2: 
           r = nums[ind_med]
        else:
            r = (nums[ind_med] + nums[ind_med-1])/2
        
        return r
        
res =  Solution.findMedianSortedArrays(Solution, [1,2],[3,4])
print(res)