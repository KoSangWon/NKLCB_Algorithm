from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True
    
    
def solution(numbers):
    answer = 0
    num_list = list(numbers)
    arr = []
    for i in range(len(num_list)):
        arr += [''.join(j) for j in permutations(num_list, i + 1)]
        
    arr = list(set(arr))
    for i in arr:
        if i[0] == '0':
            continue
        if is_prime(int(i)):
            answer += 1
            
    return answer
solution('011')