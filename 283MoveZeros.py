class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
       
        index = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                hold=nums[index]
                nums[index]=nums[i]
                nums[i]=hold
                index+=1


if __name__ == '__main__':
    a=Solution()
    nums = [0,1,0,3,12]
    a.moveZeroes(nums)
    print(nums)