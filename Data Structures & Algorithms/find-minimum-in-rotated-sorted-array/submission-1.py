class Solution:
    def findMin(self, nums: List[int]) -> int:
        size_of_the_list = len(nums) - 1
        index_of_first_element = 0
        index_of_last_element = size_of_the_list

        counter = 0

        while index_of_first_element <= index_of_last_element:
            mid_point = (index_of_first_element + index_of_last_element) // 2 # Using floor division to avoid float values

            if nums[mid_point] < nums[index_of_first_element]: 
                index_of_last_element = mid_point
                counter += 1
            elif nums[mid_point] > nums[index_of_last_element]:
                index_of_first_element = mid_point
                counter += 1

            # If this condition true, it means the list is already sorted and smallest element is on first index
            if counter == 0:
                return nums[0]

            if index_of_last_element - index_of_first_element == 1:
                if nums[index_of_first_element] > nums[index_of_last_element]:
                    return nums[index_of_last_element]
                else:
                    return nums[index_of_first_element]
            