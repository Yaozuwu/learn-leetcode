class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Create a dict which can remember the location and number of each items in the list( Hash table)
        Time Complexity: O(n)
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return (i, dict[target -x])
            dict[x] = i