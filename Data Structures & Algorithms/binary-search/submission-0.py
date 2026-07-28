class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size_of_the_list = len(nums) - 1
        index_of_first_element = 0
        index_of_last_element = size_of_the_list

        while index_of_first_element <= index_of_last_element:
            mid_point = (index_of_first_element + index_of_last_element) // 2 # Using floor division to avoid float values

            if nums[mid_point] == target:
                return mid_point

            if target > nums[mid_point]: 
                index_of_first_element = mid_point + 1
            else:
                index_of_last_element = mid_point - 1

        if index_of_first_element > index_of_last_element:
            return -1
            