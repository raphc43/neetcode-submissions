class Solution:
    def binary_search_small_int_index(self, nums: List[int]) -> int:
        """RETURNS INDEX OF THE SMALLEST INTEGER"""
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
                return 0

            if index_of_last_element - index_of_first_element == 1:
                if nums[index_of_first_element] > nums[index_of_last_element]:
                    return index_of_last_element
                else:
                    return index_of_first_element

    def search(self, nums: List[int], target: int) -> int:
        smallest_int_index = self.binary_search_small_int_index(nums)
        length_to_be_added = 0	

        if smallest_int_index != 0:
            if target == nums[smallest_int_index]:
                return smallest_int_index
            if target <= nums[-1]:
                length_to_be_added = len(nums[:smallest_int_index])
                del nums[:smallest_int_index]
            elif target >= nums[0]:
                del nums[smallest_int_index:]

        size_of_the_list = len(nums) - 1
        index_of_first_element = 0
        index_of_last_element = size_of_the_list

        while index_of_first_element <= index_of_last_element:
            mid_point = (index_of_first_element + index_of_last_element) // 2 # Using floor division to avoid float values

            if nums[mid_point] == target:
                return mid_point + length_to_be_added

            if target > nums[mid_point]: 
                index_of_first_element = mid_point + 1
            else:
                index_of_last_element = mid_point - 1

        if index_of_first_element > index_of_last_element:
            return -1