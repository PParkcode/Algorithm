import java.util.*

fun main() {

    val num = readLine()!!.toInt()
    var target:Int

    val minHeap = PriorityQueue<Int>()
    repeat(num) {
        target= readLine()!!.toInt()
        if(target>0) {
            minHeap.add(target)
        }
        else if(target==0) {
            if(minHeap.isEmpty()) {
                println("0")
            }
            else{
                println(minHeap.poll())
            }
        }
    }

}
