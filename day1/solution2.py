def solution(nums):
    answer = 0
    nums_len = len(nums)//2
    set_len = len(set(nums))
    answer = set_len if set_len < nums_len else nums_len
    return answer