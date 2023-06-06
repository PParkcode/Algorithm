# Algorithm
### 풀면서 깨달은 것이나 팁이 있다면 정리해보자

## 😲 Tip

- ### Map, HashMap
- #### HashMap의 삽입, 검색, 삭제 모두 O(1)의 복잡도이다.
  시간 초과가 발생한다면 고려해보자
  
- #### Map은 불변형, HashMap은 가변형
  
- #### HashMap<String, MutableList<>> 형식
   위와 같이 사용하고 싶으면 리스트 초기화 후 add 연산을 하자
   ```
   map[key] = mutableListOf<Pair<Int,Int>>() //리스트 초기화
            
   map[key]?.add(Pair(i,something[i])) // 값 삽입
  ```

- #### map에서 value 로 정렬을 하고 싶다면 
  ```
  val sortedMap = map.toList().sortedBy { it.second }.toMap().toMutableMap()
  
  val sortedMap = map.toList().sortedByDescending { it.second }.toMap().toMutableMap()
  ```
