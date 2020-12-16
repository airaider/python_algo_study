#Tip

1. `isalnum()` : 영문자, 숫자 판별 함수

    ex) `char.isalnum()` => 맞으면 True 반환
   

2. `lower()` : 소문자 변환


3. `pop()` : 가장 끝에 있는 인자 제거, pop(index)으로 지정 가능


4. 정규표현식
   `string = re.sub('[^a-z0-9]', '', string)`
   

5. `list[::-1]` : 문자열 뒤집기 


6. lamba 표현식 
   
   ex) `letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))`

   key는 x.split()[1:] 식별자를 제외한 [1:] 이후를 키로 지정, 만약 동일시에는 x.split()[0] 식별자로 순서 지정

   a.sort(key = lambda(x : (조건)))


7. Counter 객체

   `collections.Counter()` -> 객체의 빈도수를 key, value 값으로 지님

   `counts.most_common(1)` -> 가장 빈도수 높은 객체를 return


8. `re.sub(r'[^\w]', ' ', paragraph)` -> 문자 이외의 값을 빈칸으로 치환


9. `"".join()` : 문자열 합치기