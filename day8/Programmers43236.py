def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance

    while left <= right:        
        cur = 0
        removed_cnt = 0 # 삭제 개수
        min_distance = float('inf')
        mid = (left + right) // 2
        
        for rock in rocks:
            dist = rock - cur
            if dist < mid:
                removed_cnt += 1
            else:
                cur = rock # 현재 바위 업데이트
                min_distance = min(min_distance, dist) # 최소 거리 업데이트
                
        if removed_cnt > n:
            right = mid - 1 # 왼쪽으로 범위 지정
        else:
            answer = min_distance
            left = mid + 1 # 오른쪽으로 범위 지정
    return answer


if __name__=="__main__":
    print(solution(25, [2, 14, 11, 21, 17], 2))

