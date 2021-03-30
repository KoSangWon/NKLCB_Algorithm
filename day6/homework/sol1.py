from collections import deque
def solution(priorities, location):
    answer = 0
    queue = [(i, idx) for idx, i in enumerate(priorities)]
    
    while True:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            answer += 1
            if queue[0][1] == location:
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

    return answer

solution([2,1,3,2], 2)