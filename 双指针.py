#15.三数之和：给一个包含n个整数的数组，判断nums是否存在a，b，c使得a+b+c=0
def threeSum(nums):
    # 选择一个C位k，再双指针
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        if nums[k] > 0: break  # 1. because of j > i > k.
        if k > 0 and nums[k] == nums[k - 1]: continue  # 2. 跳过重复
        i, j = k + 1, len(nums) - 1
        while i < j:  # 3. 双指针
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]: i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]: i += 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
    return res
#print(threeSum([-1,0,1,2,-1,-4]))

#18.四数之和：给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
def fourSum(nums, target):
    result = []
    if not nums or len(nums) < 4:
        return result
    nums.sort()  # 必须排序
    length = len(nums)
    for k in range(length - 3):
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        min1 = nums[k] + nums[k + 1] + nums[k + 2] + nums[k + 3]
        if min1 > target:
            break
        max1 = nums[k] + nums[length - 1] + nums[length - 2] + nums[length - 3]
        if max1 < target:
            continue
        for i in range(k + 1, length - 2):  # 三数之和
            if i > k + 1 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            h = length - 1
            min2 = nums[k] + nums[i] + nums[j] + nums[j + 1]
            if min2 > target:
                continue
            max2 = nums[k] + nums[i] + nums[h] + nums[h - 1]
            if max2 < target:
                continue
            while j < h:
                curr = nums[k] + nums[i] + nums[j] + nums[h]
                if curr == target:
                    result.append([nums[k], nums[i], nums[j], nums[h]])
                    j += 1
                    while j < h and nums[j] == nums[j - 1]:
                        j += 1
                    h -= 1
                    while j < h and nums[h] == nums[h + 1]:
                        h -= 1
                elif curr > target:
                    h -= 1
                elif curr < target:
                    j += 1
    return result
#print(fourSum([1,0,-1,0,-2,2], 0))

#75.颜色分类:给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
# 使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
def sortColors(nums):
    #荷兰三色旗问题解，0指针的左边界，2指针的右边界
    # 对于所有 idx < p0 : nums[idx < p0] = 0
    # curr是当前考虑元素的下标
    p0 = curr = 0
    # 对于所有 idx > p2 : nums[idx > p2] = 2
    p2 = len(nums) - 1
    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1
    return nums
#print(sortColors([2,0,2,1,1,0]))

#163.缺失的区间:给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，
# 返回不包含在数组中的缺失区间。
def findMissingRanges(nums, lower, upper):
    res = []
    low = lower - 1
    nums.append(upper + 1)
    for num in nums:
        dif = num - low
        if dif == 2:
            res.append(str(low + 1))
        elif dif > 2:
            res.append(str(low + 1) + "->" + str(num - 1))
        low = num
    return res
#print(findMissingRanges([0,1,3,50,75], 0, 99))


