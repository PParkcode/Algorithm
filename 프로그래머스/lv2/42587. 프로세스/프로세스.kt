import java.util.*

class Solution {
    fun solution(priorities: IntArray, location: Int): Int{

    var answer =0

    var flag:Boolean =false
    var temp :Pair<Int,Int>
    val q :Queue<Pair<Int,Int>> = LinkedList()
    for(i in priorities.indices) {
        q.add(Pair(i,priorities[i]))
    }

    //큐가 빌 때까지
    while(q.isNotEmpty() ) {
        flag= false

    // 값을 하나 꺼낸다.
        temp = q.poll()

    //큐를 순회하면서 우선순위가 높은게 있다면 큐에 다시 삽입하고 flag true
        for(item in q) {
            if(item.second > temp.second) {
                q.add(temp)
                flag = true
                break
            }
        }
    //높은게 있었다면 while문 continue
        if(flag) {
            continue
        }
        answer ++


    //큐에서 뽑은 값이 방문 처리된다면 반복문 탈출
        if(temp.first == location) {
            break
        }
    }

    return answer

}
}