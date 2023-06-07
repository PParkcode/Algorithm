# Algorithm
### 풀면서 깨달은 것이나 팁이 있다면 정리해보자

## 😲 Tip

### Map, HashMap
- #### HashMap의 삽입, 검색, 삭제 모두 O(1)의 복잡도이다.
  시간 초과가 발생한다면 고려해보자
  
- #### Map은 불변형, HashMap은 가변형
  
- #### HashMap<String, MutableList<>> 형식
   위와 같이 사용하고 싶으면 리스트 초기화 후 add 연산을 하자
   ```kotlin
   map[key] = mutableListOf<Pair<Int,Int>>() //리스트 초기화
            
   map[key]?.add(Pair(i,something[i])) // 값 삽입
  ```

- #### map에서 value 로 정렬을 하고 싶다면 
  ```kotlin
  val sortedMap = map.toList().sortedBy { it.second }.toMap().toMutableMap()
  
  val sortedMap = map.toList().sortedByDescending { it.second }.toMap().toMutableMap()
  ```

### Queue

- #### Queue 사용법
```kotlin
var q : Queue<Int> = LinkedList() // 큐로 선언하고 LinkedList 로 할당
    
    // 값 추가
    q.add(1)    // 객체를 큐에 추가 (큐가 가득찬 상태이면 illegalStateException 발생)
    q.offer(3)  // 객체를 큐에 추가 (큐가 가득찬 상태이면 false 반환)
    
    
    // 객체 리턴(제거 아님!)
    println(q.element())    // 맨 앞 객체 리턴 (큐가 비어있는 상태이면 NoSuchElementException 발생)
    println(q.elementAt(1)) // 인덱스 값의 객체 리턴
    println(q.peek())   // 맨 앞 객체 리턴 (큐가 비어있는 상태이면 false 반환)

    // 맨 앞 객체 제거 후 반환
    q.remove()  // 삭제하면서 객체 반환 (큐가 비어있는 상태이면 NoSuchElementException 발생)
    var tmp = q.poll()  // 삭제하면서 객체 반환 (큐가 비어있는 상태이면 false 반환)
```


### List

 - #### List의 값 전체를 수정하고 싶다면
 ```kotlin
 val list = mutableListOf(0,1,2,3)
 
 // relaceAll메소드 사용. 모든 요소 1씩 증가
 list.replaceAll { it.plus(1) }
 
 // map 메소드 사용.  모든 요소 1씩 감소 
 val newList = list.map { it.minus(1) }
 
 ```
