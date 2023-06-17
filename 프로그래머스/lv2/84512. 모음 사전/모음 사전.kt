class Solution {
    val list = listOf("A","E","I","O","U")
    var count = 0
    var answer = 0 
    fun solution(word: String): Int {
        
        //하나하나 다 확인하면서 카운트를 늘려야 하나?
        var now =""
        

        // count를 구하는 것까지는 좋은데 바로 종료해버리고 싶음
        // 어케 해야지?
        for(item in list) {
            if(answer>0) {
                break
            }
            recur(now+item,word)
        }
        println(count)
        return answer
    }
    
    
    
    fun recur(str:String,target:String) {
        count++
        if(answer>0) return
        
        if(str == target) {
            answer =count
            return 
        }
        
        if(str.length>=5) {
            return
        }
        
        for(item in list) {
           recur(str+item,target)
        }
        return
        
    }
}