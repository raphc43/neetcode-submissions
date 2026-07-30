class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {nums[0]: 0}
        for i in range(len(nums)):
            if i != 0 and target - nums[i] in stored:
                return [stored[target - nums[i]], i]
            else:
                stored[nums[i]] = i
        