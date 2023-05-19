import java.util.*

class Solution {
    fun solution(queue1: IntArray, queue2: IntArray): Int {
        var answer: Int = 0
        
        
        val q1:Queue<Long> = LinkedList()
        val q2:Queue<Long> = LinkedList()
        
        for(idx in queue1.indices) {
            q1.add(queue1[idx].toLong())
            q2.add(queue2[idx].toLong())
        }
       
        var s1: Long = queue1.sum().toLong()
        var s2: Long = queue2.sum().toLong()
        
        var total:Long = s1 + s2
        var temp = 0L
        
        
        
        if(total%2==1L) return -1
        
        
    
        while(true) {
            
            if(answer>queue1.size*3) {
                answer =-1
                break
            }
            
            if(s1==s2) {
                break
            }
            if(s1>s2){
                temp = q1.remove()
                q2.add(temp)
                s1-=temp
                s2+=temp
                
                answer++
            }
            else {
                temp = q2.remove()
                q1.add(temp)
                
                s2-=temp
                s1+= temp
                answer++
            
            }
        }
        
        return answer
    }
}