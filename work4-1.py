nums = [1,2,3,4,5,6,7,8,9]
target = 10
for i in nums:
    for j in nums:
        if(nums[i-1] + nums[j-1] == target):
            print("列表为%d,%d：",i,j)
            nums1 = [i,j]
            print(nums1)
