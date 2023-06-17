import java.util.*
import kotlin.collections.*

class Solution {
    val graph = HashMap<Int,MutableList<Int>>()
    var answer = 99999
    val visited = mutableSetOf<Int>()
    fun solution(n: Int, wires: Array<IntArray>): Int {


        // 그래프를 걍 그리자 (출력 양호)
        for(edge in wires) {
            if(!graph.contains(edge[0])) {
                graph[edge[0]] = mutableListOf()
            }
            if(!graph.contains(edge[1])) {
                graph[edge[1]] = mutableListOf()
            }
            graph[edge[0]]!!.add(edge[1])
            graph[edge[1]]!!.add(edge[0])
        }

        // 간선을 돌면서 하나씩 잘라 보며 커넥트 갯수 구함
        for(node in graph) {
            var idx = node.value.size
            while(idx>0) {

                var temp = node.value.get(idx-1)
                node.value.removeAt(idx-1)
                calculate(node.key, n)

                node.value.add(temp)
                idx--
            }
        }


        return answer
    }
    fun calculate(a:Int, n:Int) {
        dfs(a)
        var t = visited.size
        var other = n - t
        var result:Int
        if(other>t) {
            result = other - t
        } else {
            result = t - other
        }
        visited.clear()

        if(answer>result) {
            answer = result
        }
    }
    fun dfs(num: Int) {
        visited.add(num)

        for(node in graph[num]!!) {
            if(!visited.contains(node)) {
                dfs(node)
            }
        }
    }
}