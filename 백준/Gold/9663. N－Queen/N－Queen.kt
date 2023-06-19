import kotlin.math.abs

var count =0

fun main() {
    val num = readLine()!!.toInt()
    val arr = Array(num) {IntArray(num)}


    for(col in 0 until num) {
        n_queens(arr,0,col)
    }
    println(count)

}

fun n_queens(arr:Array<IntArray>,i:Int, col:Int) {

    var size = arr.size
    if(i>=size) {
        return
    }
    if(promising(arr,i,col)) {

        arr[i][col] =1
        if(i==size-1) {
            count++
        }

        else {
            for(a in 0 until size) {
                n_queens(arr, i+1,a)
            }
        }
    }
    arr[i][col] = 0
}
//i는 depth 즉 y  col은 x좌표
fun promising(arr:Array<IntArray>,i:Int, col:Int):Boolean {

    for(y in 0 until i) {
        if(arr[y][col]==1) {
            return false
        }
    }
    for(a in 0 until i) {
        for( b in arr.indices){
            var difY = abs(a - i)
            var difX = abs(b - col)

            if(difX == difY && arr[a][b] == 1) {
                return false
            }
        }
    }
    return true
}