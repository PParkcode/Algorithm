class Solution {
    fun solution(numbers: IntArray, target: Int): Int {
        var answer = 0
        var idx = 0

        answer = find(numbers,0,target,0)
        return answer

    }

    fun find(numbers: IntArray,idx:Int,target: Int,current:Int):Int {
        
        if(idx == numbers.size) {
            if(current == target) {
                return 1
            }
            else{
                return 0
            }
        }
        var num = numbers[idx]

        var numPlus =current+num
        var numMinus = current - num


        var a =find(numbers,idx+1, target,numPlus)
        var b =find(numbers,idx +1, target, numMinus)
        //return find(numbers,idx+1, target,numPlus) + find(numbers,idx +1, target, numMinus)

        return a+b
    }
    
}