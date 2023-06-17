class Solution {
    var answer = 0 
    var count = 0
    var visited = BooleanArray(8)
    
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        
        for(i in dungeons.indices) {
            recur(dungeons, k,i)
        }
        return answer
    }
    
    fun recur(dungeons:Array<IntArray>, k: Int,idx:Int) {
        // 현재 피로도 갱신
        var now = k - dungeons[idx][1]
        // 방문 여부 갱신
        visited[idx] = true
        // count 갱신
        count++
        // 정답 갱신
        if(count>answer) {
            answer = count
        }
        
        
        //던전 탐색 
        for(i in dungeons.indices) {
            if(visited[i] == false && now>=dungeons[i][0]) {
                recur(dungeons,now, i)
            }
        }
        count--
        visited[idx] = false
    }
}