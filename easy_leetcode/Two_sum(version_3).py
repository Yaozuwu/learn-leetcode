class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Using two pointers named start and end to trace the index of original list
        Time complexity is O(n)
        Space complexity is O(n)
        """
        start, end = 0, len(nums)-1
        numtosort = nums[:]; numtosort.sort()
        index = []
        while start < end :
            if numtosort[start] + numtosort[end] == target:###Using two loops to traceback indexs, the cost is still O(n)
                for k in range(len(nums)):
                    if nums[k] == numtosort[start]:
                        index.append(k)
                        break
                for k in range(len(nums)-1, -1, -1):
                    if nums[k] == numtosort[end]:
                        index.append(k)
                        break
                index.sort()
                break ###after acquire the index, we should get off the loop, otherwise it will loop forever
            elif numtosort[start] + numtosort[end] < target:
                start +=1
            elif numtosort[start] + numtosort[end] > target:
                end -=1
        return (index[0], index[1])