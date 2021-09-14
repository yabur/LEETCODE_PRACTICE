# def two_sum(nums, target):
#     """
#     :type target: ints
#     :type nums: List[int]
#     :rtype: List[int]
#     """
        # dic = {}

        # for i, num in enumerate(nums):
        #     if target - num in dic:
        #         return [dic[target-num], i]
        #     dic[num] = i


def twoSum(numbers: [int], target: int) -> [int]:
    
    # 2 pointer approach
    start = 0
    end = len(numbers) - 1
    
    while start < end:
        # case 1:
        if numbers[start] + numbers[end] == target:
            return  [start+1, end+1]
        # case 2:
        if numbers[start] + numbers[end] > target:
            end -= 1
        # case 3:
        if numbers[start] + numbers[end] < target:
            start += 1
    return [-1,-1]

if __name__ == '__main__':

    A = [2, 7, 11, 15]
    print(twoSum(A, 9))
