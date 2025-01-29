class Solution:
    def majorityElement(self, alist):
        adict = {}
        max_value = 0
        for item in alist:
            if item in adict:
                adict[item] +=1
            else:
                adict[item] = 1
        
        for key, value in adict.items():
            if value > max_value:
                max_value = value
                max_key = key
        
        return max_key
            
                
                
    
    
    
solution  = Solution()
result = solution.majorityElement([2,3,4,3,3,3,3,1])
print(result)