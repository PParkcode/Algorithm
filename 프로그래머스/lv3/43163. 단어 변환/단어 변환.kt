import java.util.*
import kotlin.collections.LinkedHashMap

class Solution {
    fun solution(begin: String, target: String, words: Array<String>):Int {

        var answer = 0

        val graph = LinkedHashMap<String,LinkedList<String>>()
        val q:Queue<String> = LinkedList()
        val visited = setOf<String>()


        graph[begin] = LinkedList()
        if(!words.contains(target)) {
            return 0
        }

        for(item in words) {
            graph[item] = LinkedList()
            if(canTranslate(begin,item)) {
                graph[begin]!!.add(item)
                graph[item]!!.add(begin)
            }

        }

        for(i in words.indices) {
            for (j in i until words.size) {
                if (i == j) {
                    continue
                }
                if(canTranslate(words[i],words[j])) {
                    graph[words[i]]!!.add(words[j])
                    graph[words[j]]!!.add(words[i])
                }
            }
        }

        q.add(begin)
        visited.plus(begin)

        var temp:String



        

        var qSize:Int
        
        while(q.isNotEmpty()) {
            qSize =q.size

            repeat(qSize) {
                temp = q.poll()
                if(temp=="-1") {
                    answer++
                }
                else{
                    if(temp == target) {
                        return answer +1
                    }


                    for(item in graph[temp]!!) {
                        if(!visited.contains(item)){
                            q.add(item)
                            visited.plus(item)
                        }
                    }
                }

            }
            q.add("-1")


        }



        return 0

    }
    fun canTranslate(a:String, b:String): Boolean{
        var count = 0
        for(i in a.indices) {
            if(a[i]!=b[i]) {
                count++
            }
        }

        return count == 1
    }
}