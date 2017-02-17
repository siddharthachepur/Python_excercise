class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # non_duplicates = [x for x in nums if nums.count(x) == 1]
        # return non_duplicates
        # (OR)
        # for x in nums:
        #    if nums.count(x) == 1:
        #        return x
        s = set()
        for x in nums:
            if x in s:
                s.remove(x)
                continue
            s.add(x)
        return s.pop()
