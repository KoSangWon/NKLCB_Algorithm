class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()
        self.count_leaf = 0 # 파생 단어 개수(leaf 노드 개수)
        
class Trie:
    def __init__(self):
        self.head = Node(None)
        self.word_count = 0
        
    def insert(self, word):
        curr = self.head
        
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
            curr.count_leaf += 1
        
        curr.child['*'] = True
        self.word_count += 1
    
    def search(self, word):
        curr = self.head
        marth_fail = False
        
        for c in word:
            if c != '?':
                if c not in curr.child:
                    match_fail = True
                    break # 검색 실패하면 탈출
                curr = curr.child[c]
            else:
                return curr.count_leaf # Case 1:'?'를 만나는 순간 하위 개수 return
            
        if match_fail is True:
            return 0 # Case 2: 매치 단어 없음
        
        return 1 # Case 3: 단어 일치
    
def solution(words, queries):
    tries = dict()
    inv_tries = dict()
    
    # 글자 수 별로 Trie를 만들어주고 단어들을 삽입해줌
    for word in words:
        word_len = len(word)
        
        if word_len not in tries:
            tries[word_len] = Trie() # Trie 초기 생성
            inv_tries[word_len] = Trie()
            
        tries[word_len].insert(word) # Trie에 삽입
        inv_tries[word_len].insert(word[::-1]) # 전위 와일드카드를 위해 생성(역순으로 생성)
        
    answer = list()
    for query in queries:
        query_len = len(query)
    
        if query_len not in tries: # Case 1: 글자 수 맞지 않는 경우
            answer.append(0)
        elif query.count('?') == query_len: # Case 2: 모든 글자가 '?'인 경우
            answer.append(tries[query_len].word_count)
        elif query[0] == '?': # Case 3: 전위 와일드카드(역순으로 해결)
            answer.append(inv_tries[query_len].search(query[::-1]))
        else: # Case 4: 후위 와일드카드
            answer.append(tries[query_len].search(query))
        
    return answer
        

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
        