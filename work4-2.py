while(1):
    nums = input("请录入一个整数(输入STOP结束)：")
    if(nums == "STOP"):
        break
target = input("请输入一个指定的数：")
target = int(target)
for i in nums:
    for j in nums:
        if(nums[i] + nums[j] == target):
            print("列表为%d,%d：",i,j)
            nums1 = [i,j]
            print(nums1)

