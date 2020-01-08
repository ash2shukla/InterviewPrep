class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_num = -1
        for i in nums:
            i_num = i_num+1
            slice_obj = slice(i_num+1,len(nums),1)
            nums2 = nums[slice_obj]
            for j in nums2:
                obtained_sum = i+j
                if obtained_sum == target:
                    if i == j:
                        return[nums.index(i), nums.index(i,nums.index(i)+1,len(nums))]
                    else:
                        return[nums.index(i),nums.index(j)]
    