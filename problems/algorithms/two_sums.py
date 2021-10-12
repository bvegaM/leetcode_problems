from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,j in enumerate(nums):
            difference = target-j
            if difference in hashMap: return (hashMap[difference],i)
            hashMap[j]=i
        return ()

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    response = solution.twoSum(nums,target)
    print(response)
