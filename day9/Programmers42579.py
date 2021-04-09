# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    ht1 = dict()
    ht2 = dict()
    
    for i, elem in enumerate(zip(genres, plays)):
        g, p = elem
        if g not in ht1:
            ht1[g] = 0
            ht2[g] = []
            
        ht1[g] += p
        ht2[g].append((i, p))
        
    sort_ht1 = sorted(list(ht1.items()), key=lambda x:-x[1]) # 값을 기준으로 역순 정렬
    print(sort_ht1)
    print(ht2)
    
    for g, p in sort_ht1:
        sort_ht2 = sorted(ht2[g], key=lambda x:-x[1]) # stable sort를 사용하고 있기 때문에 재생 횟수 기준 낮은 노래 신경 안써도 됨. 
        print(sort_ht2)
        answer += list(map(lambda x: x[0], sort_ht2))[:2]
        
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])