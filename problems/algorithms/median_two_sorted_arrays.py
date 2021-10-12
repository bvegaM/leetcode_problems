from typing import List
import statistics

class Solution:

    ## Improve solution because the complexity of this algorithm is O(m+n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        return statistics.median(nums3)


if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    solution = Solution()
    response = solution.findMedianSortedArrays(nums1, nums2)
    print(response)