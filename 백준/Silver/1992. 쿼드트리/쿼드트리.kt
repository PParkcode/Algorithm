import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() {

    val bw = BufferedWriter(OutputStreamWriter(System.out))
    var num = readLine()!!.toInt()

    val arr:Array<String> = Array(num){ readLine()!! }

    find(bw,arr,0,0,num)
    bw.flush()

}
fun find(bw:BufferedWriter,arr:Array<String>, r:Int, c:Int,size:Int) {

    if(check(arr,r, c, size)) {
        if(arr[r][c]=='0'){
            bw.write("0")
        }
        else{
            bw.write("1")
        }

        return
    }

    bw.write("(")
    var nextSize = size/2
    find(bw,arr, r,c,nextSize)

    find(bw,arr,r,c+nextSize,nextSize)
    find(bw,arr,r+nextSize,c,nextSize)
    find(bw,arr,r+nextSize,c+nextSize,nextSize)
    bw.write(")")

}

fun check(arr:Array<String>,r:Int,c:Int,size:Int):Boolean {
    val first = arr[r][c]

    for(i in r until r+ size ){
        for(j in c until c+size) {
            if(arr[i][j]!=first) {
                return false
            }
        }
    }
    return true
}

