fun main() {

    val (n,r,c) = readLine()!!.split(" ").map { it.toInt() }
    var len=1
    repeat(n) {
        len*=2
    }
    var result = findPlace(r,c,len/2) -1
    println(result )
}

fun findPlace(r:Int, c:Int,half:Int):Int {
    if(half==0) {
        return r+c+1
    }
    if(r<half) {
        if(c<half) { //1사분면
            return findPlace(r,c,half/2)
        }
        else { //2사분면
            return findPlace(r,c-(half),half/2) + (half*half)
        }
    }
    else {
        if( c<half) { // 3사분면
            return findPlace(r-half, c,half/2) +(half*half*2)
        }
        else { // 4사분면
            return findPlace(r-half,c-half,half/2)+(half*half*3)
        }

    }
}