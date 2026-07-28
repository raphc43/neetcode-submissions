from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        if any(count > 1 for count in counter.values()):
            return True
        return False
        
        