# My Solution
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_list = {}
        for element in range(1, len(nums)+1):
            if element not in nums:
                ret_list[element] = True
        return ret_list.keys()


# Subbu Solution
    def findDisappearedNumbers_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        aux = 0
        for each_num in nums:
            if not (aux & 1 << each_num):
                aux = aux | 1 << each_num
        return [each for each in range(1, len(nums)+1) if not (aux & 1 << each)]

# Fast & optimistic Solution
    def findDisappearedNumbers_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
