#TIP

---


###1. 제네릭 타입이기 때문에 자료형 명시 불필요

    하지만 가독성, 효율성을 위해서 함수 인자로 넘길 시에, 명시하는 것이 중요!
    
    ex) `def solution(test : int): print(test)` 

<br>

###2. `sorted()` 

   tim 소트
   
   key= 옵션 가능

   `.sort() `

   in-place 소트

   리턴값 없음 (None 리턴)

<br>

###3. 딕셔너리 순서 저장

   3.7 이상의 버전에서만 입력 순서 유지

<br>

###4. 해시 테이블

파이썬 -> 오픈 어드레싱

자바 -> 개별 체이닝

<br>

###5. list copy 방법

파이썬은 모든 객체를 참조하는 형태로 퍼리

[:]

copy()

deepcopy()

<br>

###6. 다익스트라 최단경로 알고리즘

```
Q = [(0,K)]
dist = collections.defaultdict(int)
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v,w in graph[node]:
            alt = time+w
            heapq.heappush(Q, (alt, v))

```        
