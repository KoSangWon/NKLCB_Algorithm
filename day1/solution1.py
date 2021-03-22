def solution(n):
    if n == 0 or n == 1:
        answer = n
    else:
        answer = n + 1
        for i in range(2, n//2 + 1):
            if n % i == 0:
                answer += i
    return answer