class Solution {
    fun solution(genres: Array<String>, plays: IntArray): IntArray {
    var answer = intArrayOf()
    var tempAnswer = mutableListOf<Int>()

    val totalMap = HashMap<String,Int>()
    val genreMap = HashMap<String, MutableList<Pair<Int,Int>>>()
    for(i in genres.indices) {
        if(totalMap.containsKey(genres[i])) {
            totalMap[genres[i]] = totalMap[genres[i]]!! + plays[i]
            genreMap[genres[i]]?.add(Pair(i,plays[i]))

        }
        else {
            totalMap[genres[i]] = plays[i]
            genreMap[genres[i]] = mutableListOf<Pair<Int,Int>>()
            genreMap[genres[i]]?.add(Pair(i,plays[i]))
        }
    }



    val sortedTotalMap = totalMap.toList().sortedByDescending { it.second }.toMap().toMutableMap()

    for((key,value) in sortedTotalMap) {
        var count =0
        genreMap[key]?.sortByDescending { it.second }



        for(item in genreMap[key]!!) {
            if(count<2) {
                tempAnswer.add(item.first)
                count++
            } else {
                break
            }
        }


    }

    answer =tempAnswer.toIntArray()
    return answer
}
    
}

