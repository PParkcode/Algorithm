fun main() {

    val br = System.`in`.bufferedReader()
    val sb = StringBuilder()

    val num = br.readLine().toInt()

    var list = br.readLine().split(" ").map{ it.toInt()}

    val map :MutableMap<Int,Int> = HashMap()


    var sorted = list.sorted()

    var rank=0
    for(item in sorted) {

        if(!map.containsKey(item)) {
            map[item] = rank
            rank++
        }
    }

    for(item in list) {
        sb.append(map.get(item))
        sb.append(" ")
    }
    sb.deleteCharAt(sb.lastIndexOf(" "))
    print(sb.toString())

}

