"""
冒泡排序
"""


def bubble(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [3, 6, 4, 2, 11, 10, 5, 4, 3, 7]
    print(bubble(nums))

