class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, arr in enumerate(matrix):
            if target > arr[-1]:
                if i == len(matrix) - 1:
                    return False
                else:
                    continue
                    
            elif target < arr[-1]:
                nums = arr
                print('we')
                break
            elif arr[-1] == target:
                return True
            
            if i == len(matrix) - 1:
                return False            
                
        size_of_the_list = len(nums) - 1
        index_of_first_element = 0
        index_of_last_element = size_of_the_list

        while index_of_first_element <= index_of_last_element:
            mid_point = (index_of_first_element + index_of_last_element) // 2 # Using floor division to avoid float values

            if nums[mid_point] == target:
                return True

            if target > nums[mid_point]: 
                index_of_first_element = mid_point + 1
            else:
                index_of_last_element = mid_point - 1

        if index_of_first_element > index_of_last_element:
            return False
        