import kotlin.collections.HashMap

fun main() {

    var (n,m) = readLine()!!.split(" ").map { it.toInt() }
    var temp:String
    val hashMap: HashMap<String,Int> = HashMap()
    val list = mutableListOf<String>()
    for(i in 1 ..n) {
        temp = readLine()!!.toString()
        hashMap.put(temp,i)
        list.add(temp)
    }
    var trans:Int
    repeat(m) {
        temp= readLine()!!

        try{
            trans= temp.toInt()
            println(list[trans-1])
        } catch(e:Exception) {
            println(hashMap.get(temp))
        }
    }

}
