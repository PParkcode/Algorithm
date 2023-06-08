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
 
 ### PriorityQueue
 
 - #### 우선순위 큐의 시간 복잡도
 
   데이터 추가, 삭제 `offer()`, `poll()`  --> **O(logN)**


   최소값, 최대값 확인 `peek()`  --> **O(1)**

   데이터 검색  `contains()`  --> **O(logN)**
 
 ### Comparator
 
 `sortedWith` 함수는 비교자`(Comparator)`를 인자로 받습니다. 비교자는 두 개의 요소를 비교하여 정렬 순서를 결정합니다.


아래 코드 람다 표현식을 사용하여 비교자를 정의하고 있습니다.`{ a, b -> ... }`는 람다 표현식의 시작을 나타내며, a와 b는 비교되는 두 개의 요소를 나타냅니다.


```kotlin
list = list.sortedWith(Comparator<Int>{ a, b ->
        when {
            a > b -> 1
            a < b -> -1
            else -> 0
        }
    })
```

비교자 내부에서는 `when` 표현식을 사용하여 다음과 같이 세 가지 경우를 처리하고 있습니다:

- a > b : a가 b보다 큰 경우, 1을 반환합니다.
- a < b : a가 b보다 작은 경우, -1을 반환합니다.
- 그 외 (a == b) : a와 b가 같은 경우, 0을 반환합니다.

<br>

- 반환값이 1인 경우: a가 b보다 크다고 판단되어 a가 b보다 뒤에 위치합니다.
- 반환값이 -1인 경우: a가 b보다 작다고 판단되어 a가 b보다 앞에 위치합니다.
- 반환값이 0인 경우: a와 b가 같다고 판단되어 순서는 변하지 않습니다.


따라서, 이 코드에서는 요소간의 크기를 비교하여 오름차순으로 정렬하고자 하였습니다.


- #### PriorityQueue에서의 Comparator

```kotlin
val priorityQueue = PriorityQueue<Pair<Int, Int>>(Comparator { a, b ->
    a.second.compareTo(b.second) // Pair의 두 번째 값으로 비교하여 오름차순 정
})
```
`compareTo` 함수는 `Comparable` 인터페이스를 구현한 객체에서 사용할 수 있는 함수로, 비교 결과에 따라 정수 값을 반환합니다.


`a.second.compareTo(b.second)`는 a와 b의 두 번째 값을 비교하여 다음과 같이 반환합니다:

- 반환 값이 음수인 경우: a의 두 번째 값이 b의 두 번째 값보다 작음을 나타냅니다.
- 반환 값이 양수인 경우: a의 두 번째 값이 b의 두 번째 값보다 큼을 나타냅니다.
- 반환 값이 0인 경우: a의 두 번째 값과 b의 두 번째 값이 같음을 나타냅니다.


`PriorityQueue`에서 `Comparator`를 사용할 때, 비교 결과에 따라 우선순위가 결정되므로, `a.second.compareTo(b.second)`를 사용하면 `Pair`의 두 번째 값이 작은 순서대로 정렬되는 효과를 얻을 수 있습니다.
