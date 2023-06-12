import java.util.*

class Solution {
    fun solution(operations: Array<String>): IntArray {
        var answer = intArrayOf()
        var temp:Int
        
        
        
        var answerList:MutableList<Int> = mutableListOf()
        
        val minPq = PriorityQueue<Int>() 
        
        //최대 힙 코드
        val maxPq = PriorityQueue<Int>(Comparator<Int>{ a,b ->
            b.compareTo(a)
        })
        
        
        for(item in operations) {
            //큐에 집어 넣는 것은 문제 없음
            if(item[0] == 'I') {
                temp = item.substring(2).toInt()
                minPq.offer(temp)
                maxPq.offer(temp)
            }
            
            if(item[0] == 'D') {
                deleteItem(item ,minPq,maxPq)
            }
        }
        
        if(maxPq.isEmpty()){
            answerList.add(0)
            answerList.add(0)
        }
        else {
            answerList.add(maxPq.poll())
            answerList.add(minPq.poll())
        }
    
    
        return answerList.toIntArray()
    }
    
    fun deleteItem(item: String, minQ: PriorityQueue<Int>, maxQ: PriorityQueue<Int>) {
        
        var temp: Int
        if(item[2] == '-'){
            if(minQ.isNotEmpty()) {
                temp = minQ.poll()
                maxQ.remove(temp)
            }
            
        }
        else {
            if(maxQ.isNotEmpty()) {
                temp = maxQ.poll()
                minQ.remove(temp)
            }
        }
    }
    
    
}