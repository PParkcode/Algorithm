import java.util.*
class Solution {
    
    fun solution(n: Int, computers: Array<IntArray>): Int {

    var answer= 0
    val q: Queue<Int> = LinkedList()
    var visited= arrayListOf<Boolean>()

    var temp:Int

    repeat(n) {
        visited.add(true)
    }


    for(idx in visited.indices) {
        if(visited[idx]) {
            q.add(idx)
            visited[idx] = false
            answer++
            println(idx)
        }
        else {
            continue
        }
        while(q.isNotEmpty()) {
            temp = q.poll() 
            visited[temp] = false
            
            for(i in computers[temp].indices) {
                if(visited[i] && computers[temp][i] == 1) {
                    q.add(i)
                    visited[i] = false
                }
            }
        }

    }

    return answer
}
    /*
    
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        var visited= mutableListOf<Int>()
        var temp:Int
        for(i in 0 until n){
            visited.add(0)
        }
        var queue:Queue<Int> = LinkedList()

        for(i in computers.indices){
            if(visited[i]==1){
                continue
            }
            queue.add(i)
            visited[i]=1

            while(queue.isNotEmpty()){
                temp=queue.remove()
                visited[temp]=1
                println(temp)
                for(i in computers[temp].indices){
                    if(i==temp) continue
                    if(computers[temp][i] ==1 && visited[i]!=1){
                        queue.add(i)

                    }
                }

            }
            answer++
        }

        return answer
    }
    
    */
}