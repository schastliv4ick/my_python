from typing import List


l = []
def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    global l
    for i, n1, n2 in enumerate(zip(nums1, nums2)):
        if n1 < n2:
            l.append(i)
    return l 
         
   

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)