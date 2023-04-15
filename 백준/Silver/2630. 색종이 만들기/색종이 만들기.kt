var blue=0
var white =0
fun main() {
    var n = readLine()!!.toInt()

    val arr = Array(n) { readLine()!!.split(" ").map { it.toInt() } }

    find(arr,0,0,n)

    println(white)
    println(blue)

}

fun find(arr:Array<List<Int>>,r:Int, c:Int, size:Int) {

    if(check(arr,r,c,size)) {
        if(arr[r][c]==0) white++
        else blue++

        return
    }
    var nextSize =size/2
    find(arr,r,c,nextSize)
    find(arr,r,c+nextSize,nextSize)
    find(arr,r+nextSize,c,nextSize)
    find(arr,r+nextSize,c+nextSize,nextSize)



}

fun check(arr:Array<List<Int>>, r:Int, c:Int, size:Int):Boolean {
    val first = arr[r][c]

    for( i in r until r + size) {
        for(j in c until c +size ){
            if(arr[i][j]!=first) {
                return false
            }
        }
    }
    return true
}