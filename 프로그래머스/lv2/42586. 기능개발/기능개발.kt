import java.util.*

class Solution {
fun solution(progresses: IntArray, speeds: IntArray): IntArray {
    var answer = intArrayOf()
    var tempAnswer = mutableListOf<Int>()

    var temp =0
    val queue = mutableListOf<Int>()
    val speedQueue = mutableListOf<Int>()

    //큐 삽입
    for(i in progresses.indices) {
        queue.add(progresses[i])
        speedQueue.add(speeds[i])
    }


    while(queue.isNotEmpty()) {
        temp=0
        var count =0
        //진행도에 따른 값 추가
        for(i in queue.indices) {
            queue[i]+=speedQueue[i]
        }

        //첫번째 값이 100 이상이라면
        temp = check(queue,speedQueue,count)

        if(temp>0) {
            tempAnswer.add(temp)
        }


    }
    return tempAnswer.toIntArray()
}
// 재귀 함수로 값 리턴
fun check(queue:MutableList<Int>,speedQueue:MutableList<Int>,count:Int):Int {
    if(queue.isNotEmpty()) {
        if(queue[0]>=100) {
            queue.removeAt(0)
            speedQueue.removeAt(0)
            return 1 + check(queue,speedQueue,count)
        }
    }

    return 0
}
}