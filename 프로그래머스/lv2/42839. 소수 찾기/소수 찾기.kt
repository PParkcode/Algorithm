class Solution {
    val set = mutableSetOf<Int>()
    fun solution(numbers: String): Int {
        
        
        var answer = 0
        // 숫자를 쪼개서 조합
        recur("",numbers)
        
        
        
        // set의 숫자를 확인하여 소수인 수만 count
        for(item in set) {
            if(check(item)) {
                answer++
            }
        }
        return answer
    }
    
    fun recur(cur:String, others: String) { 
        // 현재 조합을 set에 추가
        if(cur != "") {
            set.add(cur.toInt())
        }
        
        // 조합을 새로하여 재귀 함수 실행
        for(i in others.indices) {
            recur(cur+others[i], others.substring(0,i) + others.substring(i+1))
        }
    }
    
    fun check(num:Int):Boolean {
        var count = 0
        if(num==0 || num == 1) {
            return false
        }
        for(i in 1 .. num) {
            
            if(num%i==0) {
                count ++
            }
            if(count>2) {
                return false
            }
        }
        return count == 2
    }
}