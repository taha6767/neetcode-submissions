class Solution:
    

    def search(self, nums: List[int], target: int) -> int:
        def find_split():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1   # split is strictly right of mid
                else:
                    right = mid      # split is at mid or left of it
            return left
        split = find_split()
        if(target == nums[len(nums)-1]):
            return len(nums)-1
        if(target > nums[len(nums)-1]):
            left = 0
            right = split-1
            while(left < right):
                mid = (left+right)//2
                if(target == nums[mid]):
                    return (mid)
                if(target > nums[mid]):
                    left = mid+1
                else:
                    right = mid
            return left if nums[left] == target else -1
        if(target < nums[len(nums)-1]):
            left = split
            right = len(nums) - 1
            while(left<right):
                mid = (left + right) //2
                if(target == nums[mid]):
                    return mid
                if(target > nums[mid]):
                    left = mid+1
                else:
                    right = mid
            return left if nums[left] == target else -1

                