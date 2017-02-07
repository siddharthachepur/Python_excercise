class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(findNums)):
            flag = 0
            for k in range(len(nums)):
                if findNums[i] == nums[k]:
                    break
            for j in range(k+1, len(nums)):
                if nums[j] > findNums[i]:
                    flag = 1
                    res.append(nums[j])
                    break
            if flag == 0:
                res.append(-1)
        return res
