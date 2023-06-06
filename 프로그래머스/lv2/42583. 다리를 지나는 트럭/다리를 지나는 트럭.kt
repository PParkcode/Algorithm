import java.util.*

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
    var answer = 0
    val size = truck_weights.size
    var waitQ:Queue<Int> = LinkedList()
    var passingQ: Queue<Int> = LinkedList()
    var finishQ: Queue<Int> = LinkedList()
    var lengthQ = mutableListOf<Int>()

    for(i in truck_weights) {
        waitQ.add(i)
    }

    while(finishQ.size < size) {
        
        if(waitQ.isNotEmpty()) {
            // 무게 오케이
            if(totalWeight(queue = passingQ) + waitQ.peek() <= weight ) {
                passingQ.add(waitQ.poll())
                lengthQ.add(bridge_length)
            }
            
        }

        crossOneBlock(lengthQ)
        if(lengthQ.first()<=0) {
            finishQ.add(passingQ.poll())

            lengthQ.removeAt(0)
        }
        

        answer++

    }

    answer++

    return answer
}

fun totalWeight(queue: Queue<Int>):Int {
    var weight = 0

    for(item in queue) {
        weight +=item
    }
    return weight
}

fun crossOneBlock(bridge: MutableList<Int>) {
    bridge.replaceAll {it.minus(1)}
}
}

/**
다리를 건너는 트럭은 bridge_length만큼 후에 건널 수 있다.
 ex) length가 3이라면 1초부터 3초까지는 다리 위에 있어야 한다.
*/