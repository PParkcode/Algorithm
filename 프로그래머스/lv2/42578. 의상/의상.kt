class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        var answer = 1
    var hashMap = HashMap<String,Int>()
    
        for(item in clothes){
        if(hashMap.containsKey(item[1])){
            hashMap[item[1]] = hashMap[item[1]]!! + 1
        }
        else {
            hashMap[item[1]]=1
        }
    }

    for(i in hashMap) {
        println(i.value)
        answer *= (i.value+1)
    }

    return answer-1
    }
}