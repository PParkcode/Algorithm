class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
       
        
        var a:Int =0
        var b:Int =0
        
        var tiles = brown + yellow
        var sum = (tiles +4 - yellow)/2
        
        for(i in 1 until sum) {
            if(i*(sum-i) == tiles) {
                if(i>sum-i) {
                    a=i
                    b=sum-i
                } else {
                    a = sum-i
                    b= i
                }
                break
            }
        }
        var answer = intArrayOf(a,b)
        return answer
        
    }
}